import os
import csv

PyBank = os.path.join("Resources/PyBank_budget_data.csv")

output_path = os.path.join("Analysis/pybank_results.txt")

date = []
p_l = []
change_in_profit_loss = []

with open(PyBank) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csvreader: 
        date.append(row [0])
        p_l.append(float (row[1]))

    for i in range(1,len(p_l)):
        change_in_profit_loss.append(p_l[i]-p_l[i-1])
        avg_in_profit_loss = sum(change_in_profit_loss)/len(change_in_profit_loss)
        greatest_profit = max(change_in_profit_loss)
        greatest_profit_index = change_in_profit_loss.index(greatest_profit) + 1
        greatest_loss = min(change_in_profit_loss)
        greatest_loss_index = change_in_profit_loss.index(greatest_loss) + 1

# question one
print(f'total number of months {len(date)}')

# question two
print(f'sum of profit loss {sum(p_l)}')

# question 3
print(f'avg change in profit loss {round(avg_in_profit_loss,2)}')

#question 4
print(f'greatest profit {date[greatest_profit_index]} {greatest_profit}')

# question 5
print(f'greatest loss {date[greatest_loss_index]} {greatest_loss}')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Write the first row (column headers)
    txtfile.write
    
