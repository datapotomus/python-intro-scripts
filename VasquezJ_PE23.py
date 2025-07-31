#Debug the User Input Handler

import pyinputplus as pyip

print("User Input Processing System")

age = pyip.inputNum("Enter your age: ", min=1)
if age >= 18:
    print("You are an adult.")
elif age < 18:
    print("You are a minor.")
else:
    print("Invalid input.")
