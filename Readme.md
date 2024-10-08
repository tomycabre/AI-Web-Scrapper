# AI-Based Real Estate Web Scraper

Welcome to our AI-based web scraper project, designed to efficiently extract data using advanced machine learning models to gather and process real estate listings, providing users with structured and valuable information.

## Prerequisites

Ensure you have Python 3.12.5 installed for compatibility with all dependencies and features. Note that Python 3.13 does not work in this project as of October 2024.

Download Python 3.12.5 from the official [Python website](https://www.python.org/downloads/release/python-3125/).

## Recommended IDE

For the best development experience, we recommend using Visual Studio Code (VSCode).

Download VSCode from the official [Visual Studio Code website](https://code.visualstudio.com/).

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/tomycabre/AI-Web-Scrapper.git
cd AI-Web-Scrapper
```

### Step 2: Virtual Environment Setup

#### Windows

```bash
py -m venv ai
```

#### MacOS

```bash
python3 -m venv ai
```

### Step 3: Activate the Virtual Environment

#### Windows

```bash
.\ai\Scripts\activate.bat
```

#### MacOS

```bash
source ai/bin/activate
```

### Step 4: Install Required Packages

#### Windows

```bash
py -m pip install -r requirements.txt
```

#### MacOS

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit Application

#### Windows

```bash
py -m streamlit run main.py
```

#### MacOS

```bash
streamlit run main.py
```

### Step 6: Chromedriver Setup

#### Windows

1. Download Chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).
2. Select "Stable" and download the (`win64` or `win32`) zip file.
3. Extract the zip file and copy `chromedriver.exe` to your AI-WEB-SCRAPPER folder.

#### MacOS

1. Delete the existing `chromedriver.exe` from the project.
2. Download Chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).
3. Select "Stable" and download the appropriate zip file (`mac-arm64` or `mac-x64`).
4. Extract the zip file and copy `chromedriver` to your AI-WEB-SCRAPPER folder.

### Step 7: Install Ollama

1. Download Ollama from [here](https://ollama.com/download).
2. Select your platform (MacOS, Linux, Windows) and complete the installation.

3. Open Command Prompt and type:
   ```bash
   ollama
   ```
4. Download your desired Ollama version (e.g., llama3):

   ```bash
   ollama run llama3
   ```

5. Update the model version in `parse.py` (line 17):

   ```python
   model = OllamaLLM(model="your model version here")
   ```

### Setup Complete

Congratulations! You have successfully set up the AI-Based Real Estate Web Scraper.

## Features

1. Automated Data Extraction: Scrapes real estate listings from multiple websites.
2. AI Integration: Uses machine learning models to enhance data extraction accuracy.
3. Customizable: Easily update the model version and scraping parameters.

## Usage

Instructions on how to use the web scraper will be provided here.

## Contributing

We welcome contributions! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
