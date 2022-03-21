import os
import csv

# csv file location path
csvpath = os.path.join("Resources","budget_data.csv")

# Read csv file data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    #Count the number of Months. In the code I am skipping the header line and then counting the rest of the lines
    next(csvreader)
    months = len(list(csvreader))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    
   
    # Calculate the net total amount
    next(csvreader)
    total = []
    for row in csvreader:
        # print(row)
        total.append(int(row[1]))

    net_income = sum(total)
    # print(net_income)






print("Financial Analysis")
print("----------------------------")
print(f"Total Months: " + str(months))
print(f"Total: $" + str(net_income))