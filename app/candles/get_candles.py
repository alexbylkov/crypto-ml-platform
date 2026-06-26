from typing import TypedDict
from datetime import datetime
import httpx

from app.constants.urls import BYBIT_BASE_URL

class Candle(TypedDict):
    time: str
    open: float
    high: float
    low: float
    close: float

def convert_list_candles(list_str_candles: list[str]) -> Candle:
    startTime, openPrice, highPrice, lowPrice, closePrice, *_ = list_str_candles

    return {
        'time': datetime.fromtimestamp(int(startTime) / 1000).strftime("%Y-%m-%d %H:%M:%S"),
        'open': float(openPrice),
        'high': float(highPrice),
        'low': float(lowPrice),
        'close': float(closePrice),
    }

def get_candles(symbol: str, interval: str = "60", limit: int = 5) -> list[Candle]:
    params = { 'category': 'spot', 'symbol': symbol, 'interval': interval, 'limit': limit }
    response = httpx.get(BYBIT_BASE_URL + 'v5/market/kline', params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    list_candles = data["result"]["list"]
    result = [convert_list_candles(x) for x in list_candles]

    return result
