import argparse
import sys
import time
from urllib.parse import urlsplit, urlunsplit

# You can import the amazing function you just wrote in the other file!
# (Assuming you saved your engine as 'scraper.py')
from scraper import get_emails 

try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS


def build_search_queries(niche, location="", include_domains=None):
    parts = [niche.strip(), location.strip()]
    base = " ".join(part for part in parts if part)

    query_templates = [
        "{base} contact page",
        "{base} contact us",
        "{base} email",
        "{base} lead generation",
        "{base} inquiry",
    ]

    queries = []
    site_domains = [domain.strip() for domain in (include_domains or []) if domain.strip()]

    for template in query_templates:
        if not base:
            continue

        query = template.format(base=base).strip()
        if site_domains:
            for domain in site_domains:
                queries.append(f"{query} site:{domain}")
        else:
            queries.append(query)

    return queries


def normalize_url(url):
    if not url:
        return ""

    parts = urlsplit(url.strip())
    if parts.scheme not in {"http", "https"}:
        return ""

    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query, ""))


def matches_domain_filters(url, include_domains=None, exclude_domains=None):
    domain = urlsplit(url).netloc.lower()

    include_domains = [domain_name.strip().lower() for domain_name in (include_domains or []) if domain_name.strip()]
    exclude_domains = [domain_name.strip().lower() for domain_name in (exclude_domains or []) if domain_name.strip()]

    if include_domains and not any(domain_name in domain for domain_name in include_domains):
        return False

    if exclude_domains and any(domain_name in domain for domain_name in exclude_domains):
        return False

    return True


def hunt_for_clients(niche, location="", max_results=10, include_domains=None, exclude_domains=None):
    queries = build_search_queries(niche, location, include_domains=include_domains)
    print(f"\n[*] Deploying Spider for niche: '{niche}'")
    if location:
        print(f"[*] Location filter: '{location}'")
    if include_domains:
        print(f"[*] Include domains: {', '.join(include_domains)}")
    if exclude_domains:
        print(f"[*] Exclude domains: {', '.join(exclude_domains)}")

    seen_urls = set()
    url_list = []

    try:
        with DDGS() as ddgs:
            for query in queries:
                print(f"[*] Searching: {query}")
                results = list(ddgs.text(query, max_results=max_results))

                for result in results:
                    raw_url = result.get("href") or result.get("url") or result.get("link") or ""
                    normalized_url = normalize_url(raw_url)
                    if not normalized_url or normalized_url in seen_urls:
                        continue

                    if not matches_domain_filters(normalized_url, include_domains=include_domains, exclude_domains=exclude_domains):
                        continue

                    seen_urls.add(normalized_url)
                    url_list.append(normalized_url)

                    if len(url_list) >= max_results:
                        return url_list

        return url_list
    except Exception as error:
        print(f"[!] Search failed: {error}")
        return url_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Niche-targeted email spider")
    parser.add_argument("niche", nargs="?", default="marketing agency", help="Industry or market to target")
    parser.add_argument("--location", default="India", help="Optional location filter")
    parser.add_argument("--max-results", type=int, default=5, help="Maximum unique URLs to scrape")
    parser.add_argument("--delay", type=float, default=3.0, help="Pause between target sites in seconds")
    parser.add_argument("--include-domain", action="append", default=[], help="Only keep results from these domains (repeatable)")
    parser.add_argument("--exclude-domain", action="append", default=[], help="Skip results from these domains (repeatable)")
    parser.add_argument("--render-js", action="store_true", help="Try rendering target pages with JavaScript")
    parser.add_argument("--no-crawl-related", action="store_true", help="Only scrape the discovered URL, not contact/about pages")
    parser.add_argument("--max-related-pages", type=int, default=5, help="Maximum related pages to crawl per target")
    args = parser.parse_args()

    target_urls = hunt_for_clients(
        args.niche,
        location=args.location,
        max_results=args.max_results,
        include_domains=args.include_domain,
        exclude_domains=args.exclude_domain,
    )

    # 3. Feed them to your Engine!
    print(f"[*] Found {len(target_urls)} potential targets. Initiating extraction...")

    for url in target_urls:
        try:
            # Call YOUR function from scraper.py
            get_emails(url, render_js=args.render_js, crawl_related=not args.no_crawl_related, max_related_pages=args.max_related_pages)

            # Be polite to servers: Sleep for 3 seconds before hitting the next website
            print("[-] Pausing to evade bot detection...")
            time.sleep(args.delay)
        except Exception as e:
            print(f"[!] Target {url} failed: {e}")

    print("\n[***] SPIDER MISSION COMPLETE. Check your business_leads.txt file. [***]")
