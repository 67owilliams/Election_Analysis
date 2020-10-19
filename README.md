# Election_Analysis

## Resouces
* Data source: election_results.csv
* Software: Python v.3.8.5, VS Code v.1.50.1

## [Overview of Election Audit](https://github.com/67owilliams/Election_Analysis/blob/main/Analysis/election_analysis.txt)
Using Python to calculate the outcome for the election to find:
* The total number of votes cast.
* Complete list of candidates that received votes.
* The number of votes each candidate received.
* Percentage of votes each candidate won.
* The voter turnout for each county
* The percentage of votes each county
* The county with the highest vote count
* Winner of the election based on popular votes.

## Election-Audit Results
There was a total of 369,711 votes cast during the congressional election.

#### County Analysis
* Jefferson held 10.5% of votes with a total of 38,855.
* Denver held 82.8% of votes with a total of 306,055.
* Arapahoe held 6.7% of votes with a total of 11,606.
* Denver had 306,055 votes of each county holding 82.8% of total votes.

##### Candidate Analysis
* Charles Casper Stockham received 85,213 votes winning 23% of total of votes.
* Diana DeGette received 272,892 votes winning 82.8% of total votes.
* Raymon Anthony Doane received 11,606 votes winning 3.1% of total votes.
* Diana DeGette was the winner of the election who held 73.8% of the votes with a total of 272,892.

## ELection-Audit Summary
This script can be used to run analysis on small town elections up to presidential elections with a bit of tweaking. If the data is there it can be used to easily run analysis from the state level down to individual cities using dictionaries.

    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
It can also be used to find in which locations each candidate was the most popular based on votes cast in each county.
 
        for county_name in county_votes:
            if county_votes[county_name] > county_voter_turnout:
                county_voter_turnout = county_votes[county_name]
                largest_county = county_name
        largest_country_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"
        )
 
