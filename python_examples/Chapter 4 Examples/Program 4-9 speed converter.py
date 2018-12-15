#Program 4-9 Speed Converter
#This program converts the speeds 60 kph
#through 130 kph (in 10 kph increments)
#to mph.

start_speed = 10         #Starting Speed
end_speed = 190            # Ending speed
increment = 5          #Speed increment 
conversion_factor = 0.6214 #Conversion Factor

#Print the table headings
print('KPH\tMPH')
print('--------------')

#Print the speeds.
for kph in range (start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t', format(mph, '.1f'))
    
            
