#classifies a number based on its divisibility and whether it is even or odd.
#The program should evaluate the following conditions in order:

try:
    print('Please enter a positive integer: ', end='')
    posInt = int(input())

    if posInt <= 0:
        print('Invalid input. Please enter a positive integer.')
    elif posInt % 3 == 0 and posInt % 5 == 0:
        print('The number is divisible by both 3 and 5')
    elif posInt % 3 == 0:
        print('The number is divisible by 3 only')
    elif posInt % 5 == 0:
        print('The number is divisible by 5 only.')
    elif posInt % 2 == 0:
        print('The number is even and not divisible by 3 or 5')
    elif posInt % 2 == 0 and posInt % 3 != 0 and posInt % 5 != 0:
        print('The number is even and not divisible by 3 or 5')
    # elif posInt % 2 != 0 and posInt % 3 != 0 and posInt % 5 != 0:
     #   print('The number is odd and not divisible by 3 or 5')
    else:
        print('The number is odd and not divisible by 3 or 5')
        
except ValueError:
    print('Invalid input.')


