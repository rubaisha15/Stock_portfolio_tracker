# Stock Portfolio Tracker

A simple Python application to track and visualize the value of a stock portfolio over time. Users can add and remove stocks, view the current total value of their portfolio, and plot the portfolio value's changes over time.

## Features

- **Add Stocks**: Add stocks to your portfolio with their symbol and the quantity you own.
- **Remove Stocks**: Remove stocks from your portfolio by specifying the symbol and quantity to remove.
- **View Portfolio Value**: View the current total value of all stocks in your portfolio.
- **Plot Value Over Time**: Visualize how the total value of your portfolio has changed over time with a plot.

## Requirements

- Python 3.x
- Requests library
- Matplotlib library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries by running:

```bash
pip install requests matplotlib
```

## Usage

To use the Stock Portfolio Tracker, run the script from your terminal:

```bash
python Stock_portfolio_tracker.py
```

Follow the interactive prompts to manage your stock portfolio:

1. **Add Stock**: Enter the stock symbol and quantity to add it to your portfolio.
2. **Remove Stock**: Specify the stock symbol and quantity you wish to remove.
3. **View Portfolio Value**: Check the current value of your entire portfolio.
4. **View Portfolio Value Over Time**: Plot the changes in your portfolio's value over time.
5. **Exit**: Close the application.

## Configuration

You must provide your own Alpha Vantage API key to fetch stock prices. Replace `'YOUR_ALPHA_VANTAGE_API_KEY'` in the code with your actual API key.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

This project is open-source and available under the MIT License.
