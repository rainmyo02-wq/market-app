import flet as ft
from flet import app
import requests

def get_market_data(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        data = response.json()
        meta = data['chart']['result'][0]['meta']
        price = meta['regularMarketPrice']
        currency = meta['currency']
        return f"{price} {currency}"
    except Exception as e:
        return "Error fetching data"

def main(page: ft.Page):
    page.title = "Global Market Dashboard"
    
    btc_price = get_market_data("BTC-USD")
    
    page.add(
        ft.Text("Market Dashboard", size=30, weight="bold"),
        ft.Text(f"Bitcoin Price: {btc_price}", size=20)
    )

if __name__ == "__main__":
    app(target=main)
