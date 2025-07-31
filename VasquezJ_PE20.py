def celsius_to_fahrenheit(float_temp):
    return round(((float_temp * 9 / 5) + 32), 1)


def fahrenheit_to_celsius(float_temp):
    return round(((float_temp - 32) * 5 / 9), 1)


print("Temperature Converter")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Enter your choice: ")

try:
    if choice == "1":
        temp = input("Enter temperature in Celsius: ")
        float_temp = float(temp)
        print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(float_temp))

    elif choice == "2":
        temp = input("Enter temperature in Fahrenheit: ")
        float_temp = float(temp)
        print("Temperature in Celsius: ", fahrenheit_to_celsius(float_temp))

    else:
        print("Invalid choice, please enter 1 or 2")
except ValueError:
    print("Invalid choice, please enter a number")
