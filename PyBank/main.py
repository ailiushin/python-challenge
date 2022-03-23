import os
import csv

# csv file location path
csvpath = os.path.join("Resources","budget_data.csv")

# List placeholders
months = []
total = []
changes = []

# Read csv file data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # Skip the header
    next(csvreader)
    
    # first_row = next(csvreader)
    # profit_previous = first_row[1]
    # # Go through each row and populate lists    
    for row in csvreader:
        
        # add total
        total.append(int(row[1]))

        # add months
        months.append(row[0])
    
    # calculate monthly changes
    for i in range(1,len(total)):
        changes.append(total[i] - total[i-1])

    # calculate  total profit/loss
    net_income = sum(total)

    # calculate  total number of months
    total_months = len(months)

    # calculate average changes for total months
    average_change = round(sum(changes)/(total_months-1),2)

    # identify mix/max values and find corresponding months
    max_increase_value = max(changes)
    max_increase_month = months[changes.index(max(changes))+1]
    max_decrease_value = min(changes)
    max_decrease_month = months[changes.index(min(changes))+1]  

# terminal results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total: $" + str(net_income))
print(f"Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: " + str(max_increase_month) + " " + "($"+str(max_increase_value)+")")
print(f"Greatest Decrease in Profits: " + str(max_decrease_month) + " " + "($"+str(max_decrease_value)+")")

# create text file
output_path = os.path.join("Analysis","analysis.txt")

# print text output file
with open(output_path,"w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Months: " + str(total_months) + "\n")
    text.write(f"Total: $" + str(net_income) + "\n")
    text.write(f"Average Change: $" + str(average_change) + "\n")
    text.write(f"Greatest Increase in Profits: " + str(max_increase_month) + " " + "($"+str(max_increase_value)+")" + "\n")
    text.write(f"Greatest Decrease in Profits: " + str(max_decrease_month) + " " + "($"+str(max_decrease_value)+")" + "\n")