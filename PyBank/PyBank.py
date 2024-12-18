# -*- coding: UTF-8 -*-
# Dependencies
import os
import csv


INPUT_CSV_PATH = os.path.join("Resources","budget_data.csv")
OUTPUT_CSV_PATH = os.path.join("analysis","budget_analysis.txt")


os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
current_month_profit = 0
total_change = 0
greatest_increase_value = -99999999
greatest_decrease_value = 99999999

# Open and read the CSV
with open(INPUT_CSV_PATH) as csvfile:
    # CSV reader specifies variable that holds contents, CSV stands for Comma Separated Values - Therefore the default delimiter is a comma
    csvreader = csv.reader(csvfile)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        current_month_profit = int(row[1])
        # Track the total
        total_months += 1
        #Track the net change
        total_net += current_month_profit
        # Calculate the average net change across the months
        if total_months == 1:
            last_month_profit = current_month_profit
        # Calculate the average net change across the months
        else:
            # Track the net change
            change = current_month_profit - last_month_profit
            total_change += change
            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase_value:
                greatest_increase_value = change
                greatest_increase_month = row[0]
            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease_value:
                greatest_decrease_value = change
                greatest_decrease_month = row[0]
            #Reset
            last_month_profit = current_month_profit 

# Generate the output summary
average_change = total_change / (total_months - 1)
output = f"""
Financial Analysis
-------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(average_change,2)}
Greatest Increase in Profits: {greatest_increase_month}, $ {greatest_increase_value}
Greatest Decrease in Profits: {greatest_decrease_month}, ${greatest_decrease_value}
"""

# Print the output
print(output)

# Write the results to a text file
with open(OUTPUT_CSV_PATH, "w") as txt_file:
    txt_file.write(output)
