import os

STUDENT_EMAIL = os.environ.get("STUDENT_EMAIL", "default_email@example.com")

STUDENT_SECRET = os.environ.get("STUDENT_SECRET", "default_secret")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")