AI Passport KYC Verification System

An end-to-end AI powered passport verification pipeline that extracts structured identity data from a passport image using Computer Vision + OCR + LLM reasoning.

This project simulates how real fintech / onboarding / banking KYC systems automatically read government documents.

✨ Features

Detects passport layout regions using YOLOv8

Automatically crops:

Photo

Signature

MRZ zone

Smart region reconstruction (no heavy labeling needed)

OCR text extraction using EasyOCR

AI structured data extraction using LLM

Pipeline Architecture

Upload Passport
      ↓
YOLO Layout Detection
(photo + mrz + signature)
      ↓
Geometry Region Builder
(text area + number area)
      ↓
OCR (EasyOCR)
      ↓
LLM Parsing (Groq / Llama)
      ↓
Structured JSON Output
Output Example
{
  "passport_number": "575034801",
  "surname": "FRANKLIN",
  "given_names": "BENJAMIN",
  "nationality": "UNITED STATES OF AMERICA",
  "date_of_birth": "17 Jan 1706",
  "sex": "M",
  "expiry_date": "15 Jan 2028"
}
Steps To Install:

1.git clone <repo>
cd passport_ai

py -3.12 -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

2.Add .env:

GROQ_API_KEY=your_key_here

3.Run:

python app.py

4.Open:

http://127.0.0.1:5000
