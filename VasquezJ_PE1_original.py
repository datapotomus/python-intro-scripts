# program evaluates user input and provides appropriate response based on specific conditions.


while True:
    try:
        for num in range(1, 101):
            print('Please enter a number between 1 and 100:')
            num = int(input())

            if num < 1 or num > 100:  # numbers outside of range
                print('\nInvalid input.', end=' ')

            elif num >= 1 and num < 25:  # numbers from 1 to 24 are too low
                print("The number is too low\n")

            elif num >= 25 and num <= 50:  # numbers 25 through 50 (inclusive) are medium
                print('The number is medium\n')

            elif num > 50 and num <= 100:  # numbers 51 through 100 are high
                print('The number is high\n')

    except ValueError:  # error handling
        print("\nInvalid input.", end=" ")


