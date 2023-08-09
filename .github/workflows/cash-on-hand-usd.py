import csv
from pathlib import Path

def cash_on_hand(csv_file_path):
    with open(csv_file_path, mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        cashonhand = [row for row in reader if any(row)]  # Filter out empty strings
        
    results = []
    
    # Find and collect the days with cash deficits
    for i in range(1, len(cashonhand)):
        prev_cash = int(cashonhand[i - 1][1])
        current_cash = int(cashonhand[i][1])

        if current_cash < prev_cash:
            cash_deficit = prev_cash - current_cash
            results.append(f"[CASH DEFICIT] DAY: {cashonhand[i][0]}, AMOUNT: USD{cash_deficit}")
    
    return results

# Provide the absolute path to the CSV file
csv_file_path = ".github/workflows/cash-on-hand-usd.csv"

cash_deficits = cash_on_hand(csv_file_path)

# This part will not print anything to the console
# Instead, it will write the results to a file named "main.txt"
with open("main.txt", "a") as output_file:
    for result in cash_deficits:
        output_file.write(result + "\n")
