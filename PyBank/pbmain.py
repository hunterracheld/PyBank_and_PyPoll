## PyBank
#import dependecies
import os

import csv

#create filepath for csv
working_csv = os.path.join('..', 'Resources','budget_data.csv')

#use a function to calculate totals with budget_data & text_file as parameter 
# use a list comprehension to get all values from column 1 [index 0] and column 2 [index 1]
def print_totals(budget_data, text_file):
    alldates = [row[0] for row in budget_data]
    profitloss = [int(row[1]) for row in budget_data]

    #get total months in dataset
    totalmonths = (len(alldates))

    #get total value of all profit & loss values
    total = sum(profitloss)
  
    #get average of all profit & loss values
    average = round((total/totalmonths),2)

    #format average as curerency
    formattedaverage = format(average, ",.2f")

    #get minimum & maximum values from all profit & loss values, and adjacent date
    mintotal = min(profitloss)
    mindate = alldates[profitloss.index(mintotal)]

    maxtotal = max(profitloss)
    maxdate = alldates[profitloss.index(maxtotal)]

    #print results to terminal & text file
    def printandwrite(results):
        print (results)
        text_file.write(f'{results}\n')
    
    printandwrite ("------------------")
    printandwrite ("Financial Analysis")
    printandwrite ("------------------")
    printandwrite (f'Total Months: {totalmonths}')
    printandwrite (f'Total:  $ {total}')
    printandwrite (f'Average Change: $ {formattedaverage}')
    printandwrite (f'Greatest Increase in Profits:  {maxdate} (${maxtotal})')
    printandwrite (f'Greatest Decrease in Profits:  {mindate} (${mintotal})')
   

# call csv
with open (working_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    # Read the header row first
    csv_header = next(csvreader)

    # make csvreader iterable so both list comprehensions can be completed
    budgetdata = list(csvreader)

    # Set variable for output file
    output_file = os.path.join('..', "PyBank", "f_analysis.txt")
   
    # Open the output file
    with open(output_file, "w") as text_file:
        
        #call print_totals and pass budgetdata and text_file to it
        print_totals(budgetdata, text_file)


