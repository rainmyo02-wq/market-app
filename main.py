import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


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


class ShopZoneApp(App):

    def build(self):
        self.title = "Global Market Dashboard"

        layout = BoxLayout(
            orientation='vertical', padding=20, spacing=20
        )

        title_label = Label(
            text="Market Dashboard",
            font_size='30sp',
            bold=True,
            size_hint=(1, 0.3),
        )

        btc_price = get_market_data("BTC-USD")
        price_label = Label(
            text=f"Bitcoin Price: {btc_price}",
            font_size='20sp',
            size_hint=(1, 0.7),
        )

        layout.add_widget(title_label)
        layout.add_widget(price_label)

        return layout


if __name__ == '__main__':
    ShopZoneApp().run()
