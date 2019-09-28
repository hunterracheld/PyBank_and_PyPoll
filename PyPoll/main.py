## PyPoll

#import necessary dependencies
import os
import csv
import numpy as np

#create variable for file path to csv
working_csv = os.path.join('..','Resources','election_data.csv')

#create function to hold all election date and write it to a textfile
def print_totals(election_data, text_file):
	
	#create list of votes based on 3rd item in every row
	votes = [row[2] for row in election_data]
	totalvotes = int(len(votes))
	
	#print total votes to make sure code is working

	#create list of all names
	allnames = np.array(votes)
	
	#create list of all unique names
	candidates = np.unique(allnames)

	#create dictionary for candidates [key] and total votes for each [value]
	candidate_votes = {}
	
	#print candidates list to make sure code is working

	#loop through candidates, set each value to 0
	for cand in candidates:
		candidate_votes[cand] = 0
	
	#print candidate_votes to make sure code is working
	
	#loop through candidates again, this time setting value to +1 each time name occurs
	for votegetter in votes:
		candidate_votes[votegetter] = candidate_votes[votegetter] + 1
	
	#print candidate_votes to make sure code is working

	#The winner of the election based on popular vote.
	winner_votes=0
	winner_name = ""
	for key , value in candidate_votes.items():
		if value > winner_votes:
			winner_votes = value
			winner_name = key
	
	# create new dictionary for percentage totals 
	candidate_ps = {}

	# loop through unique values in candidate list to set keys, value equals percentage of votes each candidate won
	for cand in candidates:
		candidate_ps[cand] = '{:.3f}'.format((candidate_votes[cand]/totalvotes)*100)
	
	#create function to print results to terminal and write to text file
	def printandwrite(results):
		print (results)
		text_file.write(f'{results}\n')
	
	printandwrite("----------------")
	printandwrite("Election Results")
	printandwrite("----------------")
	printandwrite(f'Total Votes: {totalvotes}')
	printandwrite("----------------")
	for name in candidates:
		printandwrite(f'{name}: {candidate_ps[name]}% ({candidate_votes[name]})')
	printandwrite("----------------")
	printandwrite(f'Winner: {winner_name}')
	printandwrite("----------------")
		
#read csv and pass it through function
# call csv
with open (working_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")

	# Read the header row first
	csv_header = next(csvreader)

	# make csvreader iterable so both list comprehensions can be completed
	electiondata = list(csvreader)

	# Set variable for output file
	output_file = os.path.join('..', "PyPoll", "p_analysis.txt")
	# Open the output file
	with open(output_file, "w") as text_file:
		#call print_totals and pass electiondata and text_file to it
		print_totals(electiondata, text_file)
   