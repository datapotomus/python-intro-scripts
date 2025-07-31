# the program accepts a student's numeric score (between 0 and 100) and classifies it into a letter grade

try:
    for score in range(0, 100):
        print('\nPlease enter your score, it should range from 0 to 100: ',end='')
        score = int(input())

        if score < 0 or score > 100:     # if score is out of range get error msg
            print('Error: Please enter a valid score between 0 and 100')
        elif score >= 90 and score <= 100:  # score of "A"
            print('Your grade is an A, great job!')
        elif score >= 80 and score < 90:  # score of "B"
            print('Your grade is a B, keep up the good work!')
        elif score >= 70 and score < 80:  # score of a "C"
            print('Your grade is a C, we have some work to do.')
        elif score >=60 and score < 70: # score of "D"
            print('Your grade is a D, please see me in my office.')
        elif score < 60:  # score of "F"
            print('Your grade is an F...what have you been doing all semester?!')
    #else:
     #   print('Error: Please enter a valid score between 0 and 100')        
except ValueError:  # error msg if non-integer value entered
    print('Error: Please enter a valid score between 0 and 100')

