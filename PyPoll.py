import csv
import os

#Set variable to path to open
file_to_load = os.path.join("Resources", "election_results.csv")

#Set variable to path to save
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open election_results.csv to read
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    #1.The toal number of votes cast
    #2.A complete list of candidates that received votes
    #3.The percentage of votes each candidate won
    #4.The total number of votes each candidate won
    #5.The winner of the election based on popular vote

#Close CSV file
election_data.close()