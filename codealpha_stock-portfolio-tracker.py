# --- Hardcoded stock prices ---
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# --- User Input ---
portfolio = {}
print("Enter stock name and quantity (e.g., AAPL 10). Type 'done' to finish.")
while True:
    entry = input("Stock and quantity: ")
    if entry.lower() == "done":
        break
    try:
        symbol, qty = entry.upper().split()
        qty = int(qty)
        if symbol in stock_prices:
            portfolio[symbol] = portfolio.get(symbol, 0) + qty
        else:
            print(f"Unknown stock: {symbol}")
    except:
        print("Invalid input. Use format: SYMBOL QUANTITY")

# --- Calculate total investment ---
total = sum(qty * stock_prices[symbol] for symbol, qty in portfolio.items())

# --- Display result ---
print("\nPortfolio Summary:")
for symbol, qty in portfolio.items():
    value = qty * stock_prices[symbol]
    print(f"{symbol}: {qty} shares × ${stock_prices[symbol]} = ${value}")
print(f"\n📈 Total Investment Value: ${total}")

# --- Optional: Save to CSV ---
save = input("Save to CSV? (y/n): ").lower()
if save == 'y':
    with open("portfolio_summary.csv", "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = qty * price
            f.write(f"{symbol},{qty},{price},{value}\n")
        f.write(f"Total,,,{total}\n")
    print("✅ Saved to portfolio_summary.csv")
