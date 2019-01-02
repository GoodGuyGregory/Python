first_name = input("What is your first name? ")
print("Hello", first_name)
if first_name == "Greg":
	print(first_name, "is learning Python")
elif first_name == "Random Guy":
	print(first_name, "is not a real name")
else:
	#perhaps our users Can't read.
	#cast the string
	age = int(input("How old are you? "))
	#7 is a decent age for reading comprehension
	if age <= 6:
		print("Dude, you're {}! If you can read this already....".format(age))
	print("You should totally learn Python, {}!".format(first_name))
		
print("Have a great day {}!".format(first_name))
	  