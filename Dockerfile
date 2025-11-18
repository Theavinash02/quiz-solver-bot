# Dockerfile

# 1. Base image with Python + Playwright Browsers installed
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 2. Set up a user named 'user' (ID 1000)
# Hugging Face Spaces does not allow running as root
RUN useradd -m -u 1000 user

# 3. Set working directory
WORKDIR /app

# 4. Fix permissions so 'user' can access the folder
RUN chown user:user /app

# 5. Switch to 'user'
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 6. Copy requirements and install
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 7. Copy the application code
COPY --chown=user . .

# 8. Expose Hugging Face's default port
EXPOSE 7860

# 9. Run the API on port 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]