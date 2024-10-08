import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
import time

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

# Display current URLs with text inputs for URL and buttons for removal
for idx, url_info in enumerate(st.session_state.url_list):
    col1, col2 = st.columns([0.85, 0.15])  # Adjusted column widths for better alignment

    with col1:
        st.session_state.url_list[idx]["url"] = st.text_input(f"{url_info['name']}", value=url_info["url"], key=f"url_input_{idx}")
    
    with col2:
        # Display the remove button for all links except the first one (Link 1)
        if idx > 0:
            st.write("")  # This adds vertical space to align the button
            if st.button("Remove", key=f"remove_button_{idx}"):
                remove_url(idx)

# Button to add a new URL (always available)
if st.button("Add Link"):
    add_url()

# Step 2: Scrape the Websites
if st.button("Scrape Websites"):
    # Filter out empty URLs
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
                dom_content = scrape_website(url)
                body_content = extract_body_content(dom_content)
                cleaned_content = clean_body_content(body_content)

                # Measure the end time for scraping, extracting, and cleaning
                scrape_time = time.time() - start_time

                # Store the cleaned content in the dictionary
                scraped_data[name] = cleaned_content

                # Display the DOM content in an expandable text box
                with st.expander(f"View DOM Content for {name}"):
                    st.text_area(f"DOM Content ({name})", cleaned_content, height=300)

                # Display the time taken to scrape, extract, and clean
                st.write(f"Scraping, extracting, and cleaning took {scrape_time:.2f} seconds for {name}.")

            except Exception as e:
                st.write(f"Error scraping {name}: {e}")

        # Store the scraped content in session state
        st.session_state.scraped_data = scraped_data

# Step 3: Ask Questions About the Scraped Data
if "scraped_data" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse from all the scraped content")

    if st.button("Parse Content"):
        if parse_description:
            parse_status_placeholder = st.empty()  # Use an empty container for dynamic status updates
            parse_status_placeholder.write("Parsing the content...")

            # Process the scraped content for each link name
            for idx, (name, content) in enumerate(st.session_state.scraped_data.items()):
                st.write(f"Parsing content from {name} ({idx + 1}/{len(st.session_state.scraped_data)})")

                # Measure the start time for parsing
                parse_start_time = time.time()

                # Split content into chunks and parse
                dom_chunks = split_dom_content(content)
                parsed_result = parse_with_ollama(dom_chunks, parse_description)

                # Measure the end time for parsing
                parse_time = time.time() - parse_start_time

                # Display parsed result for each link name
                st.write(f"Parsed result for {name}:")
                st.write(parsed_result)

                # Display the time taken to parse the content for each link in green
                st.markdown(
                    f'<p style="color:green;">Parsing took {parse_time:.2f} seconds for {name}.</p>',
                    unsafe_allow_html=True,
                )

            # Clear the previous status message
            parse_status_placeholder.empty()
            st.write("Parsing completed.")

