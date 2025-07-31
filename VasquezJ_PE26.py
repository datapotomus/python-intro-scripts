# Program produces a product list and allows updating of product quantity

import pyinputplus as pyip

def main():  # Main function that lists product info and quantity, prompts for updates
    print('PRODUCT LIST')
    backpack = HikeGear('Osprey 60L Backpack',320.63, 15)
    sleeping_bag = HikeGear('Marmot 20F Sleeping Bag', 250.98, 5)
    hike_shoe = HikeGear('Altra Lonepeak Hiking Shoe', 150.75, 8)
    backpack.display_info()
    sleeping_bag.display_info()
    hike_shoe.display_info()

    # Updating product quantites
    update = pyip.inputChoice(['y', 'n'], prompt ='\nWould you like to update any product quantities? Y or N: ')
    if update.lower() == 'y':
        item_update = pyip.inputNum('Item to Update:\nType 1: Backpack\nType 2: Sleeping Bag\nType 3: Hiking Shoe\nENTER SELECTION: ', min=1, max=3)
        if item_update == 1:
            new_qty = pyip.inputNum('--Enter the new quantity?  ')
            backpack = HikeGear('Osprey 60L Backpack',320.63, new_qty)
            backpack.update_quantity(new_qty)
        if item_update == 2:
            new_qty = pyip.inputNum('--Enter the new quantity?  ')
            sleeping_bag = HikeGear('Marmot 20F Sleeping Bag', 250.98, new_qty)
            sleeping_bag.update_quantity(new_qty)
        if item_update == 3:
            new_qty = pyip.inputNum('--Enter the new quantity?  ')
            hike_shoe = HikeGear('Altra Lonepeak Hiking Shoe', 150.75, new_qty)
            hike_shoe.update_quantity(new_qty)
    else:
        print('--No products were updated--')


class HikeGear:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f'Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}')

    def update_quantity(self, new_qty):
        print(f'\nUpdating quantity for {self.name}... ')
        print(f'Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}')


if __name__ == "__main__":
    main()
