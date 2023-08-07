from pathlib import Path
import csv

# Create a path to the CSV file
csv_file_path = Path("C:/YEAR 1/P4B/TeaGIF/CSV report/Overheads.csv")

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

# Find the highest overhead
highest_overhead, max_percentage = find_highest_overhead(csv_file_path)

# Print the output
print(f"[HIGHEST OVERHEAD] {highest_overhead.upper()}: {max_percentage:}%")