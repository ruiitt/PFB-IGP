import overhead
import cash_on_hand
import profit_and_loss

def main():
    # Execute functions and collect their results
    highest_overhead, max_percentage = overhead.find_highest_overhead(overhead.csv_file_path)
    cash_deficits = cash_on_hand.cash_on_hand(cash_on_hand.csv_file_path)
    profit_deficits = profit_and_loss.find_profit_deficits(profit_and_loss.csv_file_path)

    # Create main.txt and write the results
    with open("main.txt", "w") as output_file:
        output_file.write("[HIGHEST OVERHEAD] " + highest_overhead.upper() + f": {max_percentage:.2f}%\n\n")

        output_file.write("[CASH DEFICITS]\n")
        for result in cash_deficits:
            output_file.write(result + "\n")
        output_file.write("\n")

        output_file.write("[PROFIT DEFICITS]\n")
        for day, amount in profit_deficits:
            output_file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount:.2f}\n")

if __name__ == "__main__":
    main()

    # Read and print the content of main.txt
    with open("main.txt", "r") as output_file:
        print(output_file.read())