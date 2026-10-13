import sys
import time

# You can import the amazing function you just wrote in the other file!
# (Assuming you saved your engine as 'scraper.py')
from scraper import get_emails 

try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS


def hunt_for_clients(search_query, max_results=10):
    print(f"\n[*] Deploying Spider to search for: '{search_query}'")
    
    # Use DDGS to search the web
    try:
        with DDGS() as ddgs:
            # We grab the top search results
            results = list(ddgs.text(search_query, max_results=max_results))

            url_list = []
            for result in results:
                # Extract just the web link from the search result
                url_list.append(result['href'])

            return url_list
    except Exception as error:
        print(f"[!] Search failed: {error}")
        return []


if __name__ == "__main__":
    target = " ".join(sys.argv[1:]).strip() or "marketing agency contact page India"

    # 2. Get 5 target URLs
    target_urls = hunt_for_clients(target, max_results=5)

    # 3. Feed them to your Engine!
    print(f"[*] Found {len(target_urls)} potential targets. Initiating extraction...")

    for url in target_urls:
        try:
            # Call YOUR function from scraper.py
            get_emails(url)

            # Be polite to servers: Sleep for 3 seconds before hitting the next website
            print("[-] Pausing to evade bot detection...")
            time.sleep(3)
        except Exception as e:
            print(f"[!] Target {url} failed: {e}")

    print("\n[***] SPIDER MISSION COMPLETE. Check your business_leads.txt file. [***]")
