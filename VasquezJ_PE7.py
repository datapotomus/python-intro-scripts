import sys

access_code = 5669
print('Enter 4-digit access code: ', end='')
guess = input()

while True:
    if guess == 'exit':
        sys.exit('System Terminated')
        break
    elif guess == '5669':
        print('Access Granted. Welcome.')
        break
    elif guess != access_code:
        print('Access Denied. Try Again.\n')
        print('Enter Access Code: ')
        guess = input()
