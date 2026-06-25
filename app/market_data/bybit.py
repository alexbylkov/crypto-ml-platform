import httpx

BYBIT_BASE_URL = 'https://api.bybit.com/'

def get_price(symbol: str) -> float:
    params = { 'category': 'spot', 'symbol': symbol }
    response = httpx.get(BYBIT_BASE_URL + 'v5/market/tickers', params=params, timeout=10)
    response.raise_for_status()


    data = response.json()
    last_price = data["result"]["list"][0]["lastPrice"]

    return float(last_price)