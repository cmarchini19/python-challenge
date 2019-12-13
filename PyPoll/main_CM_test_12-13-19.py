#PyPoll Analysis
#-------------------------------

#Step 1: Import the modules I'll need
import os
import csv

#Step 2: Identify the budget_data.csv file we'll use for PyPoll
bankcsv = os.path.join("Resources","election_data.csv")

with open(bankcsv, newline="") as csvfile:
    electionheader = csv.reader(csvfile, delimiter=",")
    print(electionheader)
    
    election_header = next(electionheader)
    print(f"Header: {election_header}")
    
    
    for row in electionheader:
        print(sum(row[0])

