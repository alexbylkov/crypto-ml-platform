import httpx

from constants.urls import BYBIT_BASE_URL

def get_price(symbol: str) -> float:
    try:
        params = { 'category': 'spot', 'symbol': symbol }
        response = httpx.get(BYBIT_BASE_URL + 'v5/market/tickers', params=params)
        last_price = response.json()['result']['list'][0]['lastPrice']

        return last_price
    except:
        return None