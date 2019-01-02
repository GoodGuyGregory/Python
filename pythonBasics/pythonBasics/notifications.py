# fine looking unsmelly code 

praise = "You are doing great"
#strings are immutable therefore we use the method upper to capitalize
praise = praise.upper()
# numbers of characters in praise
number_of_characters = len(praise)
result = praise + "!" * number_of_characters
print(result)

advice = "Don't forget to ask for help"
advice = advice.upper()
number_of_characters = len(advice)
result = advice + "!" * number_of_characters
print(result)

advice2 = "Don't repeat yourself. Keep things DRY"
advice2 = advice2.upper()
number_of_characters = len(advice2)
result = advice2 + "!" * number_of_characters
print(result)

#Function to do this
def yell(text):
	text = text.upper()
	number_of_characters = len(text)
	result = text + "!" * (number_of_characters // 2)
	print(result)

yell("You are doing great")
yell("Don't repeat yourself. Keep it DRY")
yell("Don't forget to ask for help")

