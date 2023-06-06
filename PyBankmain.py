import os
import csv
#Set File Path

csv_homework = os.path.join("Resources", "budget_datafinal.csv")

#Output
text_path = "output.txt"

#Variables
sum_months = 0
sum_revenue = 0
average_revenue = 0
revenue_change = 0
revenue = []
prev_revenue = 0
month_change = []
largest_decrease = ["",999999]
largest_increase = ["",0]
revenue_change_month = []

with open(csv_homework) as csvfile:
    csvreader = csv.DictReader(csvfile)
#print unique months
    for row in csvreader:
        sum_months+=1
#total revenue
        sum_revenue = sum_revenue + int(row["Profit/Losses"])
#average change in revenue
        revenue_change = float(row["Profit/Losses"])- prev_revenue
        prev_revenue = float(row["Profit/Losses"])
        revenue_change_month = revenue_change_month + [revenue_change]
        month_change = [month_change] + [row["Date"]]

#Greatest Increase
        if revenue_change>largest_increase[1]:
            largest_increase[1]= revenue_change
            largest_increase[0]= row['Date']

#Greatest Decrease
        if revenue_change<largest_decrease[1]:
            largest_decrease[1]= revenue_change
            largest_decrease[0]= row['Date']

    average_revenue = sum(revenue_change_month)/len(revenue_change_month)

# Send to TXT
with open(text_path, 'w') as file:
    file.write("CSV_Homework_3\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % sum_months)
    file.write("Total Revenue: $%d\n" % sum_revenue)
    file.write("Average Revenue Change $%d\n" % average_revenue)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (largest_increase[0], largest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (largest_decrease[0], largest_decrease[1]))