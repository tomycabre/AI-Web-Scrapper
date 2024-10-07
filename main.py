import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
import time  # Import time for measuring execution time

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Measure the start time
        start_time = time.time()

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Measure the end time for scraping, extracting, and cleaning
        scrape_time = time.time() - start_time

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

        # Display the time taken to scrape, extract, and clean
        st.write(f"Scraping, extracting, and cleaning took {scrape_time:.2f} seconds.")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            # Use an empty container to display the dynamic status
            parse_status_placeholder = st.empty()
            parse_status_placeholder.write("Parsing the content...")

            # Measure the start time for parsing
            parse_start_time = time.time()

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)

            # Measure the end time for parsing
            parse_time = time.time() - parse_start_time

            # Clear the previous status message
            parse_status_placeholder.empty()

            # Display "Parsed" when done
            st.write("Parsed")

            # Display parsed result
            st.write(parsed_result)

            # Display the time taken to parse the content in green
            st.markdown(
                f'<p style="color:green;">Parsing took {parse_time:.2f} seconds.</p>',
                unsafe_allow_html=True,
            )

