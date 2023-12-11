# Start by importing
import os
import csv

# Set path
path = os.path.join('Pybank', 'Resources', 'budget_data.csv')


# Create a list to store the data
budget_data = []

# Define Variables
total_months = []
change_profit_losses = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


# Open and read CSV 
with open(path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header label
    header = next(csvreader)  

    for row in csvreader: 
        
        # Count of months
        count_months += 1

        # Net total amount of profit/loss
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Change in profit loss 
            change_profit_loss = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            total_months.append(row[0])

            # Append each change_profit_losses to the change_profit_losses[]
            change_profit_losses.append(change_profit_loss)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    # Sum and average of the changes in profit and loss
    sum_profit_loss = sum(change_profit_losses)
    avg_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in profit and loss
    max_change = max(change_profit_losses)
    min_change = min(change_profit_losses)

    # Locate the index value of highest and lowest changes in profit and loss
    highest_month_index = change_profit_losses.index(max_change)
    lowest_month_index = change_profit_losses.index(min_change)

    # Assign best and worst month
    best_month = total_months[highest_month_index]
    worst_month = total_months[lowest_month_index]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${avg_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${max_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${min_change})")


#Print to a text file: financial_analysis.txt
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months:  {count_months}\n")
    text.write(f"Total:  ${net_profit_loss}\n")
    text.write(f"Average Change:  ${avg_profit_loss}\n")
    text.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    text.write(f"Greatest Decrease in Losses:  {worst_month} (${min_change})\n")


