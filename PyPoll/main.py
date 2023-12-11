# Start by importing
import os
import csv

# Set path
path = os.path.join('PyPoll', 'Resources', 'election_data.csv')


# Set variables
count = 0
candidate_list = []
candidate = []
vote_count = []
vote_percent = []

# Open and read CSV 

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header label
    csv_header = next(csvreader)
    
    # Conduct the ask
    for row in csvreader:
       
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidate_list.append(row[2])
    
    # Create a set from the candidatelist to get the candidates names
    for x in set(candidate_list):
        candidate.append(x)

        total_vote_candidate = candidate_list.count(x)
        vote_count.append(total_vote_candidate)
        percent_votes_candidate = round((total_vote_candidate/count)*100, 2)
        vote_percent.append(percent_votes_candidate)
        
    winning_vote_count = max(vote_count)
    winner = candidate[vote_count.index(winning_vote_count)]


    
#Print to terminal

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate))):
        text.write(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("---------------------------------------\n")