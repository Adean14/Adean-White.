# Shopping cart dictionary
# Centralized dictionary storing ALL products with current price and available stock
products = {
    "rice": {"price": 200, "stock": 1000},
    "flour": {"price": 190, "stock": 1100},
    "bread": {"price": 550, "stock": 1200},
    "sugar": {"price": 190, "stock": 900},
    "cornmeal": {"price": 170, "stock": 1000},
    "chicken": {"price": 1800, "stock": 2500},
    "sweet corn": {"price": 470, "stock": 1300},
    "almond milk": {"price": 780, "stock": 1500},
    "cow's milk": {"price": 500, "stock": 1000},
    "butter": {"price": 450, "stock": 1000},
    "cooking oil": {"price": 450, "stock": 1100},
    "pepsi": {"price": 300, "stock": 2000},
    "all purpose seasoning": {"price": 350, "stock": 1500},
    "chicken seasoning": {"price": 350, "stock": 2500},
    "fish seasoning": {"price": 300, "stock": 1000},
    "wata": {"price": 200, "stock": 3000},
    "coffee": {"price": 550, "stock": 1000},
    "bleach": {"price": 400, "stock": 1300}
}
# Initializes an empty dictionary to manage customer cart and items in stock
cart = {}
def display_products():
  print("\nAvailable Products: ")
  for item in products:

      print(item, "Price: ", products[item]["price"], "Stock: ",  products[item]["stock"])



def add_to_cart():
  product= input("Enter product name: ").lower()
    # Checking quantity of product in inventory
  if product not in products:
    print("Product is not available!")
    return

# Error check for handling quanitity input
  try:
    quantity=int(input("Enter quantity: "))
  except:
    print ("Invalid quantity")
    return
# Order validation: the next two if statements is used to confirm a valid input
# Regarding the quantity of an item
  if quantity <=0:
    print ("Quantity must be greater than 0")
    return

  if quantity > products[product]["stock"]:
    print ("Not enough stock available")
    return
# Once user input has been validated, selected items will be added to customer's
# basket
  if product in cart:
    cart[product] += quantity
  else:
    cart[product] = quantity

  #This will update quanity of items in stock once the items are added to cart
  products[product]["stock"] -= quantity
  print(product, "Added to cart")

# The purpose of the below function is to allow customers to remove items before checkout
# which then automatically restore stock to inventory when removed and
# prevent inventory loss from cart abandonment.
def remove_from_cart ():
  product = input("Enter product to remove: ").lower()
# RESTOCK: Return quantity back to inventory
  if product in cart:
    products[product]["stock"] += cart[product]
    # Remove from cart completely
    del cart[product]
    print("Item removed")

  else:
    print("Item not in cart.")

# Error Checking
# this block of code determines whether the shopping cart dictionary is empty,
# which would cause the loop below to crash. if it is, it writes
#"Your cart is empty!" and uses return to end the function right away.
def view_cart_summary():#Display item(s) in costumer's cart and total cost.
    if not cart:
      print("Cart is empty.")
      return

    print("\nShopping Cart: ")
    total = 0
#The 'for item in cart' loop iterates through each product in the customer's
#shopping cart, retrieving the unit price from the product dictionary and the
#purchased quantity from the cart, multiplying them to calculate the line total,
#adding it to the running grand total, and printing each item's details. After
#all items have been processed, it displays the final subtotal, transforming
#cart data into a professional, customer-readable summary.
    for item in cart:
      price = products[item]["price"]
      quantity = cart[item]
      item_total = price*quantity
      total += item_total

      print(item, "-Qty: ", quantity, "Total: ", item_total)

    print("Subtotal: ", total)
#Before the payment process, checks are done to confirm if items are in cart,
#If no item then a message is print and the return function will end the loop
#and avoiding any errors
def checkout():
    if not cart:
      print("Cart is empty.")
      return

    subtotal = 0
#Calculation of the items checkout
    for item in cart:
        subtotal += products[item]["price"] * cart[item]# loops through each item in cart while multiplying price by quantity

    discount = 0 #Calculation for discount if applies
    if subtotal > 5000:
      discount = subtotal * 0.05

    tax = (subtotal - discount) * 0.10

    total = subtotal - discount + tax
#print information once calculation is complete
    print("\n====CHECKOUT====")
    print("Subtotal", subtotal)
    print("Discount", discount)
    print("Tax (10%) :", tax)
    print("Total", total)

    try:
      payment = float(input("Enter payment amount.: "))#print payment as decimal
    except ValueError:#error checking, verify nun-numerical value
      print("Invalid payment")
      return

    if payment < total: #If users makes a payment less than the grand total amount
      print("Insufficient payment.")
      return

    change = payment - total #calculates the customer's change

    generate_receipt(subtotal, discount, tax, total, payment, change) #Use the receipt function to print the official transaction record

    cart.clear() #The cart is then emptied to finalize the sale and prepare for the next customer

def generate_receipt(subtotal, discount, tax, total, payment, change):
    print("\n====RECEIPT====")
    print("------------------------")

    # Display all purchase items and additional transaction details for receipt
    for item in cart:
        price = products[item]["price"]
        quantity = cart[item]
        print(item, "x", quantity, "=", price * quantity)

    print("------------------------")
    print("Subtotal", subtotal)
    print("Discount", discount)
    print("Tax (10%):", tax)
    print("Total", total)
    print("Paid", payment)
    print("Change", change)

    print("\nTHANK YOU FOR SHOPPING WITH US!")
    print("===============================")

# Function to display low stock alert.
# display "low stock alert" if item count int stock is less than 5
def low_stock_alert():
    print("\nLow Stock Alert")
    for item in products:
            # Check if stock is less than 5
            if products[item]["stock"] < 5:
                print(item, "Stock is low!: ", products[item]["stock"])

# Main program loop.
# Infinite loop to allow multiple transactions

while True:
  print("\nWELCOME TO BEST BUY RETAIL STORE!")
  print("\n====POS MENU====")
  print("1. View Products")
  print("2. Add to Cart")
  print("3. Remove from Cart")
  print("4. View Cart Summary")
  print("5. Checkout")
  print("6. Low Stock Alert")
  print("7. Exit")

  choice = input("Enter Choice: ")

# Menu Option
# manage user choices
  if choice == "1":
    display_products()

  elif choice == "2":
    add_to_cart()

  elif choice == "3":
    remove_from_cart()

  elif choice == "4":
    view_cart_summary()

  elif choice == "5":
    checkout()

  elif choice == "6":
    low_stock_alert()

  elif choice == "7":
    print("Exiting System...")
    # Exit the loop and end program.
    break
  else:
    print("Invalid Choice!")#If a number other than what's listen is chosen