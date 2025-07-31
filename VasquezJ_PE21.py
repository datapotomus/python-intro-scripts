# Bank Account System that allows users to deposit, withdraw, and check their balance.
import pyinputplus as pyip

def deposit(amount):
    running_balance.append(amount)

def withdraw(amount):
    if amount > sum(running_balance):
        print("Insufficient funds.\nWithdrawal Unsuccessful!")
    
    else:
        neg_amt =  amount * (-1)   
        running_balance.append(neg_amt)
        print("Withdrawal successful.")

def get_balance(running_balance):
    new_bal = sum(running_balance)
    return new_bal

balance = 100
running_balance =[100]

while True:
    print("\nBank Account System")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = pyip.inputNum("Enter amount to deposit: ", min=1)
        deposit(amount)
        print("Deposit successful.")
    
    elif choice == '2':
        amount = pyip.inputNum("Enter amount to withdraw (enter a positive number): ", min=1)
        withdraw(amount)
        
    
    elif choice == '3':
        print("Current Balance: " + str(get_balance(running_balance)))
    
    elif choice == '4':
        print("Exiting system...")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")