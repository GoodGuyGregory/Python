name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
resp = input("{} do you understand While Loops in Python? (Type yes/no) ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
while resp != "yes":
# TODO: Since the user doesn't understand while loops, let's explain them.
	print("{} While loops are conditional statements that will execute continously until a Boolean condition is met".format(name))
	print("While loops are a vital part of most programming languages's conditional logic")
# TODO: Ask the user again, by name, if they understand while loops.
	resp = input("Do you understand While loops now? Y/N ")
  
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("You really know your stuff in Python, Congrats {}!".format(name))
