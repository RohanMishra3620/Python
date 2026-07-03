import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import random

# --- CONFIGURATION ---
SITEMAP_URL = "https://medium.com/sitemap/sitemap.xml" # Update to your actual sitemap
YOUR_BASE_DOMAIN = "medium.com"

def get_blog_urls(sitemap_url):
    """Reads sitemap.xml and extracts all blog URLs."""
    print(f"Reading sitemap: {sitemap_url}")
    
    # Disguise the script as a normal Google Chrome browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(sitemap_url, headers=headers, timeout=10)
        print(f"Server Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print("⚠️ The server did not return a successful response. It might be blocking bots or the URL is wrong.")
            return []

        soup = BeautifulSoup(response.content, "xml")
        
        # Extract all <loc> tags from the XML
        urls = [loc.text for loc in soup.find_all("loc")]
        print(f"Found {len(urls)} URLs in sitemap.")
        return urls
        
    except Exception as e:
        print(f"⚠️ Error fetching sitemap: {e}")
        return []


def extract_external_backlinks(url, base_domain):
    """Opens a blog and extracts all external backlinks."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        
        external_links = []
        for a_tag in soup.find_all("a", href=True):
            href = a_tag['href']
            parsed_href = urlparse(href)
            
            # Check if it's an external HTTP/HTTPS link
            if parsed_href.scheme in ['http', 'https'] and base_domain not in parsed_href.netloc:
                external_links.append(href)
                
        return external_links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def check_http_status(url):
    """Checks the HTTP status of a given URL."""
    try:
        # Use HEAD request for speed, fallback to GET if needed
        response = requests.head(url, timeout=10, allow_redirects=True)
        return response.status_code
    except requests.RequestException:
        return 404 # Treat connection errors as dead links

def check_google_index(url):
    """Opens Playwright, searches Google, and checks if indexed."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        
        search_query = f"site:{url}"
        google_url = f"https://www.google.com/search?q={search_query}"
        
        try:
            page.goto(google_url)
            # Randomized delay to help avoid immediate CAPTCHA blocks
            time.sleep(random.uniform(2.0, 5.0)) 
            
            content = page.content()
            
            # Watch out for Google's CAPTCHA wall
            if "Our systems have detected unusual traffic" in content:
                print("⚠️ Google triggered a CAPTCHA! You are temporarily blocked.")
                return "CAPTCHA Blocked"
                
            # Check for Google's standard "did not match" message
            if "did not match any documents" in content or "No results found for" in content:
                is_indexed = "Not Indexed"
            else:
                is_indexed = "Indexed"
                
        except Exception as e:
            print(f"Error checking index for {url}: {e}")
            is_indexed = "Error"
            
        finally:
            browser.close()
            
        return is_indexed

def main():
    print("--- Starting SEO Backlink Audit ---")
    
    # 1. Read Sitemap & Get Blog URLs
    blog_urls = get_blog_urls(SITEMAP_URL)
    
    if not blog_urls:
        print("No URLs found. Exiting.")
        return

    # 2. Open every blog and extract external backlinks
    all_external_links = []
    print("Extracting backlinks...")
    for blog in blog_urls:
        links = extract_external_backlinks(blog, YOUR_BASE_DOMAIN)
        all_external_links.extend(links)
        
    # 3. Remove duplicate backlinks
    unique_links = list(set(all_external_links))
    print(f"Found {len(unique_links)} unique external backlinks.")
    
    results = []
    
    # Process each unique backlink
    for link in unique_links:
        print(f"\nProcessing: {link}")
        
        # 4. Check HTTP Status
        status_code = check_http_status(link)
        print(f"Status Code: {status_code}")
        
        # 5 & 6. Open Headless Browser & Check Google Index
        # We only check indexing if the page actually exists (Status 200)
        if status_code == 200:
            index_status = check_google_index(link)
        else:
            index_status = "Skipped (Dead Link)"
            
        print(f"Index Status: {index_status}")
        
        # Stop execution to prevent complete IP ban if Google flags us
        if index_status == "CAPTCHA Blocked":
            print("Stopping index checks to avoid IP ban.")
            break

        # 7. Store Result
        results.append({
            "Backlink URL": link,
            "HTTP Status": status_code,
            "Google Index Status": index_status
        })
        
    # 8. Generate Report
    print("\nGenerating Report...")
    df = pd.DataFrame(results)
    df.to_csv("backlink_audit_report.csv", index=False)
    print("Success! Report saved to 'backlink_audit_report.csv'.")
    print("--- End ---")

if __name__ == "__main__":
    main()