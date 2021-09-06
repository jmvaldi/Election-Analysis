# The data we need to retrieve.
# 1. The toal number of votes cast.
# 2. A complete list of candidates who receive votes.
# 3. The percentage of votes each candidate won.
# 4. The toal number of votes each candidate won.
# 5. The winner of elections based on popular votes
# Import the datetime class from the datetime module.

#Add our dependecies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

 # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)    