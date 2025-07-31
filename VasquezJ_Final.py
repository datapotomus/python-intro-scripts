# Jacob Vasquez, 7/20/2025
# TITLE: Backpacking Gear Gift Card Program
# Program gives user a $1000 gift card to spend on three different outdoor gear categories.
# Categories are backpacks, tents, and sleeping bags.
# Each category has a choice of ultralight or standard gear.
# Program keeps track of gift card balance and warns when balance will exceed gift card.

import sys
import requests
from PIL import Image
import pyinputplus as pyip
gift_card = [1000]  # Global variable for gift card balance
purchases = []  # Global variable for purchases list
shopping_cart = []  # Global variable for shopping cart to keep track of user's selections

# Shopping cart keeps track and displays user's selections
# Function takes 'make' as a parameter and appends it to the shopping_cart list
# It then prints the contents of the shopping cart.
# It is called after each purchase to update the cart.
def shopping_list(make):
    print('\n---YOUR SHOPPING CART---')
    shopping_cart.append(make)
    print("\n".join(shopping_cart))

# Function loads jpg images of gear from internet using Pillow
# It takes three URLs as parameters and opens each image in sequence.
# It uses requests to get the image data and Pillow to open and display the images.
# It is called when the user chooses to see images of the packs, tents, or sleeping bags.
# It handles exceptions if the images cannot be loaded.
def open_image(url1, url2, url3):
    data = requests.get(url1).content
    f = open('img.jpg', 'wb')
    f.write(data)
    f.close()
    img = Image.open('img.jpg')
    img.show()

    data = requests.get(url2).content
    f = open('img.jpg', 'wb')
    f.write(data)
    f.close()
    img = Image.open('img.jpg')
    img.show()

    data = requests.get(url3).content
    f = open('img.jpg', 'wb')
    f.write(data)
    f.close()
    img = Image.open('img.jpg')
    img.show()

# Function maintains and displays running total of gift card as user make selections using
# gift card balance and the purchases list as parameters.
# It calculates the total purchases and checks if the user is exceeding the gift card balance.
# If the user is within the balance, it prompts them to continue shopping or end the program.
# If the user exceeds the balance, it prompts them to continue shopping or end the program with
def card_balance(gift_card, purchases):
    total_purchases = sum(purchases)
    exceed_balance = (total_purchases - gift_card[0])
    exceed_bal_round = f"{exceed_balance:.2f}"
    balance = (gift_card[0] - total_purchases)
    balance_round = f"{balance:.2f}"

    if total_purchases <= gift_card[0]:
        print(f"\n***You have ${balance_round} left on your gift card***")
        continue_shop = pyip.inputChoice(['', 'B'], prompt ='\nPress ENTER to continue shopping OR Press B to see your remaining balance and end program: ')
        if continue_shop.lower() == 'b':
            print(f'You have a remaining balance of ${balance_round} to use later. Thank you for shopping.')
            end = input('Press q to quit: ')
            if end == 'q':
                sys.exit()
            else:
                print('Thank you for shopping. Have a great day!')
                sys.exit()

    elif total_purchases > gift_card[0]:
        print(f'\nYou are about to exceed your gift card by ${exceed_bal_round}!!!!')
        shop = pyip.inputChoice(['y', 'n'], prompt ='\nWould you like to continue shopping? Y or N: ')
        if shop.lower() == 'n':
            print(f'Total amount due is ${exceed_bal_round}.')
            end = input('Press q to end program.')
            if end == 'q':
                sys.exit()
            else:
                print('Thank you for shopping. Have a great day!')
                sys.exit()
        elif shop.lower() == 'y':
            print(f'You owe ${exceed_bal_round}.')

# The main function is the entry point of the program.
# It prompts the user to select a category of gear to shop from.
# It uses pyinputplus to validate the input and ensure it is within the specified range.
# It then calls the main function to start the shopping process.
# The main function contains the logic for each category and the choices available within each category.
# It also includes error handling for invalid inputs and exceptions.
def main():
    print('CONGRATULATIONS!!! You have won a $1000 gift card to buy backpacking gear.')
    print('You get to choose from 3 main product categories: Backpacks, Tents, and Sleeping Bags.')
    while True:
        product = pyip.inputNum('\nPick the category you would like to shop:\nType 1: Backpacks\nType 2: Tents\nType 3: Sleeping Bags\nEnter your selection: ', min=1, max=3)
