#PyBank Financial Data Analysis
#-------------------------------

#Step 1: Import the modules I'll need
import os
import csv

#Step 2: Define and Identify the budget_data.csv file we'll use for PyBank
bankcsv = os.path.join("Resources","budget_data.csv")

dates = []
total = 0
profitlossprevious = 0
totalrowchange = 0
greatestincrease = 0
greatestdecrease = 0

with open(bankcsv, newline="") as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")
    #print(bankreader)
    
    bank_header = next(bankreader)
    
    for row in bankreader:

        #Checking to see if there's a month
        if len(dates) == 0.0:
            profitlossprevious = int(row[1])
            print("Otherworks")

        #Step 3: Find the total number of months included in the dataset (Output will be 'Total months: 86')
        dates.append(row[0])

        #Step 4: Find the net total amount of "Profit/Losses" over the entire period (total will be $38,382,578)
        total = total + int(row[1])

        #Step 5: Find the average of the changes in "Profit/Losses" over the entire period (avg. will be -$2,315.12)

        rowchange = int(row[1]) - profitlossprevious 
        totalrowchange = totalrowchange + rowchange
        profitlossprevious = int(row[1])

        #Step 6: Find the greatest increase in profits (date and amount) over the entire period (result will be Feb-2012 $1,926,159)
        
        if rowchange > greatestincrease:
            greatestincmonth = row[0]  
            greatestincrease = rowchange

        #Step 7: Find the greatest decrease in losses (date and amount) over the entire period (result will be Sep-2013  $(2,196,167)
        if rowchange < greatestdecrease:
            greatestdecmonth = row[0]
            greatestdecrease = rowchange

    averagechange = round(totalrowchange / (len(dates)-1), 2)

    #Print results
    
    print("Financial Analysis")
    print("------------------")
    print(f'Total Months: {len(dates)}')
    print(f'Total Profit/Loss: ${total}')
    print(f'Average Profit/Losses Change: ${averagechange}')
    print(f'Greatest Increase: {greatestincmonth} ${greatestincrease}')
    print(f'Greatest Decrease: {greatestdecmonth} ${greatestdecrease}')

#Step 8: Your final script should both print the analysis to the terminal and export a text file with the results.
    outputpath = os.path.join("output","PyBankAnalysis.txt")
    outputfile = open(outputpath, "w")

    #Writing out the text
    outputfile.writelines("Financial Analysis")
    outputfile.writelines("\n------------------")
    outputfile.writelines(f'\nTotal Months: {len(dates)}')
    outputfile.writelines(f'\nTotal Profit/Loss: ${total}')
    outputfile.writelines(f'\nAverage Profit/Losses Change: ${averagechange}')
    outputfile.writelines(f'\nGreatest Increase: {greatestincmonth} ${greatestincrease}')
    outputfile.writelines(f'\nGreatest Decrease: {greatestdecmonth} ${greatestdecrease}')