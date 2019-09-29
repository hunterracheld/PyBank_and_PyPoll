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
    monthlypl = [int(row[1]) for row in budget_data]

    #create list to hold monthly changes
    monthlychange = []
    
    #loop over each item in monthlypl, up to 2nd to last value
    #calculate difference, add that value to monthlychange[]
    for x in range(len(monthlypl)):
        if x < len(monthlypl)-1:
            pl = monthlypl[x]
            nextpl = monthlypl[x+1]
            monthlychange.append(nextpl-pl)
    print (monthlychange)
    
    #get total months in dataset
    totalmonths = (len(alldates))

    #get total value of all profit & loss values
    total = sum(monthlypl)
  
    #get average change of all profit & loss values
    averagechange = (sum(monthlychange)/totalmonths)

    #format average as curerency
    formattedaverage = format(averagechange, ",.2f")

    #get minimum & maximum values from all profit & loss values, and adjacent date
    mintotal = min(monthlypl)
    mindate = alldates[monthlypl.index(mintotal)]

    maxtotal = max(monthlypl)
    maxdate = alldates[monthlypl.index(maxtotal)]

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
