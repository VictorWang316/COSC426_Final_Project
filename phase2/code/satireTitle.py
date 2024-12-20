'''import requests
from bs4 import BeautifulSoup
import time

# Base URL for the Faux News section
base_url = "https://www.humortimes.com/topics/faux-news/page/"

# List to store article titles
titles = []

# Function to scrape a single page
def scrape_page(page_num):
    url = f"{base_url}{page_num}/"
    print(f"Processing page {page_num}: {url}")
    
    try:
        # Send a GET request to the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article titles on the page
        for article in soup.find_all('article'):
            # Extract the title text
            title_tag = article.find('h2', class_='entry-title')
            if title_tag and title_tag.a:
                title = title_tag.a.get_text(strip=True)
                titles.append(title)
    except requests.exceptions.RequestException as e:
        print(f"Error processing page {page_num}: {e}")

# Maximum number of pages to scrape (set high enough to cover all content)
max_pages = 2000  # Adjust as necessary

# Loop through pages until we reach the limit or no more titles
for page_num in range(1, max_pages + 1):
    scrape_page(page_num)
    
    # Stop if we've collected 10,000 titles
    if len(titles) >= 10000:
        print("Reached 10,000 titles. Stopping.")
        break
    
    # Pause to respect the site's server (adjust as needed)
    time.sleep(0.5)

# Save the titles to a text file
output_file = "/home/zwang1/cosc426/Final/Dataset/Satire/new_satire_titles.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for title in titles:
        file.write(title + "\n")

print(f"Scraping complete. {len(titles)} titles saved to '{output_file}'.")
'''

''' Code that works
import requests
from bs4 import BeautifulSoup

# Base URL for the "Opinion" section of The Onion
url = "https://theonion.com/opinion/"

# Function to scrape titles
def scrape_titles(url):
    print(f"Fetching content from: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Locate titles in <h2> tags with class containing 'wp-block-post-title'
        titles = soup.find_all("h2", class_="wp-block-post-title")
        
        # Extract and display titles
        if titles:
            print(f"Extracted {len(titles)} titles:")
            for idx, tag in enumerate(titles, start=1):
                print(f"{idx}. {tag.get_text(strip=True)}")
        else:
            print("No titles found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_titles(url)
'''
'''
import requests
from bs4 import BeautifulSoup

# Categories with their base URLs
categories = {
    "opinion": "https://theonion.com/opinion",
    "politics": "https://theonion.com/politics",
    "entertainment": "https://theonion.com/entertainment",
}

# Function to scrape a single page of a category
def scrape_page(base_url, page_number):
    url = f"{base_url}/page/{page_number}" if page_number > 1 else base_url
    print(f"Processing page: {url}")
    
    titles = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract titles from <h2> tags with the specific class
        for tag in soup.find_all('h2', class_='wp-block-post-title'):
            titles.append(tag.get_text(strip=True))
        
        if titles:
            print(f"Extracted titles from {url}:")
            for idx, title in enumerate(titles, start=1):
                print(f"{idx}. {title}")
        else:
            print(f"No titles found on {url}.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error processing {url}: {e}")
    
    return titles

# Function to test scraping of first two pages of each category
def test_categories(categories):
    for category, base_url in categories.items():
        print(f"\n=== Testing Category: {category.upper()} ===")
        for page_number in range(1, 3):  # Test the first two pages
            scrape_page(base_url, page_number)

# Execute the test
if __name__ == "__main__":
    test_categories(categories)
'''


'''import requests
from bs4 import BeautifulSoup
from time import sleep

# Categories with their base URLs and number of pages
categories = {
    "opinion": {"base_url": "https://theonion.com/opinion", "last_page": 586},
    "politics": {"base_url": "https://theonion.com/politics", "last_page": 309},
    "entertainment": {"base_url": "https://theonion.com/entertainment", "last_page": 378},
}

# Function to scrape all pages of a category
def scrape_all_pages(base_url, last_page):
    titles = []
    for page_number in range(1, last_page + 1):
        url = f"{base_url}/page/{page_number}" if page_number > 1 else base_url
        print(f"Processing page: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract titles from <h2> tags with the specific class
            for tag in soup.find_all('h2', class_='wp-block-post-title'):
                titles.append(tag.get_text(strip=True))
            
        except requests.exceptions.RequestException as e:
            print(f"Error processing {url}: {e}")
            continue
        
        # Sleep to prevent overwhelming the server
        sleep(1)
    
    return titles

# Function to scrape all categories
def scrape_categories(categories):
    all_titles = []
    for category, info in categories.items():
        print(f"\n=== Scraping Category: {category.upper()} ===")
        titles = scrape_all_pages(info["base_url"], info["last_page"])
        all_titles.extend(titles)  # Combine all titles into one list
        print(f"Scraped {len(titles)} titles for category: {category}")
    
    return all_titles

# Save titles to a specific file location
def save_titles_to_file(titles_list, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        for title in titles_list:
            file.write(f"{title}\n")
    print(f"Titles saved to {filepath}")

# Execute the scraping
if __name__ == "__main__":
    # Specify the file path to save the titles
    save_path = "/home/zwang1/cosc426/Final/Dataset/Satire/TOADD.txt"  # Replace with your desired path
    all_titles = scrape_categories(categories)
    save_titles_to_file(all_titles, save_path)'''

