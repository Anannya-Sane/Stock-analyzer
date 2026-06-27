import yfinance as yf
import time

def get_stock_metrics(ticker):
    try:
        ticker = ticker.upper().strip()
        stock = yf.Ticker(ticker)
        time.sleep(1)
        info = stock.info

        if not info or info.get("quoteType") is None:
            return {"Company": "N/A"}

        def safe(key, multiply=False):
            val = info.get(key)
            if val is None or val == 0:
                return "N/A"
            if multiply:
                return round(val * 100, 2)
            try:
                return round(float(val), 2)
            except:
                return val

        return {
            "Company":            info.get("longName") or info.get("shortName", "N/A"),
            "Current Price":      safe("currentPrice") or safe("regularMarketPrice"),
            "52 Week High":       safe("fiftyTwoWeekHigh"),
            "52 Week Low":        safe("fiftyTwoWeekLow"),
            "52 Week Avg":        safe("fiftyTwoWeekLow"),
            "P/E Ratio":          safe("trailingPE"),
            "P/B Ratio":          safe("priceToBook"),
            "EPS":                safe("trailingEps"),
            "ROE (%)":            safe("returnOnEquity", multiply=True),
            "Revenue Growth (%)": safe("revenueGrowth", multiply=True),
            "Profit Margin (%)":  safe("profitMargins", multiply=True),
            "Market Cap":         info.get("marketCap", "N/A"),
            "Dividend Yield (%)": safe("dividendYield", multiply=True),
            "Beta":               safe("beta"),
            "Sector":             info.get("sector", "N/A"),
            "Industry":           info.get("industry", "N/A"),
        }

    except Exception:
        return {"Company": "N/A"}
