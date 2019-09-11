import csv #imported csv and os library
import os

#Initialization and Declaration
votes = []
total_votes = 0
khan = []
correy = []
li = []
tooley = []
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#read and write path objects
path = os.path.join("Resources","election_data.csv")
writePath = os.path.join("Resources", "Results.csv")

#open file for reading csv
with open (path,'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #skip header row
    next(csvreader)

    #loop through rows, and append to respective candidates lists
    for row in csvreader:
        votes.append(row)
        if row[2] == "Khan":
            khan.append(row[2])
        elif row[2] == "Correy":
            correy.append(row[2])
        elif row[2] == "Li":
            li.append(row[2])
        elif row[2] == "O'Tooley":
            tooley.append(row[2])

    #find total votes per candidates and save to variable as an integer
    total_votes = len(votes)
    khan_total = len(khan)
    correy_total = len(correy)
    li_total = len(li)
    tooley_total = len(tooley)

    #divided respective candidate votes by total votes and multiplied by 100 to get percent.
    #truncated decimal places by using round() function
    khan_percent = round((( khan_total / total_votes ) * 100), 2)
    correy_percent = round((( correy_total / total_votes ) * 100), 2)
    li_percent = round((( li_total / total_votes ) * 100), 2)
    tooley_percent = round((( tooley_total / total_votes ) * 100), 2)

    #declared list that that holds candidate totals and found index of the highest voted candidate
    total_votes_per_candidate = [khan_total, correy_total, li_total, tooley_total]
    winner_list_index = total_votes_per_candidate.index(max(total_votes_per_candidate))

    print("Election Results")
    print('-' * 20)
    print(f'Total Votes {total_votes}')
    print('-' * 20)
    print(f'Khan: {khan_percent} ({khan_total})')
    print(f'Correy: {correy_percent} ({correy_total})')
    print(f'Li: {li_percent} ({li_total})')
    print(f"O'Tooley: {tooley_percent} ({tooley_total})")
    print('-' * 20)
    print(f'Winner: {candidates[winner_list_index]}') #matched winner index with candidates index and accesed candidates string value
    print('-' * 20)

    #opened a new file  and created writecsv object
    with open (writePath, 'w', newline='') as new_csv:

        writecsv = csv.writer(new_csv,delimiter=",")

        #used writecsv object and writerow method to write respective arguments into the new csv file
        writecsv.writerow(["Candidates", "Total", "Percent"])
        writecsv.writerow(["Khan", khan_total, khan_percent])
        writecsv.writerow(["Correy", correy_total, correy_percent])
        writecsv.writerow(["Li", li_total, li_percent])
        writecsv.writerow(["O'Tooley", tooley_total, tooley_percent])
        writecsv.writerow(["", "", ""])
        writecsv.writerow(["Total_Votes:", total_votes])
        writecsv.writerow({"Winner:", candidates[winner_list_index]})
    