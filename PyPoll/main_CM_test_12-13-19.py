 #PyPoll Analysis
#-------------------------------

#Step 1: Import the modules I'll need
import os
import csv

#Step 2: Identify the budget_data.csv file we'll use for PyPoll
pollcsv = os.path.join("Resources","election_data.csv")

totalvotes = 0
candidates = {}
percentages = {}

with open(pollcsv, newline="") as csvfile:
    electionreader = csv.reader(csvfile, delimiter=",")
    election_reader = next(electionreader)
    
    for row in electionreader:
        #Step 3: Collect number of votes
        totalvotes = totalvotes + 1

        #Step 4: Identify Candidate Data
        candidate = row[2]

        #Step 5: how many votes did the candidates receive?
        if candidate not in candidates.keys():
            candidates[candidate] = [row[0]]
            
        else:
            candidates[candidate].append(row[0])

    #Step 6: what is the percentage of votes the candidates received?
    for candidatename in candidates.keys():
        percentages[candidatename] = len(candidates[candidatename])/totalvotes * 100

#Step 7: Print Values
print(f'Election Results')
print("-------------------")
print(f'Total Votes: {totalvotes}')
print("-------------------")
for candidatename in candidates.keys():
    print(f'{candidatename} {len(candidates[candidatename])} ({round(percentages[candidatename],3)}%)')
print("-------------------")
print("Winner")

#Step 8: Write output file/csv