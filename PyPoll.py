# add our dependencies
import csv
import os
# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize vote counting variable and setting to zero
total_votes = 0
# candidate options and cadidate votes
candidate_options = []
candidate_votes = {}
# track winning candidate, vote count, and percentage
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
        # add to the total vote count
        total_votes += 1
        # get candidate name from each row
        candidate_name = row[2]
        # if candidate does not match any existing candidate add to candidate list
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1 

# save results to text file 
with open(file_to_save, "w") as txt_file:
    # Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # print candidate name and % of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # save candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Pring the winning candidates results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidates results to the text file
    txt_file.write(winning_candidate_summary)