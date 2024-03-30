import requests
import matplotlib.pyplot as plt
from datetime import datetime

class StockPortfolio:
    def __init__(self):
        self.stocks = {}
        self.portfolio_values = []

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity}
        # Update portfolio value after adding stock
        self.get_portfolio_value()

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if quantity >= self.stocks[symbol]['quantity']:
                del self.stocks[symbol]
            else:
                self.stocks[symbol]['quantity'] -= quantity
        # Update portfolio value after removing stock
        self.get_portfolio_value()

    def get_portfolio_value(self):
        total_value = 0
        for symbol, data in self.stocks.items():
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                total_value += stock_data['price'] * data['quantity']
        self.portfolio_values.append((datetime.now(), total_value))
        return total_value

    def get_stock_data(self, symbol):
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            try:
                # Ensure 'Global Quote' and '05. price' exist in the response
                price = float(data['Global Quote']['05. price'])
                return {'price': price}
            except KeyError:
                print(f"Could not find price data for {symbol}. Please check the symbol and try again.")
                return None
        else:
            print(f"API request failed with status code {response.status_code}.")
            return None

    def plot_portfolio_values(self):
        if len(self.portfolio_values) < 2:
            print("Insufficient data to plot.")
            return
        dates = [date for date, _ in self.portfolio_values]
        values = [value for _, value in self.portfolio_values]
        plt.plot(dates, values, marker='o', linestyle='-')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value ($)')
        plt.title('Portfolio Value Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracking Tool")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Value")
        print("4. View Portfolio Value Over Time")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            value = portfolio.get_portfolio_value()
            print(f"Portfolio Value: ${value:.2f}")
        elif choice == '4':
            portfolio.plot_portfolio_values()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