'''import requests
from bs4 import BeautifulSoup
from time import sleep

# New categories with their base URLs and number of pages
categories = {
    "sports": {"base_url": "https://theonion.com/sports", "last_page": 378},
    "news": {"base_url": "https://theonion.com/news", "last_page": 843},
    "local": {"base_url": "https://theonion.com/local", "last_page": 498},
}

# Function to scrape all pages of a category
def scrape_all_pages(base_url, last_page):
    titles = []
    for page_number in range(1, last_page + 1):
        url = f"{base_url}/page/{page_number}" if page_number > 1 else base_url
        print(f"Processing page: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract titles from <h2> tags with the specific class
            for tag in soup.find_all('h2', class_='wp-block-post-title'):
                titles.append(tag.get_text(strip=True))
            
        except requests.exceptions.RequestException as e:
            print(f"Error processing {url}: {e}")
            continue
        
        # Sleep to prevent overwhelming the server
        sleep(1)
    
    return titles

# Function to scrape all categories
def scrape_categories(categories):
    all_titles = []
    for category, info in categories.items():
        print(f"\n=== Scraping Category: {category.upper()} ===")
        titles = scrape_all_pages(info["base_url"], info["last_page"])
        all_titles.extend(titles)  # Combine all titles into one list
        print(f"Scraped {len(titles)} titles for category: {category}")
    
    return all_titles

# Save titles to a specific file location
def save_titles_to_file(titles_list, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        for title in titles_list:
            file.write(f"{title}\n")
    print(f"Titles saved to {filepath}")

# Execute the scraping
if __name__ == "__main__":
    # Specify the file path to save the titles for these categories
    save_path = "/home/zwang1/cosc426/Final/Dataset/Satire/TOADDOther.txt"  # Replace with your desired path
    all_titles = scrape_categories(categories)
    save_titles_to_file(all_titles, save_path)'''

import requests
from bs4 import BeautifulSoup
from time import sleep

# Categories with their base URLs and number of pages
categories = {
    "sports": {"base_url": "https://theonion.com/sports", "last_page": 378},
    "news": {"base_url": "https://theonion.com/news", "last_page": 843},
    "local": {"base_url": "https://theonion.com/local", "last_page": 498},
}

# Function to scrape all pages of a category
def scrape_all_pages(base_url, last_page):
    titles = set()  # Use a set to ensure uniqueness
    for page_number in range(1, last_page + 1):
        # Correct URL structure with trailing slash
        url = f"{base_url}/page/{page_number}/" if page_number > 1 else base_url
        print(f"Processing page: {url}")
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Cache-Control": "no-cache",
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract titles from <h2> tags with the specific class
            new_titles = [
                tag.get_text(strip=True)
                for tag in soup.find_all('h2', class_='wp-block-post-title')
            ]
            
            print(f"Page {page_number} has {len(new_titles)} titles: {new_titles}")
            
            # Update titles set to avoid duplicates
            titles.update(new_titles)
        
        except requests.exceptions.RequestException as e:
            print(f"Error processing {url}: {e}")
            continue
        
        # Sleep to prevent overwhelming the server
        sleep(1)
    
    return list(titles)

# Function to scrape all categories
def scrape_categories(categories):
    all_titles = []
    for category, info in categories.items():
        print(f"\n=== Scraping Category: {category.upper()} ===")
        titles = scrape_all_pages(info["base_url"], info["last_page"])
        all_titles.extend(titles)  # Combine all titles into one list
        print(f"Scraped {len(titles)} unique titles for category: {category}")
    
    return all_titles

# Save titles to a specific file location
def save_titles_to_file(titles_list, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        for title in titles_list:
            file.write(f"{title}\n")
    print(f"Titles saved to {filepath}")

# Execute the scraping
if __name__ == "__main__":
    # Specify the file path to save the titles for these categories
    save_path = "/path/to/your/directory/additional_titles.txt"  # Replace with your desired path
    all_titles = scrape_categories(categories)
    save_titles_to_file(all_titles, save_path)