#------Backpack Category--------
        if product == 1:
            pack_choice = pyip.inputNum('\nWhat type of gear do you want:\nType 1: Ultralight\nType 2: Standard\nEnter your selection: ', min=1, max=2)
            if pack_choice == 1:  # Displays Ultralight backpacks available with gift card# Ultralight backpack choices are displayed
                # It creates instances of the Backpacks class for each backpack and displays their details.
                # It also prompts the user to see images of the backpacks and loads them if the user chooses to do so.
                print('\nThe following Ultralight Packs are available with your gift card:')
                print('-------------------------------------------------------------')
                gregory_ul = Backpacks('Ultralight', 'Gregory', 'Focal', '58', '2.65', 269.95)
                osprey_ul = Backpacks('Ultralight', 'Osprey', 'Exos', '58', '2.8', 260)
                hyperlite_ul = Backpacks('Ultralight', 'Hyperlite', 'Southwest', '55', '1.94', 379)

                print(gregory_ul.display_packs())
                print(osprey_ul.display_packs())
                print(hyperlite_ul.display_packs())

                # Loads images of ultralight packs
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the packs? y or n: ')
                if response.lower() == 'y':
                    try:
                        hyperlite = "https://dks.scene7.com/is/image/GolfGalaxy/22HYPU3400STHWSTBCTP_Black?wid=2000&hei=2000&fit=constrain&fmt=pjpeg"
                        exos = "https://www.osprey.com/media/catalog/product/cache/40c19521a82b2b8a3ae810231e6e32e2/e/x/exos58_s22_side_blueribbon.jpg"
                        gregory = "https://www.gregory.com/dw/image/v2/BBZB_PRD/on/demandware.static/-/Sites-product-catalog/default/dw5e43e269/collections/_gregory/Focal/500x500/GMP_S22_Focal58_OzoneBlack_Front34-Square.jpg"
                        open_image(hyperlite, exos, gregory)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of pack to card_balance function
                # It prompts the user to choose a backpack and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                choice = pyip.inputChoice(['Gregory', 'Osprey', 'Hyperlite'], prompt = '\nWhich pack would you like?\nType: Gregory, Osprey, or Hyperlite: ')
                if choice.lower() == 'gregory':
                    purchases.append(gregory_ul.cost)
                    shopping_list('Gregory Focal 58 Backpack')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'osprey':
                    purchases.append(osprey_ul.cost)
                    shopping_list('Osprey Exos 58 Backpack')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'hyperlite':
                    purchases.append(hyperlite_ul.cost)
                    shopping_list('Hyperlite Southwest 55 Backpack')
                    card_balance(gift_card, purchases)

            if pack_choice == 2:  # Displays Standard backpacks available with gift card
                # It creates instances of the Backpacks class for each backpack and displays their details.
                # It also prompts the user to see images of the backpacks and loads them if the user chooses to do so.
                # It prompts the user to choose a backpack and updates the purchases list and shopping cart accordingly.
                print('\nThe following Standard Packs are available with your gift card:')
                print('-------------------------------------------------------------')
                gregory_std = Backpacks('Standard', 'Gregory', 'Baltoro', '75', '4.83', 379.95)
                osprey_std = Backpacks('Standard', 'Osprey', 'Atmos', '65', '4.6', 340)
                deuter_std = Backpacks('Standard', 'Deuter', 'Aircontact Core', '50 + 10', '4.37', 240)

                print(gregory_std.display_packs())
                print(osprey_std.display_packs())
                print(deuter_std.display_packs())

                # Loads images of standard packs
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the packs? y or n: ')
                if response.lower() == 'y':
                    try:
                        aircontact = "https://m.media-amazon.com/images/I/71rNqFGuLdL._AC_SY679_.jpg"
                        atmos = "https://www.osprey.com/media/catalog/product/cache/b2f1ce2dfe10d3d31bf2056bf6e0d10f/a/t/atmosag65_s22_side_mythicalgreen.jpg"
                        baltoro = "https://m.media-amazon.com/images/I/61P0-PEzNPL._AC_SY355_.jpg"
                        open_image(aircontact, atmos, baltoro)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of pack to card_balance function
                # It prompts the user to choose a backpack and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                # It then calls the main function to start the shopping process.
                choice = pyip.inputChoice(['Gregory', 'Osprey', 'Deuter'], prompt = '\nWhich pack would you like?\nType: Gregory, Osprey, or Deuter: ')
                if choice.lower() == 'gregory':
                    purchases.append(gregory_std.cost)
                    shopping_list('Gregory Baltoro 75 Backpack')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'osprey':
                    purchases.append(osprey_std.cost)
                    shopping_list('Osprey Atmos 65 Backpack')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'deuter':
                    purchases.append(deuter_std.cost)
                    shopping_list('Deuter Aircontact Core 50 +10 Backpack')
                    card_balance(gift_card, purchases)
