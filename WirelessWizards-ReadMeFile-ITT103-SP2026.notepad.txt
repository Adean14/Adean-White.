Authors: Adean White, Romando Bradford
Date Created: March 31, 2026
Course: ITT103
GitHub Public URL to Code:https://github.com/Adean14/Adean-White


Program functionalities:

Lines 3 - 24: shows the products that the store sells

Lines 26 - 32: initializes an empty dictionary to manage customer cart and items in stock

Lines 36 - 41: check quantity of product in inventory and tell if product is not available

Lines 44 - 48: error message check for handling quantity input, if customer inputs more than the amount available

Lines 51 - 53: error message if 0 was selected as the quantity, quantity has to be >0

Lines 55 - 57: error message if the amount of goods the customer needs, is more than the amount in stock.

Lines 59 - 62: once user(customer) input has been validated, selected items will be added to customer's basket

Lines 65 & 66: will update quantity of items in stock once the items are added to cart

Lines 71 - 78: function to allow customers to remove items before checkout, which will restock back to inventory

Lines 87 - 93: error message that will be showed in cart is empty

Lines 100 - 108:  loop iterates through each product in the customer's cart, retrieving the unit price from the product dictionary and purchased quantity from the cart, multiplying them (items in cart) to calculate the line total, adding it to the grand total.

Lines 112 - 117:  before the payment process, checks are done to confirm items are in cart, if no item in cart, then a message is printed and return function will end the loop which in turn avoids any errors 

Lines 119 - 120: calculates the items in cart

Lines 122 - 124: calculate the 5% discount if it applies

Line 126 & 126: calculates the 10% tax, the discount and then 

Lines 130 - 134: print information once calculation is completed

Lines 142 - 144:  error message if customer makes payment less than the grand total

Line 146: calculates customer change

Line 148: the receipt function to print the official transaction record

Line 150: cart is then emptied to finalize the sale and prepare for the next customer

Lines 156 - 160: display all purchase items and additional transaction details for receipt

Lines 162 - 171: information that will be shown on the receipt

Lines 175 - 180: display if stock is low when item count in stock is less than 5

Lines 185 - 195: infinite loop to allow multiple transactions (Mian program loop)

Lines 199 - 218: manage customer choices

Lines 220 - 222: if an item other than what's listed is chosen


Purpose of the Program:
A Point of Sale (PoS) system for a small retail store.

How to run it:
Using PyCharm or Google Colab install on the store system

Required modifications:
You can add items to the products list over time

Assumptions or limitations regarding its operation:
- There is no indication to use whether JMD or USD
- The program has to be exited to add additional items to the product list

