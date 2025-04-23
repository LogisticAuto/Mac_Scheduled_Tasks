import yfinance as yf
from datetime import datetime, timedelta
import smtplib

def check_stock(symbol, threshold=-9):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="3d")
    now = datetime.now().strftime("%m/%d/%Y %H:%M")
    
    if len(hist) >= 2:
        start_price = hist['Close'].iloc[0]
        end_price = hist['Close'].iloc[-1]
        percent_change = ((end_price - start_price) / start_price) * 100
        
        if percent_change <= threshold:
            return f" {symbol} has dropped {abs(percent_change):.2f}%, from: ${start_price:.2f} to: ${end_price:.2f} in the last 3 days. Alerted {now}"
    return None

def send_email(message, to_email):
    from_email = "LogisticAutoImprovements@gmail.com"
    password = "abcp nqvv rpwz nnjd"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, f"Subject: Stock Alert!\n\n{message}")

# 🧾 Ticker symbols you want to monitor
tickers = ['AI', 'AIQ', 'AMBA', 'AMD', 'AMZN', 'ANET', 'APLD', 'AQWA', 'ASAN', 'BAESY', 'BHP', 'BITS', 'BOTZ', 'BUG', 'CCCS', 'CCJ', 'CCLD', 'CEG', 'CLOU', 'COIN', 'CPRX', 'CRM', 'CRWD', 'CVX', 'D', 'DGRO', 'DHS', 'DIV', 'DJT', 'DNN', 'DRIV', 'ERJ', 'ET', 'EVEX', 'EXE', 'F', 'FANG', 'GAP', 'GM', 'GNOM', 'GOOG', 'HERO', 'JPM', 'LEN', 'LIT', 'MTDR', 'MUR', 'NGS', 'NOC', 'NOG', 'NU', 'NVDA', 'NX', 'NXE', 'ORCL', 'OSCR', 'PACB', 'PBA', 'QCOM', 'RAYS', 'SCHW', 'SM', 'SNSR', 'SOCL', 'T', 'TOL', 'TSLA', 'UEC', 'URA', 'XOM']

# 🔍 Check each one and collect alerts
alerts = []
for ticker in tickers:
    try:
        result = check_stock(ticker)
        if result:
            alerts.append(result)
    except Exception as e:
        print(f"Error processing {ticker}: {e}")

# 📬 Send one combined message if any stock triggered an alert
if alerts:
    full_message = "\n".join(alerts)
    print("Sending the following alert:\n", full_message)
    send_email(full_message, "9545345585@txt.att.net")  # SMS via email