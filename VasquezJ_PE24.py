# Debug the String Processor
# A program created to manipulate user-provided strings by converting
# them to uppercase, reversing them, and checking if they are palindromes

def process_string(text):

    no_whtspace = text.replace(" ", "")
    reversed = text[::-1]
    reversed_text = reversed.replace(" ", "")
    reversed_upper = no_whtspace[::-1].upper()

    uppercase_text = no_whtspace.upper()

    if reversed_upper == uppercase_text:
        is_palindrome = True
    else:
        is_palindrome = False
    return uppercase_text, reversed_text, is_palindrome

user_input = input("Enter a string: ")
uppercased, reversed_str, palindrome = process_string(user_input)

print("Uppercase:", uppercased)
print("Reversed:", reversed_str)
if palindrome:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
