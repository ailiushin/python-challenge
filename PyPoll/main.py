import csv
import os

# Reading csv file
csvpath = os.path.join("Resources","election_data.csv")

# Read csv file data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
   # Skip the header
    next(csvreader)

    # List placeholders
    votes = []
    names = []

    # Go through each row and populate lists   
    for row in csvreader:
        
        # add total votes to the list
        votes.append(int(row[0]))

        # add candidate names
        names.append(str(row[2]))

    # count total votes
    total_votes = len(votes)

# determine the list of candidates and sort it in the ascending order
name_list = sorted(set(names))

# set up a dictionary
candidates = {"name": [], "percentage_won": [], "votes_won": []}

# populate names into dictionary
candidates["name"] = name_list

# calculate votes received
candidate1 = sum(1 for items in names if items == (candidates["name"][0]))
candidate2 = sum(1 for items in names if items == (candidates["name"][1]))
candidate3 = sum(1 for items in names if items == (candidates["name"][2]))

# populate votes into dictionary
candidates["votes_won"] = [candidate1,candidate2,candidate3]
# calculate votes percentage and populate into the dictionary
candidates["percentage_won"] = [round((candidate1/total_votes)*100,3),round((candidate2/total_votes)*100,3),round((candidate3/total_votes)*100,3)]

# determine the winner
winnner =candidates["name"][candidates["votes_won"].index(max(candidates["votes_won"]))]

#terminal results
print("Election Results")
print("----------------------------")
print(f"Total Votes: " + str(total_votes))
print("----------------------------")
print(f'{candidates["name"][0]} : {candidates["percentage_won"][0]} % ({candidates["votes_won"][0]}) ')
print(f'{candidates["name"][1]} : {candidates["percentage_won"][1]} % ({candidates["votes_won"][1]}) ')
print(f'{candidates["name"][2]} : {candidates["percentage_won"][2]} % ({candidates["votes_won"][2]}) ')
print("----------------------------")
print(f"Winner: " + winnner)
print("----------------------------")

# create text file
output_path = os.path.join("Analysis","election results.txt")

# print text output file
with open(output_path,"w") as text:
    text.write(f"Election Results\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Votes: " + str(total_votes)+"\n")
    text.write(f"----------------------------\n")
    text.write(f'{candidates["name"][0]} : {candidates["percentage_won"][0]} % ({candidates["votes_won"][0]}) '+"\n")
    text.write(f'{candidates["name"][1]} : {candidates["percentage_won"][1]} % ({candidates["votes_won"][1]}) '+"\n")
    text.write(f'{candidates["name"][2]} : {candidates["percentage_won"][2]} % ({candidates["votes_won"][2]}) '+"\n")
    text.write(f"----------------------------\n")
    text.write(f"Winner: " + winnner + "\n")
    text.write(f"----------------------------")

