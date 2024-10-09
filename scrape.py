from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

# Initialize Chrome WebDriver
def init_webdriver():
    """Initialize Chrome WebDriver."""
    chrome_service = Service(SBR_WEBDRIVER)
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Run headless for better performance
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

# Scrape a website using Selenium WebDriver
def scrape_website(website):
    """Scrape the given website and return the page source."""
    print("Connecting to Scraping Browser...")
    driver = init_webdriver()

    try:
        driver.get(website)
        print("Page loaded successfully!")
        html = driver.page_source
        return html
    finally:
        driver.quit()  # Ensure the browser is closed after scraping

# Extract the body content from the HTML using BeautifulSoup
def extract_body_content(html_content):
    """Extract the body content from HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# Clean the body content by removing unnecessary tags and getting clean text
def clean_body_content(body_content):
    """Clean the extracted body content by removing unwanted tags."""
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove elements like nav, footer, script, and style
    for tag in soup(["nav", "footer", "script", "style"]):
        tag.extract()

    # Get cleaned text
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# Split large DOM content into smaller chunks for easier parsing
def split_dom_content(dom_content, max_length=6000):
    """Split the DOM content into smaller chunks."""
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
