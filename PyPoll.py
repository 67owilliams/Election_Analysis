import csv
import os

#Set variable to path to open
file_to_load = os.path.join("Resources", "election_results.csv")

#Set variable to path to save
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Intialize total_votes variable
total_votes = 0

#Initialize list for candidates
candidate_options = []

#Initialize dict for candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election_results.csv to read
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
         #1.The toal number of votes cast
        total_votes += 1
        #2.A complete list of candidates that received votes
        candidate_name = row[2]
       
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Append to the list of candidates.
            candidate_options.append(candidate_name)
            #Set candidate votes
            candidate_votes[candidate_name] = 0

        #Count candidate votes
        candidate_votes[candidate_name] += 1

    #3.The percentage of votes each candidate won
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #4.The total number of votes each candidate won
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent =
            #vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #5.The winner of the election based on popular vote
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

#Close CSV file
election_data.close()