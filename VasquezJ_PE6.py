# asks the user for a starting number and an ending number, then prints all numbers in that range

print ('Please enter a starting number: ', end='')
start_num = int(input())
print ('Please enter an ending number: ', end='')
end_num1 = int(input())
end_num2 = end_num1 + 1

if start_num < end_num2:
    print('Counting from ' + str(start_num) + ' to ' + str(end_num1))
    for i in range(start_num, end_num2, 1):
        print(i, end=' ')
else:
    print('Error: The starting number must be less than or equal to the ending number. Please try again.')
    

