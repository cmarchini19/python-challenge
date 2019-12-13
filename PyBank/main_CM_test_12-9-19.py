#PyBank Financial Data Analysis
#-------------------------------

#Step 1: Import the modules I'll need
import os
import csv


#Step 2: Identify the budget_data.csv file we'll use for PyPoll
bankcsv = os.path.join("Resources","budget_data.csv")

with open(bankcsv, newline="") as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")
    #print(bankreader)
    
    bank_header = next(bankreader)
    #DEBUGGING - print(f"Header: {bank_header}")

    for row in bankreader:
        print(row[1])

        #DEBUGGING - print("Step 2 works!")


#Step 3: Find the total number of months included in the dataset (Output will be 'Total months: 86')
    #Working notes:  
        #-How do I add up all the rows in the first column for months?
        #-Use "for row" from Netflix exercise?
        # print(f"Total months: " + sum(row(0))

#def months(month):
       #length = len(month)
       #total = 0.0
       #for month in months:
          # total += sum((row[0])
       # return total

#print (months)
#print ("Step 3 works!")      
    

#Step 4: Find the net total amount of "Profit/Losses" over the entire period (total will be $38,382,578)

#def net(amount):
 #       total = 0.0
  #      for amount in net:
   #         total += int(row[1])
    #    return total

#print (net)


#Step 5: Find the average of the changes in "Profit/Losses" over the entire period (avg. will be -$2,315.12)



#Step 6: Find the greatest increase in profits (date and amount) over the entire period (result will be Feb-2012 $1,926,159)


    #print(f"Greatest Increase:"  )

#Step 7: Find the greatest decrease in losses (date and amount) over the entire period (result will be Sep-2013  $(2,196,167)

#Step 8: Your final script should both print the analysis to the terminal and export a text file with the results.