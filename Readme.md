# AI Web Scrapper

This project is an AI-based web scraper that extracts data from websites, optimized for real estate.

## Installation Steps

### Step 1

Set up the virtual environment:

On Windows, run:

```bash
py -m venv ai
```

On MacOS, run:

```bash
python3 -m venv ai
```

### Step 2

Activate the virtual environment:

On Windows, run:

```bash
.\ai\Scripts\activate.bat
```

On MacOS, run:

```bash
source ai/bin/activate
```

### Step 3

Install the required packages:

On Windows, run:

```bash
py -m pip install -r requirements.txt
```

On MacOS, run:

```bash
pip install -r requirements.txt
```

### Step 4

Run the streamlit application

On Windows:

```bash
py -m streamlit run main.py
```

On MacOS:

```bash
streamlit run main.py
```

### Step 5

#### If on Windows and chromedriver.exe is not on this project.

##### 5.1

install it here:
https://googlechromelabs.github.io/chrome-for-testing/#stable

##### 5.1.2

First you will select Stable, then search for binary "chromedriver", then you download the zip folder for your Platform (Most windows users will select "win64").

##### 5.1.3

After downloading the zip file: extract it to your desired folder, open the extracted folder, copy the chromedriver.exe file and paste it in you AI-WEB-SCRAPPER folder.

#### If on MacOS.

##### 5.2.1

Delete chromedriver.exe from this project and re-install it here:
https://googlechromelabs.github.io/chrome-for-testing/#stable

##### 5.2.2

Select Stable, then search for binary "chromedriver", then you download the zip folder for your Platform (Most MacOS users will select "mac-arm64", or "mac-x64" for users with an intel based Mac).

##### 5.2.3

After downloading the zip file: extract it to your desired folder, open the extracted folder, copy the chromedriver file and paste it in you AI-WEB-SCRAPPER folder.

### Step 6

Download ollama here (This is required to run the project):
https://ollama.com/download

#### 6.1

Select your platform (MacOS, Linux, Windows) and begin instalation.

#### 6.2

After installation, open CMD and type:

```bash
ollama
```

#### 6.3

Download YOUR desired ollama version, I run llama3 (October 2024).

```bash
ollama run llama3
```

#### 6.4

After downloading ollama, go to parse.py and change the model version to your version.
You should find that in line 17 (October 2024).

```python
model = OllamaLLM(model="add your model version here..")
```

### Congratulations you finished setting up your AI-WEB-SCRAPPER.

## Usage

## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
