stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400
}

total = 0

print("Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or done): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total += investment

        print("Investment:", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment:", total)
print("Thank you!")