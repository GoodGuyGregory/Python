print("Begin Entering your Transactions for taxes")

TotalSum = 0
resp = input("Would you like to add expense items? (yes/no) ")

while resp.lower() != "n":
    amount = 0
    amount = float(input("Enter Item Cost: "))
    TotalSum += amount
    resp = input("Add another? y/n ")

print("Total Spent {}" .format(TotalSum))


# Further Work Define Functions for Tax Miles and Expenses
# def Expenses():

# def TravelMiles():
