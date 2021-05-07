# # Open the data file.
import csv
import os
from collections import defaultdict
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World\n")
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")



############
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)

         # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# 3. Print the total votes.
print(total_votes)
print(candidate_options)
print(candidate_votes)


percentage_votes = {}
for x in candidate_votes:
    percentage_votes[x] = f"{round(candidate_votes[x]/total_votes*100,2)}%"

print(percentage_votes)

print(f"winning candidate: {[x for x in percentage_votes if percentage_votes[x] == max(percentage_votes.values())][0]}")
# # Write down the names of all the candidates.
# # Add a vote count for each candidate.
# # Get the total votes for each candidate.
# # Get the total votes cast for the election.