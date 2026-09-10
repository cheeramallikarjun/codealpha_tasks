print("Stock Portfolio Tracker")
print("-----------------------")

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420
}

# Total investment
total_investment = 0

# Store portfolio details
portfolio = []

while True:

    # Ask for stock name
    stock = input("Enter stock name: ").strip().upper()

    # Check whether stock exists
    if stock not in stock_prices:
        print("Invalid stock name!")
        print("Available stocks: AAPL, TSLA, GOOGL, MSFT")
        continue

    # Get stock price
    price = stock_prices[stock]

    print("Price:", price)

    # Ask for quantity
    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = price * quantity

    # Add to total
    total_investment = total_investment + investment

    # Store stock information
    portfolio.append(
        f"{stock} - {quantity} shares - Investment: {investment}"
    )

    # Display result
    print("Investment:", investment)
    print("Total Investment:", total_investment)

    # Ask whether to continue
    again = input("Do you want to add another stock? (yes/no): ")

    if again.lower() == "no":
        break

# Final total
print("-----------------------")
print("Final Total Investment:", total_investment)

# Save portfolio to file
with open("portfolio.txt", "w") as file:

    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")

    for item in portfolio:
        file.write(item + "\n")

    file.write("-----------------------\n")
    file.write(f"Final Total Investment: {total_investment}\n")

print("Portfolio saved to portfolio.txt")