# program calculates the total cost of a purchase after applying 
# the appropriate tax rate based on the purchase location.


print('\nPlease enter the purchase amount: ',end='')
purchase = int(input('$'))
if purchase > 0:
    print('Enter the location (A, B, C, or Other)')
    location = input()

# tax rates per location
# set decimal precision to 2 place for currency
    Tax_A = ("${:,.2f}".format((purchase * .05) + purchase))
    Tax_B = ("${:,.2f}".format((purchase * .08) + purchase))
    Tax_C = ("${:,.2f}".format((purchase * .10) + purchase))
    Other = ("${:,.2f}".format(purchase))

    if location == 'A':     # location A, 5% tax
        print('Total cost including tax: $' + str(Tax_A))
    elif location == 'B':     # location B, 8% tax
        print('Total cost including tax: $' + str(Tax_B))

    elif location == 'C':     # location C, 10% tax
        print('Total cost including tax: $' + str(Tax_C))

    elif location == 'Other':   # location Other, no tax
        print('Total cost including tax: $' + str(Other))
    else:           # error if invalid location entered
        print('Error: Invalid location. Please enter A, B, C, or Other.')
else:       # error if invalid purchase amount entered
    print('Error: Please enter a valid purchase amount.')