# add our dependencies
import csv
import os
# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize vote counting variable and setting to zero
total_votes = 0

# candidate options
candidate_options = []

# create empty candidate votes dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the csv file.
    for row in file_reader:
        # 2. add to the total vote count
        total_votes += 1
        # print the candidate name from each row
        candidate_name = row[2]
        # if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1 

# determine percentage of votes for each candidate by looping thorugh the counts
# iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # print candidate name and % of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    #Determine winning vote count and candidate
    #Determine if votes are great than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true the set winnng_count = votes and winning percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set the winning_candidate equal to candidate name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Print the total votes
print(total_votes)

# print the candidate list
print(candidate_options)

# print the candidate vote dictionary
print(candidate_votes)



# The data we need to retrieve
# 1 The total number of votes cast
# 2 A complete list of canidates who recieved votes
# 3 percentage of votes each canidate won
# 4 Total number of votes for each canidate
# 5 The winner of the election based on popular vote