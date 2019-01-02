import sys
#sys allows an error to appear when attempt_count is greater thank three like break or continue in other languages
MASTER_PASSWORD = 'opensesame'
password = input("Please enter the secret password: ")
attempt_count = 1
#while the password is incorrect continue the process 
# to allow retry
while password != MASTER_PASSWORD:
	if attempt_count > 3:
		sys.exit("Too many invalid password attempt")
	password = input("Invalid password, try again: ")
	attempt_count += 1
	
print("Welcome to Funky town")

banner = "Happy Birthday!"
for letter in banner:
	print(letter.upper())