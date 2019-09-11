import csv #imported necessary libraries
import os

#initialize variables
months = []
netProfit = []
change_in_netProfit = []
change_in_netProfit_elements = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ''
greatest_decrease_date = ''

#created path to access file and path where new csv file will be created
writerPath = os.path.join("Resources", "Output.csv")
path = os.path.join("Resources","budget_data.csv")

# opened read path and created csv reader object
with open (path,'r',newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    #skipped header row
    next(csvreader)

    #iterate through rows in csv file and append months and net profit to respective lists/arrays
    for row in csvreader:
        months.append(row[0])
        netProfit.append(float(row[1]))

    #iterated through rows, subtracting month 2 from month 1, month 3 from month 2, ect.. to find change in the profit/loss
    for row in range(1,len(netProfit)):
        change_in_netProfit.append(netProfit[row] - netProfit[row - 1])
        change_in_netProfit_elements = len(change_in_netProfit)
    average_change = sum(change_in_netProfit) / change_in_netProfit_elements #divided total changes per month by total number of changes
    
    #used max and min function to find greatest increase and decrease
    greatest_increase = max(change_in_netProfit)
    greatest_decrease = min(change_in_netProfit)

    #used the index number (greatest increase and decrease lists) to match and access months list and store it into variable
    #added 1 to index reference to accomodate discrepancy in index number of netProfit list and greatest increase and decrease lists
    greatest_increase_date = months[change_in_netProfit.index(greatest_increase) + 1]
    greatest_decrease_date = months[change_in_netProfit.index(greatest_decrease) + 1]

    #printed results
    print("Financial Analysis")
    print('-' * 20)
    print(f'Total Months: {len(months)}')
    print(f'Total: {sum(netProfit)}')
    print(f'Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})')

    #opened writer path and created csv writer object
    with open (writerPath,'w',newline='') as new_csvfile:

        csvWriter = csv.writer(new_csvfile, delimiter=',')

        #used csv writer object and writerow method to write elements to csv file 
        csvWriter.writerow(["Total Months","Total","Greatest_Increase_in_profits","Greatest_Decrease_in_profits", "Greatest Increase Date", "Greatest Decrease Date"])

        csvWriter.writerow([len(months),sum(netProfit),greatest_increase,greatest_decrease,greatest_increase_date,greatest_decrease_date ])
    