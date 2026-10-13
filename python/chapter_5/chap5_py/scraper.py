import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests


EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
CONTACT_HINTS = (
    "contact",
    "contact-us",
    "about",
    "about-us",
    "team",
    "support",
    "reach-us",
    "get-in-touch",
    "connect",
)

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "Mozilla/5.0"})


def normalize_url(url: str):
    if not url:
        return ""

    parts = urlsplit(url.strip())
    if parts.scheme not in {"http", "https"}:
        return ""

    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query, ""))


def is_same_domain(url_a: str, url_b: str):
    return urlsplit(url_a).netloc.lower() == urlsplit(url_b).netloc.lower()


def fetch_html(url: str, render_js: bool = False):
    if render_js:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            print("[!] Playwright is not installed; falling back to requests.")
        else:
            try:
                with sync_playwright() as playwright:
                    browser = playwright.chromium.launch(headless=True)
                    page = browser.new_page(user_agent="Mozilla/5.0")
                    page.goto(url, wait_until="networkidle", timeout=30000)
                    html = page.content()
                    browser.close()
                    return html
            except Exception as error:
                print(f"[!] JS render failed: {error}. Falling back to requests.")

    try:
        response = SESSION.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Failed to fetch page: {error}")
        return ""


def extract_emails_from_html(html: str):
    return sorted(set(re.findall(EMAIL_PATTERN, html)))


def extract_internal_links(html: str, base_url: str):
    links = []
    href_matches = re.findall(r'href=["\']?([^"\'\s>]+)', html, flags=re.IGNORECASE)

    for href in href_matches:
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue

        absolute_url = normalize_url(urljoin(base_url, href))
        if not absolute_url or not is_same_domain(absolute_url, base_url):
            continue

        if absolute_url not in links:
            links.append(absolute_url)

    return links


def discover_related_pages(url: str, html: str, max_related_pages: int = 5):
    pages = []
    normalized_root = normalize_url(url)

    if normalized_root:
        pages.append(normalized_root)

    for link in extract_internal_links(html, url):
        path = urlsplit(link).path.lower()
        if any(hint in path for hint in CONTACT_HINTS) and link not in pages:
            pages.append(link)

        if len(pages) >= max_related_pages:
            break

    return pages


def load_existing_emails(output_path: str = "business_leads.txt"):
    file_path = Path(output_path)
    if not file_path.exists():
        return set()

    with file_path.open("r", encoding="utf-8") as file:
        return {line.strip() for line in file if line.strip()}


def save_emails(emails, output_path: str = "business_leads.txt"):
    merged = sorted(set(emails) | load_existing_emails(output_path))

    with Path(output_path).open("w", encoding="utf-8") as file:
        for email in merged:
            file.write(email + "\n")


def get_emails(url: str, render_js: bool = False, crawl_related: bool = True, max_related_pages: int = 5):
    print(f"Downloading HTML from {url}...")

    discovered_emails = set()
    base_html = fetch_html(url, render_js=render_js)
    if not base_html:
        return []

    pages_to_visit = discover_related_pages(url, base_html, max_related_pages=max_related_pages) if crawl_related else [normalize_url(url) or url]

    for page_url in pages_to_visit:
        html = base_html if normalize_url(page_url) == normalize_url(url) else fetch_html(page_url, render_js=render_js)
        if not html:
            continue

        print(f"Scanning HTML for email addresses on {page_url}...")
        found_emails = extract_emails_from_html(html)

        if not found_emails:
            print("No email addresses found.")
            continue

        for email in found_emails:
            if email not in discovered_emails:
                print(f"Found: {email}")
            discovered_emails.add(email)

    if not discovered_emails:
        return []

    save_emails(discovered_emails)
    print("Scraping complete. Leads saved to business_leads.txt")
    return sorted(discovered_emails)


if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "https://cimage.in/"
    get_emails(target_url)
