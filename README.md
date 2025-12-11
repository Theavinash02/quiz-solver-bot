---
title: LLM Analysis Quiz Bot
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
app_port: 7860
---

# LLM Analysis Quiz Bot 🤖

An autonomous agent designed to solve multi-step data science quizzes. This application leverages **Large Language Models (Gemini)**, **LangGraph**, and a suite of specialized tools to scrape web pages, analyze data, transcribe audio, and execute code dynamically.

## 🚀 Overview

This project was developed for the **TDS (Tools in Data Science)** course. The objective is to build an agent that can autonomously navigate a sequence of tasks provided via a web interface. The agent receives a starting URL, identifies the task, performs the necessary operations (coding, analysis, transformation), and submits the answer to proceed to the next stage.

### Key Capabilities
* **🌐 Web Scraping:** Uses **Playwright** to render JavaScript-heavy pages and extract dynamic content.
* **🎧 Audio Processing:** Automates the downloading and transcription of audio files (MP3) using **FFmpeg**, `pydub`, and `SpeechRecognition`.
* **📊 Data Analysis:** Analyzing CSV/JSON data using **Pandas** (filtering, sorting, aggregation).
* **💻 Code Execution:** Writes and executes Python code in a sandboxed environment (`uv` managed) to solve complex logic puzzles.
* **🛠️ Tool Integration:** Handles Git operations, SQL queries, image analysis, and embedding calculations.

## 🏗️ Architecture

The application is built using a micro-agent architecture:

1.  **FastAPI Server:** Exposes a REST endpoint (`/quiz`) to accept task requests.
2.  **LangGraph Agent:** Manages the decision-making loop (Plan → Act → Observe).
3.  **Tool Belt:**
    * `run_code`: Executes Python scripts.
    * `web_scraper`: Renders HTML using a headless browser.
    * `download_file`: Fetches remote assets.
    * `speech_recognition`: Transcribes audio passphrases.
4.  **Docker Environment:** Ensures all system dependencies (like **FFmpeg**) are available for deployment.

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Framework:** FastAPI, Uvicorn
* **LLM Orchestration:** LangChain, LangGraph
* **Model Provider:** Google Gemini (`gemini-1.5-flash` / `gemini-2.5-pro`)
* **Browser Automation:** Playwright
* **Audio Engine:** FFmpeg, Pydub
* **Dependency Management:** `uv`

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.12+
* Google Gemini API Key
* FFmpeg (for audio tasks)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/quiz-solver-bot.git](https://github.com/your-username/quiz-solver-bot.git)
cd quiz-solver-bot

### 2. Install Dependencies
This project uses **uv** for fast and efficient dependency management.

```bash
# Install uv
pip install uv

# Sync dependencies from pyproject.toml
uv sync