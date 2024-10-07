from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

def scrape_website(website):
    print("Connecting to Scraping Browser...")

    # Initialize the WebDriver correctly with the valid path to chromedriver.exe
    chrome_service = Service(SBR_WEBDRIVER)
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Run headless if needed

    # Use webdriver.Chrome for local WebDriver instance
    with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
        driver.get(website)
        print("Page loaded successfully!")

        # Now you can scrape the page content after captcha is manually solved or skip captcha handling
        html = driver.page_source
        return html


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove elements like nav, footer, script, and style
    for tag in soup(["nav", "footer", "script", "style"]):
        tag.extract()


    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content



def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
