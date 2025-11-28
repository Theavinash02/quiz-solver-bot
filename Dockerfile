FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system packages, Chrome, chromedriver, ffmpeg, Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       wget curl gnupg ca-certificates unzip build-essential \
       python3 python3-pip python3-venv \
       ffmpeg fonts-liberation libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-6 libxss1 libasound2 libxrandr2 \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# DON'T install ChromeDriver in Dockerfile - let webdriver-manager handle it at runtime
# Chrome v115+ uses new distribution method that doesn't work with old storage API
# The webdriver-manager in main.py will download the correct version on first run
RUN echo "Skipping Chromedriver installation - will be handled by webdriver-manager at runtime" \
    && echo "Installed Chrome version: $(google-chrome --product-version)" \
    && rm -f /usr/local/bin/chromedriver /usr/bin/chromedriver || true \
    && echo "Removed any stale chromedrivers from system PATH"

# App setup
WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

ENV PORT=7860
EXPOSE 7860

CMD ["python3", "app.py"]
