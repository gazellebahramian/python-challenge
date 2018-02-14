import csv

file_to_load = "Resources/budget_data2.csv"


total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
max_i = ["", 0]
min_d = ["", 9999999999999999999999]

revenue_changes = []

with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        revenue_change = int(row["Revenue"]) - prev_revenue

        prev_revenue = int(row["Revenue"])

        if (revenue_change > max_i[1]):
            max_i[1] = revenue_change
            max_i[0] = row["Date"]

        if (revenue_change < min_d[1]):
            min_d[1] = revenue_change
            min_d[0] = row["Date"]

        revenue_changes.append(int(row["Revenue"]))

    revenue_avg = sum(revenue_changes) / len(revenue_changes)
   
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(max_i[0]) + " ($" +  str(max_i[1]) + ")") 
    print("Greatest Decrease: " + str(min_d[0]) + " ($" +  str(min_d[1]) + ")")
    