#Program 4-17

#This Program averages test scores.
#It askes the user for the number of students
#and the number of test scores per students.

#Get the number of students.
num_students = int(input('How many students do you have?'))

#Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student?'))

#Determine each studen's average test score.
for student in range(num_students):
    #Initialize an accumulator for test score loop
    total = 0.0
    #Get a student's test scores.
    print('Student number', student + 1)
    print('-----------------')
    for test_num in range(num_test_scores):
        print('Test number', test_num + 1, end='')
        score = float(input(': '))
        #Add the scores to the accumulator.
        total += score

    #Calculate the average test score for this student.
        average = total / num_test_scores

#Display the average.
    print('The average for student number', student + 1, \
                  'is:', average)
    print()
