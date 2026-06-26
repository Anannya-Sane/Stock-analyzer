import yfinance as yf

def get_stock_metrics(ticker):
    stock = yf.Ticker(ticker.upper().strip())
    info = stock.info

    metrics = {
        "Company": info.get("longName", "N/A"),
        "Current Price": info.get("currentPrice", "N/A"),
        "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
        "52 Week Avg": info.get("fiftyDayAverage", "N/A"),
        "P/E Ratio": info.get("trailingPE", "N/A"),
        "P/B Ratio": info.get("priceToBook", "N/A"),
        "EPS": info.get("trailingEps", "N/A"),
        "ROE (%)": round(info.get("returnOnEquity", 0) * 100, 2) if info.get("returnOnEquity") else "N/A",
        "Revenue Growth (%)": round(info.get("revenueGrowth", 0) * 100, 2) if info.get("revenueGrowth") else "N/A",
        "Profit Margin (%)": round(info.get("profitMargins", 0) * 100, 2) if info.get("profitMargins") else "N/A",
        "Market Cap": info.get("marketCap", "N/A"),
        "Dividend Yield (%)": round(info.get("dividendYield", 0) * 100, 2) if info.get("dividendYield") else "N/A",
        "Beta": info.get("beta", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
    }
    return metrics