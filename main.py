import flet as ft
import requests
import yfinance as yf


def main(page: ft.Page):
  page.title = "Global Market Dashboard"
  page.theme_mode = ft.ThemeMode.DARK
  page.scroll = ft.ScrollMode.AUTO
  page.padding = 15

  def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,solana&vs_currencies=usd&include_24hr_change=true"
    try:
      return requests.get(url, timeout=5).json()
    except:
      return None

  def get_market_price(ticker_symbol):
    try:
      t = yf.Ticker(ticker_symbol)
      hist = t.history(period="2d")
      if len(hist) >= 2:
        curr = hist["Close"].iloc[-1]
        prev = hist["Close"].iloc[-2]
        change = ((curr - prev) / prev) * 100
        return curr, change
    except:
      pass
    return None, None

  def create_card(title, value, change_pct, symbol="$"):
    if value is None:
      val_text = "Error"
      change_text = "N/A"
      color = ft.Colors.GREY
    else:
      val_text = f"{symbol}{value:,.2f}" if symbol == "$" else f"{value:.4f}"
      color = ft.Colors.GREEN if change_pct >= 0 else ft.Colors.RED
      change_text = f"{change_pct:+.2f}%"

    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        title,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE_70,
                    ),
                    ft.Text(val_text, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        change_text,
                        size=13,
                        color=color,
                        weight=ft.FontWeight.W_500,
                    ),
                ],
                spacing=5,
            ),
            padding=15,
            width=165,
        )
    )

  crypto_row = ft.Row(wrap=True, spacing=10)
  gold_row = ft.Row(wrap=True, spacing=10)
  forex_row = ft.Row(wrap=True, spacing=10)
  loading_indicator = ft.ProgressBar(visible=False)

  def load_data(e=None):
    loading_indicator.visible = True
    page.update()

    # 1. Crypto
    crypto_row.controls.clear()
    c_data = get_crypto_data()
    if c_data:
      crypto_row.controls.append(
          create_card(
              "Bitcoin (BTC)",
              c_data["bitcoin"]["usd"],
              c_data["bitcoin"]["usd_24h_change"],
          )
      )
      crypto_row.controls.append(
          create_card(
              "Ethereum (ETH)",
              c_data["ethereum"]["usd"],
              c_data["ethereum"]["usd_24h_change"],
          )
      )
      crypto_row.controls.append(
          create_card(
              "Solana (SOL)",
              c_data["solana"]["usd"],
              c_data["solana"]["usd_24h_change"],
          )
      )
      crypto_row.controls.append(
          create_card(
              "BNB",
              c_data["binancecoin"]["usd"],
              c_data["binancecoin"]["usd_24h_change"],
          )
      )

    # 2. Gold
    gold_row.controls.clear()
    g_val, g_chg = get_market_price("GC=F")
    gold_row.controls.append(create_card("World Gold (1 Oz)", g_val, g_chg))

    # 3. Forex
    forex_row.controls.clear()
    currencies = {
        "EUR/USD": "EURUSD=X",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "JPY=X",
        "USD/THB": "THB=X",
    }
    for name, ticker in currencies.items():
      val, chg = get_market_price(ticker)
      forex_row.controls.append(create_card(name, val, chg, symbol=""))

    loading_indicator.visible = False
    page.update()

  page.add(
      ft.AppBar(
          title=ft.Text("Global Market Dashboard"),
          actions=[ft.IconButton(ft.Icons.REFRESH, on_click=load_data)],
          bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
      ),
      loading_indicator,
      ft.Text("🪙 Cryptocurrency", size=18, weight=ft.FontWeight.BOLD),
      crypto_row,
      ft.Divider(),
      ft.Text("🥇 Commodities", size=18, weight=ft.FontWeight.BOLD),
      gold_row,
      ft.Divider(),
      ft.Text("🔀 Forex Exchange", size=18, weight=ft.FontWeight.BOLD),
      forex_row,
  )

  load_data()


ft.run(main)