# LLM Analysis Quiz Solver

This project implements an automated system to solve the "LLM Analysis Quiz". It features a **FastAPI** endpoint that triggers a background agent using **Playwright** (for browser automation) and **OpenAI** (for reasoning and logic extraction).

The system is designed to be "Always On" via Docker deployment on Hugging Face Spaces.

## 📂 Project Structure

- `main.py`: FastAPI entry point & background task manager.
- `quiz_solver.py`: Core logic (Browser automation & LLM integration).
- `config.py`: Environment variable & secret management.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Deployment configuration for Hugging Face.

## 🚀 Features

* **Asynchronous Architecture:** Uses FastAPI `BackgroundTasks` to handle long-running quiz chains without timing out the initial HTTP request.
* **Headless Browsing:** Uses **Playwright** to render JavaScript-heavy pages and extract hidden content (e.g., `atob` decoding).
* **AI-Powered:** Integrates **OpenAI** to parse complex natural language questions and decide on the correct answer format.
* **Secure:** Uses environment variables for all secrets; no hardcoded keys.

## 🛠️ Setup & Installation

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```

3.  **Configure Secrets:**
    Set the following environment variables (or update `config.py` for local testing):
    * `STUDENT_EMAIL`: Your registered email.
    * `STUDENT_SECRET`: Your registered secret string.
    * `OPENAI_API_KEY`: Your OpenAI API Key.

4.  **Run Locally:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## 🧪 Testing

You can test the endpoint using `curl`:

```bash
curl -X POST "[http://127.0.0.1:8000/solve-quiz](http://127.0.0.1:8000/solve-quiz)" \
     -H "Content-Type: application/json" \
     -d '{
           "email": "your_email@example.com",
           "secret": "your_secret",
           "url": "[https://tds-llm-analysis.s-anand.net/demo](https://tds-llm-analysis.s-anand.net/demo)"
         }'