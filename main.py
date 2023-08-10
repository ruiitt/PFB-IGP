# Import paths to main.py

from pathlib import Path
from cash_on_hand import cash_on_hand
from overhead import find_highest_overhead
from profit_and_loss import find_profit_deficits

# Define the paths to the input CSV files
cash_csv_path = Path(".github/workflows/cash-on-hand-usd.csv")
overhead_csv_path = Path(".github/workflows/overheads.csv")
profit_csv_path = Path(".github/workflows/profit-and-loss-usd.csv")

# Execute functions from different modules
cash_deficits = cash_on_hand(cash_csv_path)
highest_overhead, max_percentage = find_highest_overhead(overhead_csv_path)
profit_deficits = find_profit_deficits(profit_csv_path)

# Write results to summary_report.txt
with open("summary_report.txt", "w") as summary_file:

    summary_file.write(f"[HIGHEST OVERHEAD] {highest_overhead.upper()}: {max_percentage:.2f}%\n")

    for result in cash_deficits:
        summary_file.write(result + "\n")

    for day, amount in profit_deficits:
        summary_file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount:.2f}\n")

# Print the contents of the summary_report.txt file
with open("summary_report.txt", "r") as summary_file:
    print(summary_file.read())
