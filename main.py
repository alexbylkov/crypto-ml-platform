import sys
from app.market_data.get_market_data import get_price
from app.candles.get_candles import get_candles

def main():

    actions = {
        'price': get_price,
        'candles': get_candles,
    } 

    if len(sys.argv) != 3 or sys.argv[1] not in ('price', 'candles'):
        print("Using: uv run main.py <'price' | 'candles'> <symbol>")
        sys.exit(1) 

    _, action, symbol = sys.argv
    response = actions.get(action)(symbol)
    
    print(symbol, response)

if __name__ == "__main__":
    main()
