import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
import time

# Custom CSS to make tables responsive
st.markdown("""
<style>
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .content-wrapper {
        overflow-x: auto;
        max-width: 100%;
        white-space: nowrap;
    }
    .table-wrapper {
        display: inline-block;
        vertical-align: top;
        max-width: 100%;
        overflow-x: auto;
    }
    table {
        border-collapse: collapse;
        font-size: 14px;
        margin-bottom: 10px;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
        word-wrap: break-word;
        max-width: 200px;
    }
    .csv-data {
        white-space: pre-wrap;
        word-wrap: break-word;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("AI Web Scraper")

# Initialize session state for storing URLs
if "url_list" not in st.session_state:
    st.session_state.url_list = [{"name": "Link 1", "url": ""}]  # Automatically start with Link 1

# Function to add a new URL
def add_url():
    st.session_state.url_list.append({"name": f"Link {len(st.session_state.url_list) + 1}", "url": ""})

# Function to remove a URL by index
def remove_url(index):
    if 0 <= index < len(st.session_state.url_list):
        st.session_state.url_list.pop(index)

# Function to scrape websites
def scrape_websites():
    """Scrape the websites listed in the URL list."""
    urls_to_scrape = [url_info for url_info in st.session_state.url_list if url_info["url"].strip()]

    if urls_to_scrape:
        # Dictionary to store scraped content for each URL
        scraped_data = {}

        for idx, url_info in enumerate(urls_to_scrape):
            url = url_info["url"]
            name = url_info["name"]
            st.write(f"Scraping {name} ({idx + 1}/{len(urls_to_scrape)})")

            # Measure the start time
            start_time = time.time()

            # Scrape the website
            try:
                with st.spinner(f"Scraping {name}..."):
                    dom_content = scrape_website(url)
                    body_content = extract_body_content(dom_content)
                    cleaned_content = clean_body_content(body_content)

                # Measure the end time for scraping, extracting, and cleaning
                scrape_time = time.time() - start_time

                # Store the cleaned content in the dictionary
                scraped_data[name] = cleaned_content

                # Display the time taken to scrape, extract, and clean
                st.success(f"Scraping, extracting, and cleaning took {scrape_time:.2f} seconds for {name}.")

            except Exception as e:
                st.error(f"Error scraping {name}: {e}")

        # Store the scraped content in session state
        st.session_state.scraped_data = scraped_data

# Function to parse content
def parse_content():
    """Parse the scraped content based on the description."""
    parse_description = st.session_state.get("parse_description", "")

    if parse_description:
        parse_status_placeholder = st.empty()  # Use an empty container for dynamic status updates

        # Process the scraped content for each link name
        for idx, (name, content) in enumerate(st.session_state.scraped_data.items()):
            st.write(f"Parsing content ({idx + 1}/{len(st.session_state.scraped_data)})")

            # Measure the start time for parsing
            parse_start_time = time.time()

            try:
                # Split content into chunks and parse
                dom_chunks = split_dom_content(content)
                
                # Parsing with loading spinner for each link
                with st.spinner(f"Parsing content for {name}..."):
                    parsed_result = parse_with_ollama(dom_chunks, parse_description)

                # Measure the end time for parsing
                parse_time = time.time() - parse_start_time

                # Store parsed result in session state
                if 'parsed_results' not in st.session_state:
                    st.session_state.parsed_results = {}
                st.session_state.parsed_results[name] = parsed_result

                # Display the time taken to parse the content for each link using `st.success`
                st.success(f"Parsing took {parse_time:.2f} seconds for {name}.")

            except Exception as e:
                st.error(f"Error parsing {name}: {e}")

        # Clear the previous status message
        parse_status_placeholder.empty()
        st.success("Parsing completed.")

# Display current URLs with text inputs for URL and buttons for removal
for idx, url_info in enumerate(st.session_state.url_list):
    col1, col2 = st.columns([0.85, 0.15])  # Adjusted column widths for better alignment

    with col1:
        st.session_state.url_list[idx]["url"] = st.text_input(f"{url_info['name']}", value=url_info["url"], key=f"url_input_{idx}")
    
    with col2:
        if idx > 0:
            st.write("")  # Adds vertical space for better alignment of the Remove button
            st.button("Remove", key=f"remove_button_{idx}", on_click=remove_url, args=(idx,))

# Button to add a new URL (always available)
st.button("Add Link", on_click=add_url)

# Scraping Section
scrape_container = st.container()
with scrape_container:
    if st.button("Scrape Websites"):
        scrape_websites()
    
    # Display scraped content
    if "scraped_data" in st.session_state:
        st.subheader("Scraped Content")
        for name, content in st.session_state.scraped_data.items():
            with st.expander(f"View Cleaned Content for {name}"):
                st.text_area(f"Cleaned Content ({name})", content, height=300)

# Parsing Section
parse_container = st.container()
with parse_container:
    if "scraped_data" in st.session_state:
        st.session_state["parse_description"] = st.text_area("Describe what you want to parse from all the scraped content")
        if st.button("Parse Content"):
            parse_content()
        
        # Display parsed content
        if 'parsed_results' in st.session_state:
            st.subheader("Parsed Content")
            for name, result in st.session_state.parsed_results.items():
                with st.expander(f"View Parsed Content for {name}"):
                    st.markdown(result, unsafe_allow_html=True)