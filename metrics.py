import yfinance as yf
import time

def get_stock_metrics(ticker):
    try:
        ticker = ticker.upper().strip()
        stock = yf.Ticker(ticker)
        
        # Add delay to avoid rate limiting
        time.sleep(2)
        info = stock.fast_info
        full_info = stock.info

        metrics = {
            "Company": full_info.get("longName", "N/A"),
            "Current Price": round(info.last_price, 2) if hasattr(info, 'last_price') and info.last_price else full_info.get("currentPrice", "N/A"),
            "52 Week High": round(info.fifty_two_week_high, 2) if hasattr(info, 'fifty_two_week_high') and info.fifty_two_week_high else full_info.get("fiftyTwoWeekHigh", "N/A"),
            "52 Week Low": round(info.fifty_two_week_low, 2) if hasattr(info, 'fifty_two_week_low') and info.fifty_two_week_low else full_info.get("fiftyTwoWeekLow", "N/A"),
            "52 Week Avg": round(info.fifty_day_average, 2) if hasattr(info, 'fifty_day_average') and info.fifty_day_average else full_info.get("fiftyDayAverage", "N/A"),
            "P/E Ratio": round(full_info.get("trailingPE", 0), 2) if full_info.get("trailingPE") else "N/A",
            "P/B Ratio": round(full_info.get("priceToBook", 0), 2) if full_info.get("priceToBook") else "N/A",
            "EPS": round(full_info.get("trailingEps", 0), 2) if full_info.get("trailingEps") else "N/A",
            "ROE (%)": round(full_info.get("returnOnEquity", 0) * 100, 2) if full_info.get("returnOnEquity") else "N/A",
            "Revenue Growth (%)": round(full_info.get("revenueGrowth", 0) * 100, 2) if full_info.get("revenueGrowth") else "N/A",
            "Profit Margin (%)": round(full_info.get("profitMargins", 0) * 100, 2) if full_info.get("profitMargins") else "N/A",
            "Market Cap": full_info.get("marketCap", "N/A"),
            "Dividend Yield (%)": round(full_info.get("dividendYield", 0) * 100, 2) if full_info.get("dividendYield") else "N/A",
            "Beta": round(full_info.get("beta", 0), 2) if full_info.get("beta") else "N/A",
            "Sector": full_info.get("sector", "N/A"),
            "Industry": full_info.get("industry", "N/A"),
        }
        return metrics

    except Exception as e:
        return {
            "Company": "N/A", "Current Price": "N/A",
            "52 Week High": "N/A", "52 Week Low": "N/A", "52 Week Avg": "N/A",
            "P/E Ratio": "N/A", "P/B Ratio": "N/A", "EPS": "N/A",
            "ROE (%)": "N/A", "Revenue Growth (%)": "N/A", "Profit Margin (%)": "N/A",
            "Market Cap": "N/A", "Dividend Yield (%)": "N/A", "Beta": "N/A",
            "Sector": "N/A", "Industry": "N/A",
        }
