from pathlib import Path
import csv
#Read CSV file
csv_file_path = Path("C:\YEAR 1\P4B\TeaGIF\CSV report\Profit and loss.csv")
#Create  dictionary for day-wise total profit amounts
daywise_total = {}


#Compute the difference in the net profit column if net profit on the current day is lower than the previous day. 
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader, None)#Skip the header
    current_day = None  #Keep track of the current day
    total_profit = 0    #Keep track of total profit amount
    
    for row in csv_reader:#Only read Column "Day" and "Amount"
        day = int(row[0])    
        profit = float(row[3]) 
        
        if day != current_day:#Check if the day has changed
            if current_day is not None: #Save the total profit for the previous day
                daywise_total[current_day] = total_profit
            
            current_day = day #Reset for the new day
            total_profit = 0 #Reset value for the new day
        
        
        total_profit += profit #Calculate profit for the current day
    
    if current_day is not None:#Save the total profit for the last day
        daywise_total[current_day] = total_profit


#If the net profit is always increasing, find out the day and amount the highest increment occurs
previous_total = None
highest_increment = 0
increment_day = None
for day, total_amount in daywise_total.items():
    if previous_total is not None:#Comparision 
        increment = total_amount - previous_total
        if increment > highest_increment:
            highest_increment = increment
            increment_day = day
    previous_total = total_amount
if increment_day is not None:
    print(f"Highest Increment Day: {increment_day}")
    print(f"Highest Increment Amount: {highest_increment}")
else:
    print("No increment found in the data.")




#-------CHOOOSE WANT PRINT OUT THE DIFF EACH DAY IN CSV OR TXT , THEN DELETE ONE OF IT BELOW  -----------------------------------------
# Write the profit amount difference into a text file
with open('profit_differences.txt', 'w') as outfile:
    previous_total = None
    for day, total_amount in daywise_total.items():
        if previous_total is not None:
            difference = total_amount - previous_total
            outfile.write(f"Day {day} Profit Difference: {difference}\n")
        previous_total = total_amount
print("Profit differences written to 'profit_differences.txt'.")
#-------------------------------------------------------


# Write the profit amount difference into a CSV file
output_csv_file = 'profit_differences.csv'
with open(output_csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Day', 'Profit Difference'])
    previous_total = None
    for day, total_amount in daywise_total.items():
        if previous_total is not None:
            difference = total_amount - previous_total
            csv_writer.writerow([day, difference])
        previous_total = total_amount
print(f"Profit differences written to '{output_csv_file}'.")
#---------------------------------------------------------------------------


