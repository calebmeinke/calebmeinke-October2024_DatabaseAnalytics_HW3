# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import os
import csv
print(os.path.dirname(os.path.realpath(__file__)))
csvpath = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "Resources","budget_data.csv")


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)