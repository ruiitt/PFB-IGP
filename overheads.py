from pathlib import Path
import csv

# Define the CSV file path
csv_file_path = Path(".github/workflows/overheads.csv")

# Function to find the highest overhead
def find_highest_overhead(file_path):
    max_percentage = 0
    highest_overhead = ""

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Get the field names from the header

        for row in reader:
            category = row[fieldnames[0]].strip()  # Use the first field name
            percentage = float(row[fieldnames[1]])

            if percentage > max_percentage:
                max_percentage = percentage
                highest_overhead = category

    return highest_overhead, max_percentage

# The following code will only be executed when this script is run directly, not when imported as a module
if __name__ == "__main__":
    # Find the highest overhead
    highest_overhead, max_percentage = find_highest_overhead(csv_file_path)

    # Write the results to "main.txt" instead of printing to the console
    with open("main.txt", "a") as output_file:
        output_file.write(f"[HIGHEST OVERHEAD] {highest_overhead.upper()}: {max_percentage:.2f}%\n")
