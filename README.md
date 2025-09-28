# Athlete Dashboard App

Minimalistic, multilingual athlete dashboard built with Streamlit and Docker.

## Features
- Multi-language support (English, Malayalam, Tamil, Telugu, Hindi, Kannada)
- Athlete profile display
- Sport-specific performance tracking
- Video recording and uploading
- Motivation test
- Dark/Light theme toggle

## How to Run
1. Build Docker image:
   docker build -t athlete-dashboard .

2. Run Docker container:
   docker run -p 8501:8501 athlete-dashboard

3. Open browser at http://localhost:8501
