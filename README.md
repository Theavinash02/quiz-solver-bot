# TDS LLM Quiz Solver 🤖

An intelligent quiz-solving API that uses LLM reasoning, web scraping, audio transcription, and data analysis to automatically solve complex multi-stage quizzes for the TDS LLM Analysis project.

## 🎯 Project Overview

This project provides a FastAPI-based web service that can:
- Solve multi-stage quiz chains with intelligent state management
- Transcribe and analyze audio files using OpenAI Whisper
- Process CSV data and perform statistical analysis
- Solve cryptographic puzzles (SHA1/SHA256/SHA512/MD5)
- Execute JavaScript and scrape dynamic web content
- Handle alphametic puzzles (cryptarithmetic equations)
- Use GPT-4 as a fallback for complex reasoning

## 🚀 Features

- **Multi-Stage Quiz Support**: Maintains state between connected quiz stages
- **Audio Transcription**: OpenAI Whisper (tiny model) for audio puzzle solving
- **Data Analysis**: Pandas/NumPy for CSV processing and statistical operations
- **Cryptographic Puzzles**: Dynamic hash algorithm detection and computation
- **Alphametic Solver**: Constraint-based solving for cryptarithmetic puzzles
- **JavaScript Rendering**: Selenium + Chrome for dynamic page scraping
- **LLM Fallback**: GPT-4 integration when rule-based methods fail
- **Dynamic Parameter Extraction**: No hardcoded values - adapts to quiz variations

## 📋 Requirements

- Python 3.10+
- Google Chrome (for Selenium)
- FFmpeg (for audio processing)
- OpenAI API Key (for LLM fallback)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/tds-quiz-solver.git
cd tds-quiz-solver
```

### 2. Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y google-chrome-stable chromium-chromedriver ffmpeg
```

**macOS:**
```bash
brew install --cask google-chrome
brew install chromedriver ffmpeg
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

```bash
export OPENAI_API_KEY="your-openai-api-key"
export PORT=7860  # Optional, defaults to 7860
```

Or create a `.env` file:
```env
OPENAI_API_KEY=your-openai-api-key
PORT=7860
```

## 🏃 Running Locally

```bash
python app.py
```

The API will be available at `http://localhost:7860`

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t tds-quiz-solver .
```

### Run Container

```bash
docker run -p 7860:7860 \
  -e OPENAI_API_KEY=your-key \
  tds-quiz-solver
```

## 📡 API Usage

### Endpoint

```
POST /quiz
```

### Request Body

```json
{
  "email": "25ds3000131@ds.study.iitm.ac.in",
  "secret": "your-secret-key",
  "url": "https://tds-llm-analysis.s-anand.net/demo"
}
```

### Response

```json
{
  "answer": "42",
  "explanation": "Solved using numeric extraction from question text"
}
```

### Example cURL Request

```bash
curl -X POST 'http://localhost:7860/quiz' \
  -H 'Content-Type: application/json' \
  -d '{
    "email": "e25ds3000131@ds.study.iitm.ac.in",
    "secret": "####",
    "url": "https://tds-llm-analysis.s-anand.net/demo1"
  }'
```

## 🧩 Supported Quiz Types

| Quiz Type | Description | Example |
|-----------|-------------|---------|
| **Numeric** | Extracts numbers from question text | Finding threshold values |
| **Checksum** | Computes hash with dynamic salt/blob | SHA256 with blob extraction |
| **Alphameric** | Solves cryptarithmetic equations | SEND + MORE = MONEY |
| **Audio+CSV** | Transcribes audio, filters CSV data | Cutoff-based filtering |
| **Scraping** | Extracts secret codes from pages | Hidden text in HTML |
| **JavaScript** | Executes embedded JS to find answers | Dynamic computation |
| **Image Analysis** | Analyzes charts/visualizations | Future support |

## 🔄 Quiz Processing Pipeline

```
1. Fetch Page (Selenium + Chrome)
   ↓
2. Detect Email Requirement
   ↓
