import os
import csv

# Create two separate lists to hold each column
date_list = []
profit_loss_list = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))
os.chdir("..")

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_data_csv_path, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    # Loop through the data
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(int(row[1]))

# The total number of months included in the dataset
month_total = len(date_list)

# The net total amount of "Profit/Losses" over the entire period
net_total = sum(profit_loss_list)

# The average of the changes in "Profit/Losses" over the entire period
average_change = sum(profit_loss_list)/len(profit_loss_list)
average_change = ("{:.2f}".format(average_change))

# The greatest increase in profits (date and amount) over the entire period
greatest = max(profit_loss_list)
greatest_date_index = profit_loss_list.index(greatest)
greatest_increase_date = date_list[greatest_date_index]

# The greatest decrease in losses (date and amount) over the entire period
least = min(profit_loss_list)
least_date_index = profit_loss_list.index(least)
greatest_decrease_date = date_list[least_date_index]

# Export Analysis to output file
output = open('Analysis\output.txt', 'w')
output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write("Total Months: " + str(month_total)+"\n")
output.write("Total: $" + str(net_total)+"\n")
output.write("Average Change: $" + str(average_change)+"\n")
output.write("Greatest Increase in Profits: " +
             str(greatest_increase_date) + "($" + str(greatest) + ")\n")
output.write("Greatest Decrease in Profits: " +
             str(greatest_decrease_date) + "($" + str(least) + ")\n")
output.close()


# Print to Console
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_total))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " +
      str(greatest_increase_date) + "($" + str(greatest) + ")")
print("Greatest Decrease in Profits: " +
      str(greatest_decrease_date) + "($" + str(least) + ")")
