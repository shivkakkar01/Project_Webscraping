import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import BASE_URL, OPINION_SECTION_URL, DOWNLOADS_FOLDER

def setup_driver():
    """Setup Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
    options.add_argument("--no-sandbox")  # Required for some environments
    service = Service("C:\Driver\chromedriver.exe")  # No need for full path if added to PATH
    return webdriver.Chrome(service=service, options=options)

def scrape_articles():
    """Scrape article titles, contents, and images."""
    driver = setup_driver()
    driver.get(OPINION_SECTION_URL)

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    articles = soup.select("article")[:5]  # Fetch first 5 articles

    scraped_data = []
    for article in articles:
        try:
            title = article.find("h2").get_text(strip=True)
            content_url = article.find("a")["href"]
            cover_image_url = article.find("img")["src"] if article.find("img") else None

            # Visit article page
            driver.get(BASE_URL + content_url)
            content_soup = BeautifulSoup(driver.page_source, "html.parser")
            content_element = content_soup.select_one(".article_body")
            content = content_element.get_text(strip=True) if content_element else "Content not found"

            # Save cover image
            image_path = None
            if cover_image_url:
                image_path = os.path.join(DOWNLOADS_FOLDER, os.path.basename(cover_image_url))
                download_image(cover_image_url, image_path)

            scraped_data.append({
                "title": title,
                "content": content,
                "image_path": image_path,
            })
        except Exception as e:
            print(f"Error scraping article: {e}")

    driver.quit()
    return scraped_data

def download_image(url, path):
    """Download an image from a URL."""
    os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise exception for HTTP errors
        with open(path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    except Exception as e:
        print(f"Error downloading image: {e}")

# Example usage
if __name__ == "__main__":
    articles = scrape_articles()
    for article in articles:
        print("Title:", article["title"])
        print("Content:", article["content"][:200], "...\n")  # Print first 200 characters of content
        if article["image_path"]:
            print("Image saved at:", article["image_path"])
        print("-" * 80)