# 🕷️ AI WebScraper & Parser with Ollama LLM

A lightweight, interactive Streamlit application that scrapes any webpage, extracts clean content, and intelligently parses it using a powerful LLM (LLaMA 3.1 via Ollama). Ideal for structured data extraction from messy websites – just enter a URL and a description of what you want.

---

## 🚀 Features

- **Web Scraping with Selenium**
  - Loads the full webpage using a headless Chrome driver.
  - Retrieves only meaningful content by filtering out scripts, styles, and other noise.

- **Clean DOM Extraction**
  - Uses BeautifulSoup to extract, clean, and structure the page content for downstream parsing.

- **Intelligent Parsing via Ollama LLaMA 3.1**
  - Integrates LangChain's `OllamaLLM` to process DOM chunks.
  - Prompts LLM to extract structured data (in CSV format) based on user descriptions.

- **Interactive UI with Streamlit**
  - Clean UI to input URLs and parsing instructions.
  - View DOM content, parsed results, and download as CSV.

---

## 🧠 How It Works

1. Enter the website URL in the Streamlit UI.
2. App uses `selenium` to launch a browser and fetch page content.
3. Extracts `<body>` HTML using BeautifulSoup and cleans it.
4. If DOM content exists, user provides a natural language query (e.g., "extract all product names and prices").
5. DOM content is split into chunks and sent to `LLaMA 3.1` via LangChain's `OllamaLLM`.
6. Structured results are returned in CSV format and available for download.

---
gh
## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **Scraping**: Selenium, BeautifulSoup
- **LLM Integration**: LangChain + Ollama (LLaMA 3.1)
- **Model Used**: `llama3.1`

---

## 📂 Project Structure

```bash
├── main.py          # Streamlit app – handles UI, scraping trigger, and parsing workflow
├── scrape.py        # Handles webpage scraping, content extraction, and cleanup
├── parse.py         # Sends cleaned DOM chunks to LLM and formats parsed result
```

---

## 📦 Installation & Setup

```bash
# Clone this repo
git clone https://github.com/Kasib03/AI-Webscrapper.git
cd AI-Webscrapper

# Install dependencies
pip install -r requirements.txt
```

> Make sure you have `chromedriver` installed and accessible in your system path. You may need to modify the path in `scrape.py` accordingly.

---

## 🖥️ Running the App

```bash
streamlit run main.py
```

---

## 🧠 Example Use Case

Let’s say you want to extract all blog post titles and publish dates from a tech blog:

1. Enter the blog URL.
2. In the parser text area:  
   `Extract all blog titles and their published dates from the page.`
3. Click **Parse Content**.
4. Download the resulting CSV.

---






## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)

---


