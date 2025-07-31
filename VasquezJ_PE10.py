# script defines a list of 10 random integers between 1 and 100,
# then iterates through the list.
import random  # random module
numbers = list(range(1, 100))  # assign variable to be a list from 1 to 100

# need to pick 10 random numbers from list
number_pick = random.choices(numbers, k=10)
print('Numbers:', number_pick)
input('\nPress Enter to see the even numbers in the list.')

print('\nEven numbers found:')

# pick out the even numbers from the list
for k in number_pick:
    if k % 2 == 0:
        print(k)
