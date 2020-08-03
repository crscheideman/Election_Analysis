# add our dependencies
import csv
import os
# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # print the header row
    headers = next(file_reader)
    print(headers)



# The data we need to retrieve
# 1 The total number of votes cast
# 2 A complete list of canidates who recieved votes
# 3 percentage of votes each canidate won
# 4 Total number of votes for each canidate
# 5 The winner of the election based on popular vote