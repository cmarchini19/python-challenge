#PyBank Financial Data Analysis
#-------------------------------

#Step 1: Import the modules I'll need
import os
import csv


#Step 2: Identify the budget_data.csv file we'll use for PyPoll
bankcsv = os.path.join("Resources","budget_data.csv")

dates = []
total = 0.0
average = [(total + int(row[1])]

with open(bankcsv, newline="") as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")
    #print(bankreader)
    
    bank_header = next(bankreader)

    for row in bankreader:

        #Step 3: Find the total number of months included in the dataset (Output will be 'Total months: 86')
        dates.append(row[0])

        #Step 4: Find the net total amount of "Profit/Losses" over the entire period (total will be $38,382,578)
        total = total + int(row[1])

        #Step 5: Find the average of the changes in "Profit/Losses" over the entire period (avg. will be -$2,315.12)
        avg_change = 

    print(f'Total Months: {len(dates)}')
    print(f'Total Profit/Loss: ${total}')


    
#Step 4: Find the net total amount of "Profit/Losses" over the entire period (total will be $38,382,578)

    # total = total + int(row[1])
    # print(f'Total Profit/Loss: {total}')

#print (net)


#Step 5: Find the average of the changes in "Profit/Losses" over the entire period (avg. will be -$2,315.12)



#Step 6: Find the greatest increase in profits (date and amount) over the entire period (result will be Feb-2012 $1,926,159)


    #print(f"Greatest Increase:"  )

#Step 7: Find the greatest decrease in losses (date and amount) over the entire period (result will be Sep-2013  $(2,196,167)

#Step 8: Your final script should both print the analysis to the terminal and export a text file with the results.