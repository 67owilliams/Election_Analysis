#The data that needs to be retrieved
import csv
import os
#file_to_load = "C:\Users\odas4\Desktop\Class_Folder\Module_3\Resources\election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")

#Open CSV file
#election_data = open(file_to_load, "r")
with open(file_to_load) as election_data:
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

#1.The toal number of votes cast
#2.A complete list of candidates that received votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on popular vote

#Close CSV file
election_data.close()