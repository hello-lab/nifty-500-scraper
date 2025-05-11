
# 📊 Stock Market Analysis Bot 🐍

A Python-based stock market analysis script that uses **Yahoo Finance data (via `yfinance`)** to fetch and analyze stock performance metrics including **RSI (Hourly, Daily, Monthly)**, **P/E**, **P/B**, **PEG Ratio**, **Beta**, **Debt-to-Equity**, **52-Week High/Low**, current price, discount percentage, and technical trend detection using moving averages.  

The results are compiled and exported into an Excel file for easy review 📊📈.

---

## 📌 Features  

- ✅ Fetches historical stock price data (1y, 1mo, 10y)
- ✅ Calculates **Relative Strength Index (RSI)** on multiple timeframes
- ✅ Computes financial ratios: **P/E**, **P/B**, **PEG**, **Beta**, **Debt/Equity**
- ✅ Detects stock trend direction (Uptrend, Downtrend, Consolidation) using **20 & 50 period moving averages**
- ✅ Calculates **Earnings Growth Rate**
- ✅ Exports results to **Excel (.xlsx)**
- ✅ Supports batch processing of multiple tickers

---

## 🛠️ Tech Stack  

- 🐍 Python 3.x  
- 📦 `yfinance`  
- 📦 `pandas`  
- 📦 `openpyxl` (for Excel export)

---

## 📂 Project Structure  

```

stock-analysis-bot/
├── bot.py                  # Main script
├── sharemaket.xlsx         # Output file with results
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

````

---

## 🚀 Getting Started  

### 1️⃣ Clone the repository  

```bash
git clone https://github.com/hello-lab/nifty-500-scraper.git
cd nifty-500-scrape
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*Or manually install:*

```bash
pip install yfinance pandas openpyxl
```

### 3️⃣ Add your tickers

* Add your tickers in the `ticker100` string, separated by spaces.
* Add corresponding names in `name100` list.

Example:

```python
ticker100 = "RELIANCE INFY TCS"
name100 = ["Reliance", "Infosys", "TCS"]
```

### 4️⃣ Run the script

```bash
python bot.py
```

---

## 📄 Output

An Excel file `sharemaket.xlsx` will be generated containing:

| Name     | 52-Week High | 52-Week Low | CMP | Discount % | RSI (Hourly) | RSI (Daily) | RSI (Monthly) | P/E | P/B | PEG | Beta | Debt to Equity | Trend |
| -------- | ------------ | ----------- | --- | ---------- | ------------ | ----------- | ------------- | --- | --- | --- | ---- | -------------- | ----- |
| Reliance | ...          | ...         | ... | ...        | ...          | ...         | ...           | ... | ... | ... | ...  | ...            | ...   |

---

## ⚠️ Disclaimer

This project is for **educational and personal research purposes only**.
It fetches data via Yahoo Finance’s public API through `yfinance`.
Do not use this tool for actual trading decisions without professional financial advice.


