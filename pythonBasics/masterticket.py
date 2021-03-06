#import math to use the ceiling function
import math

TICKET_PRICE = 10
# Create a New constant for service charge ($2.00)
SERVICE_CHARGE = 2
tickets_remaining = 100

# Create a function that will allow calculate prices for user
# Takes number of tickets and returns num_tickets * TICKET_PRICE
def calculate_price(num_tickets):
	 
		# add the service charge to our result
		return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Runs this code until all of the tickets are sold out!
# while any number is greater than 0 it is considered true
while tickets_remaining >= 1:
	# Output how many tickets are remaining using the tickets_remaining variable
	
	print("There are {} tickets remaining.".format(tickets_remaining))
	
	# personalize the experience for the user:
	# Gather information about the user: such as name ect
	
	print("Welcome to Master Ticket!" )
	user_name = input("What is your name? ")
	
	# Prompt the user by name and ask how many tickets they would lik	
	num_tickets = input("Welcome {}, how many tickets would you like to purchase for the show?  ".format(user_name))
	# Expect a ValueError: Handler Below
	try:
		num_tickets = int(num_tickets)
		#Raise a ValueError if the request is greater than the total tickets available
		if num_tickets > tickets_remaining:
				raise ValueError("There are currently {} tickets vailable".format(tickets_remaining))
					
	# except expected error
	except ValueError as err:
		#display appropriate message for the user
		
		print("Oops, We need to know how many tickets you would like here {}.".format(user_name , err))
		
	# Calculate the price (total = number of tickets multiplied by the price) for the user based on the ticket vairable 
	else:
			# Display the desired number of tickets
			print("Excellent, it appears you would like {} tickets to the show".format(num_tickets))
		
			amount_due = calculate_price(num_tickets)
		
			# Display the total for the user.
		
			print("Your total will be ${}".format(amount_due))
		
			# Prompt the user if they want to proceed with their order! Y/N?
			response = input("Would you like to proceed with your order? Y/N ")
		
			# if they choose to proceed 
			if response.lower() == "y":	
			# print out "SOLD"! to confirm their purchases
				print("SOLD! you have purchased {} tickets".format(num_tickets))
			# decrease or decrement the total number of tickets 
				tickets_remaining -= num_tickets
				print("There are are {} tickets remaining! Enjoy the show!".format(tickets_remaining))
else:
			# thank them by name for visiting.
			print("Thanks for visiting {}".format(user_name))
		
# Notify the user that there aren't any tickets remaining to purchase
# tell them that the tickets are Sold out!
print("Sorry we are all sold out of tickets for this show!")	