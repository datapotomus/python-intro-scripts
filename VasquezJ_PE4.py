# calculates the final price of a product after applying a discount
# discount is determined by the purchase amount and membership type

while True:
    print("What is your purchase amount?")
    price = int(input("$"))

    if price > 0:
        print("Enter membership type (Regular or Premium): ", end="")
        memb = input()

        if memb == "Regular":  # Regular members
            if price > 0 and price < 50:  # discount when price b/w $0 and $50
                print("\nThere is no discount, the final price is: $" + str(float(price)))
                print("\nIf you have more purchases, please continue...")

            elif price >= 50 and price <= 100:  # discount when price
                final_price = price * 0.95  # b/w $50 to $100 (inclusive)
                print("\nThere is a 5% discount, your final price is: $"+ str(float(final_price)))
                print("\nIf you have more purchases, please continue...")

            elif price > 100:  # discount when price over $100
                final_price = price * 0.90
                print("\nThere is a 10% discount, your final price is: $"+ str(float(final_price)))
                print("\nIf you have more purchases, please continue...")
            # else:   # error msg if negative dollar amount or zero
            # print('Error: Please enter a valid purchase amount.'

        elif memb == "Premium":  # Premium members
            if price > 0 and price < 50:  # discount when price b/w $0 and $50
                final_price = price * 0.95
                print("\nThere is a 5% discount, the final price is: $"+ str(float(final_price)))
                print("\nIf you have more purchases, please continue...")

            elif (price >= 50 and price <= 100):  # discount when price b/w $50 to $100 (inclusive)
                final_price = price * 0.90
                print('\nThere is a 10% discount, your final price is: $'+ str(float(final_price)))
                print("\nIf you have more purchases, please continue...")

            elif price > 100:  # discount when price over $100
                final_price = price * 0.85
                print("\nThere is a 15% discount, your final price is: $"+ str(float(final_price)))
                print("\nIf you have more purchases, please continue...")
            # else:   # error msg if negative dollar amount or zero
            # print('Error: Please enter a valid purchase amount.')

        else:  # error msg if incorrect member type
            print('Error: Membership type must be ' + str("'Regular'" + " or " + "'Premium'."))

             #   break
             
    else:
        print("Error: Please enter a valid purchase amount.")
    # break
