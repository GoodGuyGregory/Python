#Program 3-7 (Loan Qualifiers)

#This program determines wheater a bank customer
#qualifies for a loan

min_salary = 30000.0 #The minimum annual salary
min_years = 2 #The minimum years on the job

#Get the customer's annual salary
salary = float(input('Enter your annual salary:'))


#Get the number of years worked on their current job.
years_on_job = int(input('Enter the number of years employed:'))

#Determine wheather the customer qualifies.
if salary >= min_salary and years_on_job >= min_years:
    print('You qualify for this loan.')
else:
    print('Unfortunately you do not qualify for this loan.')
        
