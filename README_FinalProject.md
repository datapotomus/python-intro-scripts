# Backpacking Gear Gift Card Program

## Program’s Purpose

This script presents the user with a $1000 gift card they can use to buy outdoor gear. The user is presented with 3 categories of outdoor gear: Backpacks, Tents, and Sleeping Bags. Within each category, the user can pick from Ultralight and Standard gear.

The script keeps track of the gift card balance in real-time, deducting the cost of selected gear. A warning is given if the user is about to exceed their gift card balance and allows them to continue shopping past the balance or quit shopping. The script will keep track of the debt balance incurred in real-time.

## Notable Features

  * The script gives the user the option to load images directly from the web as an aid to the gear they may purchase.
  * A real-time balance is given to the user with every purchase.
  * The user is warned when they are about to exceed the gift card balance.

## How To Run It

This is a Python script. Python needs to be installed on your system to run the script. The following Python modules need to be installed to run the script:

  * Pillow (PIL Fork): opens and displays images
  * requests: downloads images from the web
  * PyInputPlus: handles user input validation
  * sys: system exit


They can be installed using pip:
pip install Pillow
pip install PyInputPlus
pip install requests
```

## Features Included

  * Manages a gift card with $1000 balance, tracks the balance in real-time
  * 3 outdoor gear categories: Backpacks, Tents, Sleeping Bags
  * Gear styles within the Categories: Ultralight and Standard
  * Displays Product Information: make, model, capacity/person/temp rating, weight, and cost
  * Gift card balance warning: Alerts user they are about to exceed their card balance
  * Images: can load images from the web of products
  * Interactive user menu: several interactive menus for user to make choices. PyInputPlus provides user input validation along with try/except blocks.
  * Exit option: user can exit out of shopping experience and is provided with a remaining card balance or amount due.

## Special Notes or Instructions

  * The script uses Pillow’s `Image.show()` method, which will open images in your operating system's default image viewer. New windows will pop up to display each image. User will have a choice to open images or not.
  * An active internet connection is needed to open product images. The script will print an apology message if images are not able to load; script will continue to function otherwise.
  * The `open_image` function temporarily saves the downloaded image as `img.jpg.` in the same directory as the script. This file is overwritten with each new image.