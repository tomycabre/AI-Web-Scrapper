# AI Web Scrapper

# AI-Based Real Estate Web Scraper

Welcome to our AI-based web scraper project, designed to efficiently extract data from real estate websites.

## Installation Guide

### Step 1: Virtual Environment Setup

#### Windows

```bash
py -m venv ai
```

#### MacOS

```bash
python3 -m venv ai
```

### Step 2: Activate the Virtual Environment

#### Windows

```bash
.\ai\Scripts\activate.bat
```

#### MacOS

```bash
source ai/bin/activate
```

### Step 3: Install Required Packages

#### Windows

```bash
py -m pip install -r requirements.txt
```

#### MacOS

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

#### Windows

```bash
py -m streamlit run main.py
```

#### MacOS

```bash
streamlit run main.py
```

### Step 5: Chromedriver Setup

#### Windows

1. Download Chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).
2. Select "Stable" and download the "win64" zip file.
3. Extract the zip file and copy `chromedriver.exe` to your AI-WEB-SCRAPPER folder.

#### MacOS

1. Delete the existing `chromedriver.exe` from the project.
2. Download Chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).
3. Select "Stable" and download the appropriate zip file (`mac-arm64` or `mac-x64`).
4. Extract the zip file and copy `chromedriver` to your AI-WEB-SCRAPPER folder.

### Step 6: Install Ollama

1. Download Ollama from [here](https://ollama.com/download).
2. Select your platform (MacOS, Linux, Windows) and complete the installation.
3. Open CMD and type:
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

Congratulations! You have successfully set up the AI-WEB-SCRAPPER.

## Usage

Instructions on how to use the web scraper will be provided here.

## Contributing

We welcome contributions! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
