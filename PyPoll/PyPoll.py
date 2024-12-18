# -*- coding: UTF-8 -*-
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
INPUT_CSV_PATH = os.path.join("Resources", "election_data.csv")  # Input file path
OUTPUT_CSV_PATH = os.path.join("analysis", "election_analysis.txt")  # Output file path

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_dict = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""  
cummulative_votes = 0 

# Open the CSV file and process it
with open(INPUT_CSV_PATH) as csvfile:
    # CSV reader specifies variable that holds contents, CSV stands for Comma Separated Values - Therefore the default delimiter is a comma
    csvreader = csv.reader(csvfile)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Increment the total vote count for each row
    for row in csvreader:
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate in vote_dict.keys():
        # Add a vote to the candidate's count
            vote_dict[candidate] += 1
        else:
            vote_dict[candidate] = 1

# Open a text file to save the output
with open(OUTPUT_CSV_PATH, "w") as txt_file:

    # Print the total vote count (to terminal)
    vote_output = f"Total Votes: {total_votes}\n"
    line_break = "------------------------------------\n"
    print(f"Election Results\n")
    print(vote_output)
    print(line_break)
    
    # Write the total vote count to the text file
    txt_file.write(vote_output)
    txt_file.write(line_break)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in vote_dict.items():

        # Get the vote count and calculate the percentage
        votes = vote_dict[candidate]
        vote_frac = round((votes/total_votes)*100, 3)

        # Update the winning candidate if this one has more votes
        if votes > cummulative_votes:
            cummulative_votes = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_votes = f"{candidate}: {vote_frac}% ({votes})\n"
        print(candidate_votes)
        
        # Write each candidate's vote count to the text file
        txt_file.write(candidate_votes)
        
    # Print final line break to output
    print(line_break)
    # Print final line break to the text file
    txt_file.write(line_break)

    # Generate and print the winning candidate summary
    winner = f"Winner: {winning_candidate}\n"
    print(winner)

    # Save the winning candidate summary to the text file
    txt_file.write(winner)