"""Minimal runner for FastAPI app so Hugging Face can start the service via `python app.py`.

It imports the `app` instance from `main.py` and runs Uvicorn.
"""
import os

try:
    # Import the FastAPI app from the project
    from main import app
except Exception as e:
    raise ImportError(f"Failed to import FastAPI app from main.py: {e}")


def run():
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    run()