#------Tent Category--------
        if product == 2:
            tent_choice = pyip.inputNum('\nWhat type of gear do you want:\nType 1: Ultralight\nType 2: Standard\nEnter your selection: ', min=1, max=2)
            if tent_choice == 1:  # Displays Ultralight tents available with gift card
                # It creates instances of the Tents class for each tent and displays their details.
                # It also prompts the user to see images of the tents and loads them if the user chooses to do so.
                # It prompts the user to choose a tent and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                print('\nThe following Ultralight Tents are available with your gift card:')
                print('-------------------------------------------------------------')
                mHardware_ul = Tents('Ultralight', 'Mountain Hardware', 'Strato UL', 2, 3, '2.3', 480)
                big_agnes_ul = Tents('Ultralight', 'Big Agnes', 'Copper Spur UL', 1, 3, '2', 449.95)
                nemo_ul = Tents('Ultralight', 'NEMO', 'Hornet OSMO UL', 3, 3, '2.8', 549.95)
                print(mHardware_ul.display_tents())
                print(big_agnes_ul.display_tents())
                print(nemo_ul.display_tents())

                # Loads images of ultralight tents
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the tents? y or n: ')
                if response.lower() == 'y':
                    try:
                        mHardware = "https://content.backcountry.com/images/items/1200/MHW/MHWZAAT/GREICE.jpg"
                        big_agnes = "https://content.backcountry.com/images/items/900/BAG/BAGZ2GN/TAN.jpg"
                        nemo = "https://content.backcountry.com/images/items/1200/NEM/NEMK063/BIBUGOGR.jpg"
                        open_image(mHardware, big_agnes, nemo)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of tent to card_balance function
                # It prompts the user to choose a tent and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                # It then calls the main function to start the shopping process.
                choice = pyip.inputChoice(['Mountain Hardware', 'Big Agnes', 'Nemo'], prompt = '\nWhich tent would you like?\nType: Mountain Hardware, Big Agnes, or Nemo: ')
                if choice.lower() == 'mountain hardware':
                    purchases.append(mHardware_ul.cost)
                    shopping_list('Mountain Hardware Strato UL 2 Person Tent')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'big agnes':
                    purchases.append(big_agnes_ul.cost)
                    shopping_list('Big Agnes Copper Spur UL 1 Person Tent')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'nemo':
                    purchases.append(nemo_ul.cost)
                    shopping_list('NEMO Hornet OSMO UL 3 Person Tent')
                    card_balance(gift_card, purchases)

            if tent_choice == 2:  # Standard tent choices
                # It creates instances of the Tents class for each tent and displays their details.
                # It also prompts the user to see images of the tents and loads them if the user chooses to do so.
                # It prompts the user to choose a tent and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                # It then calls the main function to start the shopping process.
                print('\nThe following Standard Tents are available with your gift card:')
                print('-------------------------------------------------------------')
                rei_std = Tents('Standard', 'REI Co-op', 'Half Dome', 2, 3, '2.8', 299)
                north_face_std = Tents('Standard', 'North Face', 'Stormbreak', 2, 3, '5.3', 200)
                marmot_std = Tents('Standard', 'Marmot', 'Tungsten', 3, 3, '6', 299)
                print(rei_std.display_tents())
                print(north_face_std.display_tents())
                print(marmot_std.display_tents())

                # Loads images of standard tents
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the tents? y or n: ')
                if response.lower() == 'y':
                    try:
                        rei = "https://s3.amazonaws.com/images.gearjunkie.com/uploads/2025/04/Screenshot-2025-04-07-at-10.59.24-AM.jpg"
                        north_face = "https://content.backcountry.com/images/items/1200/TNF/TNFZEAM/GOLOAKPAV.jpg"
                        marmot = "https://dks.scene7.com/is/image/GolfGalaxy/12306M_FoliageDarkAzure_CLD?wid=2000&hei=2000&fit=constrain&fmt=pjpeg"
                        open_image(rei, north_face, marmot)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of pack to card_balance function
                # It prompts the user to choose a tent and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It then calls the main function to start the shopping process.
                choice = pyip.inputChoice(['REI', 'North Face', 'Marmot'], prompt = '\nWhich tent would you like?\nType: REI, North Face, or Marmot: ')
                if choice.lower() == 'rei':
                    purchases.append(rei_std.cost)
                    shopping_list('REI Half-Dome 2 Person Tent')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'north face':
                    purchases.append(north_face_std.cost)
                    shopping_list('North Face Stormbreak 2 Person Tent')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'marmot':
                    purchases.append(marmot_std.cost)
                    shopping_list('Marmot Tungsten 3 Person Tent')
                    card_balance(gift_card, purchases)
