#This program will split a total bill from a restaurant or whatever establishment and guarantee an even split
#import math to use Ceil method (which will round up)
import math

def split_check(total, number_of_people):
	#divide the total amongst people
	#use the ceiling to allow rounding 
	#check if the person is giving incorrect information
	if number_of_people <= 1:
		#raise exception and let the user know
		raise ValueError("Looks like you are paying for everything")
		
	return math.ceil(total / number_of_people) 
#exception handling
try:
	total_due = float(input("What is your total? "))
	number_of_people = int(input("How many are in your group? "))
	amount_due = split_check(total_due, number_of_people)
except ValueError as err:
		print("Oh no! That's not a valid value. Try again...")
		print("({})".format(err))
else:
	
	print("Each Person owes ${}".format(amount_due))
	
print("#############################")
#Testing
amount_due = split_check(180,4)
#display results 
print(amount_due)

#Test2:
amount_due = split_check(84.97, 5)
#display result with the format
print("Each Person owes ${}".format(amount_due))
print("#############################")

#Testing with input:
#Need to cast the variables as floats or ints for function call to work

total_due = float(input("What is your total? "))
number_of_people = int(input("How many are in your group? "))
amount_due = split_check(total_due, number_of_people)
print("Each Person owes ${}".format(amount_due))