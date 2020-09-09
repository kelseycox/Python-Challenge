import os
import csv

# Create three separate lists to hold each column
voter_id_list = []
county_list = []
candidate_list = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))
os.chdir("..")

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")


# Read in the CSV file
with open(election_data_csv_path, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip headers
    next(csvreader)
    # Loop through the data
    for row in csvreader:
        voter_id_list.append(int(row[0]))
        county_list.append(row[1])
        candidate_list.append(row[2])

# The total number of votes cast
vote_total = len(voter_id_list)

# A complete list of candidates who received votes
# The total number of votes each candidate won
candidate_count = len(candidate_list)

li_count = candidate_list.count("Li")
khan_count = candidate_list.count("Khan")
otooley_count = candidate_list.count("O'Tooley")
correy_count = candidate_list.count("Correy")

# The percentage of votes each candidate won
candidate_percent = (candidate_count / vote_total * 100)
li_percent = (li_count / candidate_count * 100)
khan_percent = (khan_count / candidate_count * 100)
otooley_percent = (otooley_count / candidate_count * 100)
correy_percent = (correy_count / candidate_count * 100)

# The winner of the election based on popular vote
count = [li_count, khan_count, otooley_count, correy_count]
winner = max(count)
if winner == li_count:
    winner_name = "Li"
elif winner == khan_count:
    winner_name = "Khan"
elif winner == otooley_count:
    winner_name = "O'Tooley"
elif winner == correy_count:
    winner_name = "Correy"
else:
    winner_name = "No Winner"

# Format all numbers to 0.00
candidate_percent = ("{:.3f}".format(candidate_percent))
li_percent = ("{:.3f}".format(li_percent))
khan_percent = ("{:.3f}".format(khan_percent))
otooley_percent = ("{:.3f}".format(otooley_percent))
correy_percent = ("{:.3f}".format(correy_percent))


# Export Analysis to output file
output = open('Analysis\poll_output.txt', 'w')
output.write("Election Results\n")
output.write("-------------------------\n")
output.write("Total Votes: " + str(vote_total) + "\n")
output.write("-------------------------\n")
output.write("Li: " + str(li_percent) + "% (" + str(li_count) + ")\n")
output.write("Khan: " + str(khan_percent) + "% (" + str(khan_count) + ")\n")
output.write("OTooley: " + str(otooley_percent) +
             "% (" + str(otooley_count) + ")\n")
output.write("Correy: " + str(correy_percent) +
             "% (" + str(correy_count) + ")\n")
output.write("-------------------------\n")
output.write("Winner: " + winner_name + "\n")
output.write("-------------------------")
output.close()

# Print to Console
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_total))
print("-------------------------")
print("Li: " + str(li_percent) + "% (" + str(li_count) + ")")
print("Khan: " + str(khan_percent) + "% (" + str(khan_count) + ")")
print("OTooley: " + str(otooley_percent) + "% (" + str(otooley_count) + ")")
print("Correy: " + str(correy_percent) + "% (" + str(correy_count) + ")")
print("-------------------------")
print("Winner: " + winner_name)
print("-------------------------")
