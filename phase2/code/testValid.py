'''import requests
from bs4 import BeautifulSoup
import re
from time import sleep

# Base URL for the sports category
categories = {
    "sports": {"base_url": "https://theonion.com/sports", "last_page": 3},  # Testing first 3 pages
}

# Function to scrape and filter article URLs
def scrape_and_filter_urls(base_url, page_number):
    """Scrape article URLs from a single page and filter out non-article links."""
    url = f"{base_url}/page/{page_number}/" if page_number > 1 else base_url
    print(f"Processing page: {url}")

    article_urls = set()  # Use a set to ensure uniqueness
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache",
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all <a> tags with href attributes
        all_links = soup.find_all('a', href=True)
        for link in all_links:
            href = link['href']
            # Match URLs that look like articles
            if re.match(r'^https://theonion.com/[a-zA-Z0-9\-]+/$', href):
                # Filter out static/navigation URLs
                if not any(x in href for x in ['about-us', 'cookie-policy', 'privacy-policy', 'latest', 'terms-of-use', 'video', 'sports']):
                    article_urls.add(href)  # Add to set to prevent duplicates

        print(f"Found {len(article_urls)} unique article URLs on page {page_number}:")
        for idx, article_url in enumerate(sorted(article_urls), start=1):
            print(f"{idx}. {article_url}")

    except requests.exceptions.RequestException as e:
        print(f"Error processing {url}: {e}")
    
    return article_urls

# Main function to process multiple pages and aggregate unique URLs
if __name__ == "__main__":
    all_unique_urls = set()  # Aggregate all unique URLs across pages

    for category, info in categories.items():
        print(f"\n=== Processing Category: {category.upper()} ===")
        for page_number in range(1, 4):  # Process pages 1, 2, and 3
            page_urls = scrape_and_filter_urls(info["base_url"], page_number)
            all_unique_urls.update(page_urls)  # Add new URLs to the aggregate set
            sleep(1)  # Prevent overwhelming the server

    # Print final list of unique URLs
    print(f"\n=== Total Unique Article URLs Found: {len(all_unique_urls)} ===")
    for idx, url in enumerate(sorted(all_unique_urls), start=1):
        print(f"{idx}. {url}") 
'''

import requests
from bs4 import BeautifulSoup
import re
from time import sleep

# Base URL for the sports category
categories = {
    "sports": {"base_url": "https://theonion.com/sports", "last_page": 3},  # Testing first 3 pages
}

# Function to scrape and filter article URLs
def scrape_and_filter_urls(base_url, page_number):
    """Scrape article URLs from a single page and filter out non-article links."""
    url = f"{base_url}/page/{page_number}/" if page_number > 1 else base_url
    print(f"Processing page: {url}")

    article_urls = set()  # Use a set to ensure uniqueness
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache",
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all <a> tags with href attributes
        all_links = soup.find_all('a', href=True)
        for link in all_links:
            href = link['href']
            # Match URLs that look like articles with numeric IDs
            if re.match(r'^https://theonion.com/[a-zA-Z0-9\-]+-\d+/$', href):
                article_urls.add(href)  # Add to set to prevent duplicates

        print(f"Found {len(article_urls)} unique article URLs on page {page_number}:")
        for idx, article_url in enumerate(sorted(article_urls), start=1):
            print(f"{idx}. {article_url}")

    except requests.exceptions.RequestException as e:
        print(f"Error processing {url}: {e}")
    
    return article_urls

# Main function to process multiple pages and aggregate unique URLs
if __name__ == "__main__":
    all_unique_urls = set()  # Aggregate all unique URLs across pages

    for category, info in categories.items():
        print(f"\n=== Processing Category: {category.upper()} ===")
        for page_number in range(1, 4):  # Process pages 1, 2, and 3
            page_urls = scrape_and_filter_urls(info["base_url"], page_number)
            all_unique_urls.update(page_urls)  # Add new URLs to the aggregate set
            sleep(1)  # Prevent overwhelming the server

    # Print final list of unique URLs
    print(f"\n=== Total Unique Article URLs Found: {len(all_unique_urls)} ===")
    for idx, url in enumerate(sorted(all_unique_urls), start=1):
        print(f"{idx}. {url}")
