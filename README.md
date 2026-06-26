# 📊 Stock Analyzer — AI-Powered Fundamental Analysis

A clean, interactive web app that fetches real-time fundamental 
metrics for any NSE or BSE listed stock and evaluates them 
against ideal financial benchmarks.

## 🌐 Live Demo
👉 [Click here to try the app](https://anannya-sane-stock-analyzer.streamlit.app)

## 🎯 What It Does
- Fetches real-time stock data for any NSE/BSE listed company
- Shows key metrics: P/E, P/B, EPS, ROE, Profit Margin, Revenue Growth
- Color-coded badges (Good / Fair / Expensive) based on ideal benchmarks
- 52 week high, low and average price
- Market cap, dividend yield and beta (risk indicator)

## 📐 Ideal Benchmarks Used
| Metric | Good | Fair | Expensive |
|---|---|---|---|
| P/E Ratio | < 20 | 20–35 | > 35 |
| P/B Ratio | < 3 | 3–5 | > 5 |
| ROE | > 15% | 5–15% | < 5% |
| Profit Margin | > 15% | 5–15% | < 5% |
| Revenue Growth | > 10% | 0–10% | < 0% |
| Beta | < 1 | 1–1.5 | > 1.5 |

## 🛠️ Tech Stack
- Python 3.14
- yfinance (Real-time stock data)
- Streamlit (Web app)

## ▶️ How to Run Locally
pip install yfinance streamlit
streamlit run app.py

## 👩‍💻 Built by Anannya
Second AI project — combining finance knowledge with Python!
