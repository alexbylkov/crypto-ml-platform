import sys
from app.market_data.bybit import get_price

def main():
    if len(sys.argv) != 2:
        print("Использование: uv run main.py <symbol>")
        sys.exit(1) 

    symbol = sys.argv[1]
    price = get_price(symbol)
    
    print(f'{symbol}: {price}')


if __name__ == "__main__":
    main()
