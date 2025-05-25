# 🧬 AI-Powered Medical Report Assistant

An intelligent Streamlit web app that extracts, analyzes, and explains medical lab reports using OCR, NLP, and OpenAI's GPT model.

## 📌 Features

✅ Extracts text from scanned lab reports (PDFs, Images)  
✅ Uses OCR (Tesseract) to convert reports into text  
✅ Parses and identifies lab test results (name, value, range)  
✅ Uses OpenAI's GPT model to explain each result in simple terms  
✅ Detects abnormal values and suggests possible follow-up actions  

## 🧠 Technologies Used

- Python 🐍
- Streamlit 🌐 (Frontend UI)
- Tesseract OCR 🔍
- OpenAI GPT (ChatGPT API) 🤖
- Regular Expressions (NLP parsing)
- pdf2image / PIL / OpenCV (PDF/Image processing)
- dotenv (.env config)


## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medical-ai-assistant.git
cd medical-ai-assistant
