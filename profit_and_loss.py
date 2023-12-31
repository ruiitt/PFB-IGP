from pathlib import Path
import csv

csv_file_path = Path(".github/workflows/profit-and-loss-usd.csv")

def find_profit_deficits(csv_file_path):
    profit_deficits = []

    with open(csv_file_path, 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        previous_profit = float('inf')  # Initial value for comparison

        for row in csv_reader:
            day = int(row['Day'])  # Use the correct header name without the special character
            net_profit = float(row['Net Profit'])
            
            if net_profit < previous_profit:
                deficit_amount = previous_profit - net_profit
                profit_deficits.append((day, deficit_amount))

            previous_profit = net_profit

    return profit_deficits

profit_deficits = find_profit_deficits(csv_file_path)