#------Sleeping Bag Category--------
        if product == 3:
            bag_choice = pyip.inputNum('\nWhat type of gear do you want:\nType 1: Ultralight\nType 2: Standard\nEnter your selection: ', min=1, max=2)
            if bag_choice == 1:  # UL sleeping bag choices
                # It creates instances of the Bags class for each sleeping bag and displays their details.
                # It also prompts the user to see images of the sleeping bags and loads them if the user chooses to do so.
                # It prompts the user to choose a sleeping bag and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                print('\nThe following Ultralight Sleeping Bags are available with your gift card:')
                print('-------------------------------------------------------------')
                sea_summit_ul = Bags('Ultralight', 'Sea to Summit', 'Spark', 45, 'Down', '850+', '12.8', 349)
                rab_ul = Bags('Ultralight', 'Rab', 'Mythic Ultra 180', 30, 'Down', '900+', '15.5', 600)
                therm_ul = Bags('Ultralight', 'Therm-a-Rest', 'Hyperion', 32, 'Down', 900, '18', 519.95)
                print(sea_summit_ul.display_bags())
                print(rab_ul.display_bags())
                print(therm_ul.display_bags())

                # Loads images of ultralight sleeping bags
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the sleeping bags? y or n: ')
                if response.lower() == 'y':
                    try:
                        sea_summit = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tradeinn.com%2Ff%2F14060%2F140608928%2Fsea-to-summit-spark-sleeping-bag.jpg"
                        rab = "https://content.backcountry.com/images/items/1200/RAB/RABZ06F/CLOGRA.jpg"
                        therm = "https://content.backcountry.com/images/items/1200/CAS/CAS00EN/BKFO.jpg"
                        open_image(sea_summit, rab, therm)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of sleeping bag to card_balance function
                # It prompts the user to choose a sleeping bag and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                # It then calls the main function to start the shopping process.
                choice = pyip.inputChoice(['Sea to Summit', 'Rab', 'Therm-a-rest'], prompt = '\nWhich sleeping bag would you like?\nType: Sea to Summit, Rab, or Therm-a-Rest: ')
                if choice.lower() == 'sea to summit':
                    purchases.append(sea_summit_ul.cost)
                    shopping_list('Sea to Summit Spark 45' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'rab':
                    purchases.append(rab_ul.cost)
                    shopping_list('Rab Mythic Ultra 180 30' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'therm-a-rest':
                    purchases.append(therm_ul.cost)
                    shopping_list('Therm-a-Rest Hyperion 32' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

            if bag_choice == 2:  # Standard sleeping bag choices
                # It creates instances of the Bags class for each sleeping bag and displays their details.
                # It also prompts the user to see images of the sleeping bags and loads them if the user chooses to do so.
                # It prompts the user to choose a sleeping bag and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                print('\nThe following Standard Sleeping Bags are available with your gift card:')
                print('-------------------------------------------------------------')
                marmot_std = Bags('Standard', 'Marmot', 'Trestles Elite', 30, 'Synthetic', 'n/a', '38.0', 149)
                nemo_std = Bags('Standard', 'NEMO', 'Disco 30 Endless Promise', 30, 'Synthetic', 'n/a', '30.8', 269.95)
                sierra_std = Bags('Standard', 'Sierra Designs', 'Night Cap 20', 20, 'Synthetic', 900, '18', 199.95)
                print(marmot_std.display_bags())
                print(nemo_std.display_bags())
                print(sierra_std.display_bags())

                # Loads images of standard sleeping bags
                # Error handling if images can't load
                response = pyip.inputChoice(['y', 'n'], prompt = '\nWould you like to see images of the sleeping bags? y or n: ')
                if response.lower() == 'y':
                    try:
                        marmot = "https://content.backcountry.com/images/items/1200/MAR/MAR013N/GNLIC.jpg"
                        nemo = "https://www.jensonusa.com/cdn-cgi/image/width=1000,quality=70,format=auto,fit=contain/globalassets/digizuite/78552-en-sg001181-chimera.jpg"
                        sierra = "https://www.enwild.com/mm5/graphics/00000001/30/sierra-designs-night-cap-20_500x500_2.jpg"
                        open_image(marmot, nemo, sierra)
                    except Exception as e:
                        print('We apologize, there seems to be an issue loading the images')

                # Sends price of sleeping bag to card_balance function
                # It prompts the user to choose a sleeping bag and updates the purchases list and shopping cart accordingly.
                # It also calls the card_balance function to check the gift card balance after each purchase.
                # It uses pyinputplus to validate the input and ensure it is within the specified range
                # It then calls the main function to start the shopping process.
                choice = pyip.inputChoice(['Marmot', 'Nemo', 'Sierra Designs'], prompt = '\nWhich sleeping bag would you like?\nType: Marmot, Nemo, or Sierra Designs: ')
                if choice.lower() == 'marmot':
                    purchases.append(marmot_std.cost)
                    shopping_list('Marmot Trestles Elite 30' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'nemo':
                    purchases.append(nemo_std.cost)
                    shopping_list('NEMO Disco Endless Promise 30' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

                if choice.lower() == 'sierra designs':
                    purchases.append(sierra_std.cost)
                    shopping_list('Sierra Designs Night Cap 20' + chr(176) + ' Sleeping Bag')
                    card_balance(gift_card, purchases)

# Product classes for each category of gear
# Each class has an __init__ method to initialize the attributes and a display method to format the output.
# The display method returns a formatted string with the full description of the gear.
# The classes are used to create instances of the gear and display their details.
class Backpacks:
    def __init__(self, style, make, model, capacity, weight, cost):
        self.style = style
        self.make = make
        self.model = model
        self.capacity = capacity
        self.weight = weight
        self.cost = cost

    def display_packs(self):
        full_description = f"{self.style}, {self.make}, {self.model}, {self.capacity}L, {self.weight}lbs: ${self.cost}"
        return full_description.title()

class Tents:
    def __init__(self, style, make, model, person, season, weight, cost):
        self.style = style
        self.make = make
        self.model = model
        self.person = person
        self.season = season
        self.weight = weight
        self.cost = cost

    def display_tents(self):
        full_description = f"{self.style}, {self.make}, {self.model}, {self.person}-person, {self.season}-season, {self.weight}lbs: ${self.cost}"
        return full_description.title()

class Bags:
    def __init__(self, style, make, model, temp, material, fill_power, weight, cost):
        self.style = style
        self.make = make
        self.model = model
        self.temp = temp
        self.material = material
        self.fill_power = fill_power
        self.weight = weight
        self.cost = cost

    def display_bags(self):
        full_description = f"{self.style}, {self.make}, {self.model}, {self.temp} F, {self.material}, {self.fill_power} fill-power, {self.weight} oz: ${self.cost}"
        return full_description.title()

if __name__ == "__main__":
    main()

# FEATURE CHECKLIST
# The 3 required functions are:
# 1. open_image(url1, url2, url3) - Opens images of the selected gear from the web, uses parameters to load images.
# 2. card_balance(gift_card, purchases) - Maintains and displays the running total of the gift card balance, uses conditional statements
# 3. shopping_list(make) - Keeps track of the user's selections in a shopping cart, uses parameters to display the cart contents.

# The program uses classes to represent the different categories of gear: Backpacks, Tents, and Sleeping Bags.
# Each class has an __init__ method to initialize the attributes and a display method to format the output.
# It uses pyinputplus for user input validation and error handling.
# It also includes try/excpet error handling for image loading and user input validation.
# The program also includes a global variable for the gift card balance and a list to keep track of purchases.
# The program ends when the user chooses to exit or when they exceed the gift card balance.
# Image loading is done using the Pillow library, which allows for easy display of images from URLs.
# The program is designed to be user-friendly, with clear prompts and menu options for the user to select from.
