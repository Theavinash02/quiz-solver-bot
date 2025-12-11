# LLM Analysis Quiz Bot 🤖

## Overview

This project was developed for the **TDS (Tools in Data Science)** course project. The objective is to build an autonomous application capable of solving multi-step quiz tasks that involve:

-   **Data Sourcing:** Scraping websites, calling APIs, and downloading files.
-   **Data Preparation:** Cleaning text, parsing PDFs, and handling various data formats.
-   **Data Analysis:** Filtering, aggregating, performing statistical analysis, and running ML models.
-   **Data Visualization:** Generating charts, narratives, and presentations.

The system acts as an agent: it receives a quiz URL via a REST API, navigates through multiple dynamic quiz pages, solves each task using LLM-powered reasoning (Google Gemini) and specialized tools (Python code execution, SQL, Git, Audio transcription), and submits answers back to the evaluation server.

---

## Installation & Setup

### 1. Prerequisites
* Python 3.12+
* Google Gemini API Key
* FFmpeg (required for audio processing tasks)

### 2. Install Dependencies
This project uses **uv** for fast and efficient dependency management.

```bash
# Install uv
pip install uv

# Sync dependencies from pyproject.toml
uv sync
```

Alternatively, using standard pip:
```
# Install dependencies
pip install .

# Install Playwright browsers (required for web scraping)
playwright install --with-deps chromium
```
### 3. Environment Configuration
Create a .env file in the root directory with your credentials:
```
GOOGLE_API_KEY=your_gemini_api_key_here
EMAIL=your_email@example.com
SECRET=your_project_secret
```
## Docker Deployment
The project is designed to run in a containerized environment, making it ideal for deployment on platforms like Hugging Face Spaces or Render.

**Build the image:**
```
docker build -t quiz-bot .
```
**Run the container:**
```
docker run -p 7860:7860 --env-file .env quiz-bot
```
## API Usage
The application exposes a single endpoint to initiate the quiz solver agent.
- Endpoint: POST /quiz
- Content-Type: application/json

**Payload Format**
```
{
  "email": "your_email@example.com",
  "secret": "your_secret",
  "url": "[https://target-quiz-url.com/start](https://target-quiz-url.com/start)"
}
```
**Example Request (cURL)**
```
curl -v -X POST "http://localhost:7860/quiz" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","secret":"xyz","url":"[https://tds-llm-analysis.s-anand.net/demo](https://tds-llm-analysis.s-anand.net/demo)"}'
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

**Note:** This bot is designed for educational purposes to demonstrate the capabilities of LLM agents in automating complex data science workflows.


