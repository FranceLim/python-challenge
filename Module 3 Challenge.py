#odule 3 Challenge
import os
import csv


csvpath=os.path.join('Starter_Code', 'PyBank', 'Resources', 'budget_data.csv')

total_months = 0
total_money = 0

with open(csvpath) as csvdoc:
    csvreader = csv.reader(csvdoc, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



    for row in csvreader:
        list.append(0)
        print(row)
        #print(row[1])

        #date = row[0]
        #profit_loss = row[1]



        #total_months = (row[0])
       



    
#The total number of months included in the dataset