3. Preprocessing Stages:
   - JavaScript execution
   - Alphameric puzzle solving
   - Checksum computation
   - Numeric extraction
   - Secret code scraping
   ↓
4. Specialized Handlers:
   - Audio transcription
   - CSV filtering
   - Image analysis
   ↓
5. LLM Fallback (GPT-4)
```

## 🧪 Testing

### Test Individual Quiz Types

```bash
# Audio + CSV puzzle chain
curl -X POST 'http://localhost:7860/quiz' \
  -H 'Content-Type: application/json' \
  -d '{"email":"e25ds3000131@ds.study.iitm.ac.in","secret":"Cute>3","url":"https://tds-llm-analysis.s-anand.net/demo"}'
# Checksum puzzle chain
curl -X POST 'http://localhost:7860/quiz' \
  -H 'Content-Type: application/json' \
  -d '{"email":"e25ds3000131@ds.study.iitm.ac.in","secret":"Cute>3","url":"https://tds-llm-analysis.s-anand.net/demo2"}'
```

### Run Test Suite (Optional)

```bash
# Note: Test files are for development only
python test_checksum_fix.py
python test_dynamic_extraction.py
```

## 📦 Project Structure

```
tds-quiz-solver/
├── main.py                 # Core quiz solver logic (1834 lines)
├── app.py                  # FastAPI entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── README.md              # This file
├── test_*.py              # Test files (optional)
└── docs/                  # Additional documentation
    ├── CHECKSUM_FIX_SUMMARY.md
    └── DYNAMIC_EXTRACTION.md
```

## ⚙️ Configuration

### Dynamic Parameter Extraction

All quiz-specific parameters are extracted dynamically:
- **Multipliers, Offsets, Modulos**: For email-based key calculation
- **Hash Algorithms**: Auto-detects SHA1/SHA256/SHA512/MD5
- **Blob/Salt Patterns**: 5 flexible regex patterns for checksum puzzles
- **Cutoff Thresholds**: With intelligent fallback for audio+CSV puzzles

### State Management

Multi-stage quizzes use `previous_answer` parameter to pass keys between stages:
```python
demo2 → (key: 89252688) → demo2-checksum → (answer: c61387a1fab6)
```

## 🚢 Deployment Options

### Option 1: Hugging Face Spaces (Recommended)

1. Create new Space at https://huggingface.co/spaces
2. Select **Docker** SDK
3. Upload: `main.py`, `app.py`, `requirements.txt`, `Dockerfile`, `README.md`
4. Add `OPENAI_API_KEY` in Space Settings → Repository secrets
5. Space auto-builds and deploys

**Live Demo**: https://berestly-quiz.hf.space/quiz

### Option 2: Render.com

1. Create new Web Service
2. Connect your GitHub repository
3. Set build command: `docker build`
4. Add environment variable: `OPENAI_API_KEY`
5. Deploy

### Option 3: Railway / Fly.io / DigitalOcean

Similar Docker-based deployment process. Ensure you have:
- Docker runtime support
- Sufficient memory (2GB+ recommended for Whisper)
- Environment variable configuration

## ⚠️ Known Limitations

- **Sequential Quiz Chains**: Direct jumps to later stages may fail (server expects sequential access with session IDs)
- **Whisper Model**: Uses `tiny` model (faster but less accurate than larger models)
- **Chrome Startup**: Adds ~2-3s latency per request
- **OpenAI Dependency**: LLM fallback requires valid API key

## 🛡️ Security Notes

- Never commit your `.env` file or expose API keys
- Use environment variables or secrets management for production
- API has no built-in authentication (add if deploying publicly)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 👨‍💻 Author

Built for the TDS LLM Analysis project

## 🙏 Acknowledgments

- OpenAI Whisper for audio transcription
- Selenium WebDriver for JavaScript rendering
- FastAPI for high-performance API framework
- TDS course staff for the quiz challenges

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Contact: [Your contact info]

---

**Note**: This project is educational and designed for the TDS LLM Analysis course. Ensure you comply with the course's academic integrity policies when using this tool.
