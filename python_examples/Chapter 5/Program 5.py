#Program 5-15

#The following is used as a global constant
#the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter your gross pay: '))
    bonus = float(input('Enter the combined net amount of your bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
#pay as an argument and displays the retirement
#contribution.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution to retirement account: $', \
          format(contrib, ',2.f'), \
          sep='')

#The show_bonus_contrib function accepts the
#bonus ammount as an argument and displays the
#amount going into the retirement account from the bonus checks
# we recieve.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Bonus contribution to the account: $', \
          format(contrib, ',.2f'), \
          sep='')

#call the main function
main()
