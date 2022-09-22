# Michael Quick
# 21 September 2022
# Computes personal inflation given by user and determines type of inflation (low, moderate, high, or hyper)

print("The car went, \n\"vroom!\"")
# Get the user's year of interest and the number of expenditure categories
year = input("Please enter the year that you want to calculate the personal interest rate for: ")
categories = int(input("Please enter the number of expenditure categories: "))

prevExpenses = 0.0
currExpenses = 0.0

# Get expenses for the previous and current year and add them to the total expense of the appropriate year
for i in range(0, categories):
    prevExpenses += float(input("Please enter the expenses for previous year: "))
    currExpenses += float(input("Please enter the expenses for year of interest: "))

# Calculate the inflation rate
infRate = ((currExpenses - prevExpenses) / currExpenses) * 100
print("Personal inflation rate for " + year + " is " + str(infRate) + "%")

# Determine type of inflation
if infRate < 3:
    print("Type of Inflation: Low")
elif 3 <= infRate < 5:
    print("Type of Inflation: Moderate")
elif 5 <= infRate < 10:
    print("Type of Inflation: High")
else:
    print("Type of Inflation: Hyper")
