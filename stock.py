import yfinance as yf
from datetime import datetime, timedelta

def get_next_working_day(date):
    while date.weekday() >= 5:
        date += timedelta(days=1)
    return date

def get_price_change(ticker, date):
    ticker = ticker.upper().strip()
    stock = yf.Ticker(ticker)

    start = datetime.strptime(date, "%Y-%m-%d")
    start = get_next_working_day(start)
    end = start + timedelta(days=7)

    data = stock.history(start=start, end=end)

    if len(data) >= 2:
        before = data['Close'].iloc[0]
        after = data['Close'].iloc[1]
        change = round(((after - before) / before) * 100, 2)
        return round(before, 2), round(after, 2), change
    return None, None, None