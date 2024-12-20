import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import os

# Categories and their maximum page numbers
categories = {
    "entertainment": {"base_url": "https://theonion.com/entertainment", "last_page": 378},
    "sports": {"base_url": "https://theonion.com/sports", "last_page": 378},
    "opinion": {"base_url": "https://theonion.com/opinion", "last_page": 586},
}

# Destination folder for saving files
output_folder = "/home/zwang1/cosc426/Final/Dataset"  # Update this with your desired path

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

    except requests.exceptions.RequestException as e:
        print(f"Error processing {url}: {e}")
    
    return article_urls

# Main function to process multiple categories and save results
if __name__ == "__main__":
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create folder if it doesn't exist

    for category, info in categories.items():
        all_unique_urls = set()  # Aggregate all unique URLs for this category
        print(f"\n=== Processing Category: {category.upper()} ===")
        for page_number in range(1, info["last_page"] + 1):
            page_urls = scrape_and_filter_urls(info["base_url"], page_number)
            all_unique_urls.update(page_urls)  # Add new URLs to the aggregate set
            sleep(1)  # Prevent overwhelming the server
        
        # Save results to a file
        output_file = os.path.join(output_folder, f"{category}_article_urls.txt")
        with open(output_file, "w") as file:
            for url in sorted(all_unique_urls):
                file.write(f"{url}\n")
        print(f"\nSaved {len(all_unique_urls)} unique article URLs to {output_file}")
