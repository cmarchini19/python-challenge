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
votes= {}
totalcandidatevotes = 0

with open(pollcsv, newline="") as csvfile:
    electionreader = csv.reader(csvfile, delimiter=",")
    election_reader = next(electionreader)
    
    for row in electionreader:
        #Step 3: Collect number of total votes
        totalvotes = totalvotes + 1

        #Step 4: Identify where candidate data is located
        candidate = row[2]

        #Step 5: Identify how many votes each candidate received
        if candidate not in candidates.keys():
            candidates[candidate] = [row[0]]
            
        else:
            candidates[candidate].append(row[0])

    #Step 6: Identify what percentage of votes the candidates received
    for candidatename in candidates.keys():
        votes[candidatename] = len(candidates[candidatename])
        percentages[candidatename] = len(candidates[candidatename])/totalvotes * 100

#Step 7: Print election results
print(f'Election Results')
print("-------------------")
print(f'Total Votes: {totalvotes}')
print("-------------------")
for candidatename in candidates.keys():
    print(f'{candidatename}: {len(candidates[candidatename])} ({round(percentages[candidatename],3)}%)')

for candidatename in candidates.keys():    
    if len(candidates[candidate]) > totalcandidatevotes:
        totalcandidatevotes = len(candidates[candidate])
        winner = candidatename
print("-------------------")
print(f'Winner: {winner}')
print("-------------------")

#Step 8: Your final script should both print the analysis to the terminal and export a text file with the results.
outputpath = os.path.join("output","PyPollAnalysis.txt")
outputfile = open(outputpath, "w")

#Writing out the text
outputfile.writelines(f'Election Results')
outputfile.writelines("\n-------------------")
outputfile.writelines(f'\nTotal Votes: {totalvotes}')
outputfile.writelines("\n-------------------")
for candidatename in candidates.keys():
    outputfile.writelines(f'\n{candidatename}: {len(candidates[candidatename])} ({round(percentages[candidatename],3)}%)')
outputfile.writelines("\n-------------------")
outputfile.writelines(f'\nWinner: {winner}')
outputfile.writelines("\n-------------------")