#import math to use the ceiling function
import math

TICKET_PRICE = 10.00

tickets_remaining = 100

# Output how many tickets are remaining using the ttickets_remaining variable

print("There are {} tickets remaining.".format(tickets_remaining))

# personalize the experience for the user:
# Gather information about the user: such as name ect

print("Welcome to Master Ticket!" )
user_name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like
# catsed as an integer 

num_tickets = int(input("Welcome {}, how many tickets would you like to purchase for the show?  ".format(user_name)))

# Display the desired number of tickets

print("Excellent, it appears you would like {} tickets to the show".format(num_tickets))

# Calculate the price (total = number of tickets multiplied by the price) for the user based on the ticket vairable 


amount_due = math.ceil(num_tickets * TICKET_PRICE)

# Display the total for the user.

print("Your total will be ${}".format(amount_due))

# Prompt the user if they want to proceed with their order! Y/N?


# if they choose to proceed 

  # print out "SOLD"! to confirm their purchases
  
  # decrease or decrement the total number of tickets 
  
# Otherwise thank the customer