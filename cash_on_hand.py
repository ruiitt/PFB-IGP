from pathlib import Path
import csv

# Provide the absolute path to the CSV file
csv_file_path = ".github/workflows/cash-on-hand-usd.csv"

with open(csv_file_path, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    cashonhand = [row for row in reader if any(row)]  # Filter out empty strings

# Print the data read from the CSV file without empty strings
for row in cashonhand:
    print(row)

# Find and print the days with cash deficits
for i in range(1, len(cashonhand)):
    prev_cash = int(cashonhand[i - 1][1])
    current_cash = int(cashonhand[i][1])
    
    if current_cash < prev_cash:
        cash_deficit = prev_cash - current_cash
        print(f"[CASH DEFICIT] DAY: {cashonhand[i][0]}, AMOUNT: USD{cash_deficit}")
