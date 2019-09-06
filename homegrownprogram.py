# Menu of available items including category and price for Homegrown Gill's inventory
menu = {'fruit': {'bananas': {'price': 4, }, 'apples': {'price': 5, }, 'pears': {'price': 5, }, },
        'vegetables': {'beans': {'price': 3, }, 'lettuce': {'price': 4, }, 'carrots': {'price': 5, }, },
        'dairy': {'milk': {'price': 7, }, 'cheese': {'price': 15, }, 'butter': {'price': 10, }},
        'nuts': {'almonds': {'price': 10, }, 'brazil': {'price': 8, }, 'walnuts': {'price': 9, }, },
        'jams': {'blackberry': {'price': 5, }, 'blueberry': {'price': 5, }, 'orange': {'price': 5, }},
        'juices': {'apple': {'price': 5, }, 'orange': {'price': 5, }, 'grape': {'price': 5, }}}

# Empty cart for customer's order
cart = {}

# Loop for main options menu
loop_options = True

# Set delivery cost to 0 for if user wants to have items delivered or pick-up
delivery_cost = 0

# Set name of the user
name = 0

# Loop for order either delivery or pick-up
order = True


# Function for Gill when she adds new items that are available to the menu
def add(food, price):
    try:
        cat_add = input("What kind of food would you like to add?\n"
                        "Fruit\n"
                        "Vegetables\n"
                        "Dairy\n"
                        "Nuts\n"
                        "Jams\n"
                        "Juices\n").lower()
        cat_item = input("What food would you like to add?")
        cost = int(input("What is the price of {}".format(cat_item)))
        try:
            food[cat_add][cat_item] = {price: cost}
        except KeyError:
            print("Enter a Valid Input")
    except ValueError:
        print("Enter a Valid Input")


# Function that prints available items on the menu including new items that Gill adds to the menu
# Allows Gill to add items to her menu
def print_menu(food):
    try:
        for category, a in food.items():

            print(category)

            for fruit, info_item in a.items():
                print(fruit)

                print("price: $", info_item['price'])

            print()

    except ValueError:
        print("Error")


# Function that asks name for delivery and pick-up to output at the end of the program
def info():
    name_info = input("Name: ")
    return name_info


# Function that prints the categories for the items on the menu
def items():
    print("""
---------------------
Item Categories:

Fruit
Vegetables
Dairy
Nuts
Jams
Juices
Back to Options [X]
---------------------
                """)
    type_order = input("What kind of item do you want?").lower()
    return type_order


# Function that lays out the customer's order cart
def print_cart(function):
    print("Your order is:")
    for title, value in function.items():
        print(title.capitalize())
        print("Price per Item: ${}".format(value['price']))
        print("Quantity: {}".format(value['quantity']))
        print("Total Cost for Items: {}".format(value['total cost']))


def repeat():
    repeat_option = int(input("""
1: Another Order
0: Exit
"""))
    while True:
        try:
            if repeat_option == 1:
                cart.clear()
                return True

            elif repeat_option == 0:
                return False

            else:
                print("Invalid Input")
                repeat_option = int(input("""
1: Another Order
0: Exit
"""))
        except ValueError:
            print("Invalid Input")


# Options to purchase items from Homegrown Gill or for Gill or other administrators to update/add to the stock
print("""
=============
Welcome to Homegrown Gill
1: Purchasing
2: Updating Stock
0: Exit
=============""")
# while loop for input if user wants to purchase enter 1, if update stock enter 2, if exit enter 0
# if while loop is equal to 0 program stops, other wise try if 1 -> purchase, if 2 -> update stock
while order:
    try:
        order = int(input("Purchasing or updating inventory?"))
        # If user types 1 -> user wants to purchase products
        if order == 1:
            order = "Purchase"
            break

        # If user types 2 -> user wants to update products on the menu
        elif order == 2:
            order = "Update"
            # If user wants to update products -> have to put in password so only authorised people can update
            # For the purposes of testing and assessment the password is shown. Otherwise
            # in a real world application the password would only be known by authorised people
            password = input("Enter Password: \n"
                             "*Password is: abc123")
            if password == "abc123":
                try:
                    print_menu(menu)
                    add(menu, 'price')
                    print_menu(menu)
                except ValueError:
                    print("Enter a Valid Input")
        elif order == 0:
            print("Please Come Again Soon")
            quit()
        else:
            print("Invalid Input")
    except ValueError:
        print("Enter a Valid Input")


# Delivery or Pickup options
while True:
    try:
        try:
            pic_del = input("""
Pick up (P)
or 
Delivery (D) 
*There is a $3 charge for delivery
""")        # if delivery, ask for name, address, phone number and charge $3 for delivery
            if pic_del[0].lower() == "d":
                print("Delivery")
                name = info()
                address_info = input("Delivery Address: ")
                number_info = int(input("Phone Number: "))
                delivery_cost = 3
                break
            # if pickup, ask for name and charge $0 for delivery cost
            elif pic_del[0].lower() == "p":
                print("Pick up")
                name = info()
                delivery_cost = 0
                break
            else:
                print("Enter a Valid Input")
        except IndexError:
            print("Enter a Valid Input")
    except ValueError:
        print("Enter a Valid Input")

# Main options menu
while loop_options:
    try:
        print("""
Options
=================
1: Add item
2: Remove item
3: View cart
4: View Available Items
5: Check Out
0: Cancel Order [EXIT] 
=================
        """)
        option = int(input("Enter an option: "))
        # if user chooses 1, add items menu. Print category of items
        if option == 1:
            fruit_loop = True
            while fruit_loop:
                try:
                    try:
                        order_type = items()
                        # if 1st letter f, category = fruit
                        if order_type[0] == "f":
                            much_many = "many"
                            order_type = "fruit"
                            print(order_type)
                        # if 1st letter v, category = vegetables
                        elif order_type[0] == "v":
                            order_type = "vegetables"
                            much_many = "many"
                            print(order_type)
                        # if 1st letter d, category = dairy
                        elif order_type[0] == "d":
                            order_type = "dairy"
                            much_many = "much"
                            print(order_type)
                        # if 1st letter n, category = nuts
                        elif order_type[0] == "n":
                            order_type = "nuts"
                            much_many = "many"
                            print(order_type)
                        # if 1st and 2nd letter ja, category = jams
                        elif order_type[0:2] == "ja":
                            much_many = "much"
                            order_type = "jams"
                            print(order_type)
                        # if 1st and 2nd letter ju, category = juices
                        elif order_type[0:2] == "ju":
                            order_type = "juices"
                            much_many = "much"
                            print(order_type)
                        # if x goes back to main options menu
                        elif order_type[0].lower() == "x":
                            break

                        else:
                            print("Enter a Valid Input")
                            break
                        # prints the items and prices in the chosen category
                        for item_food in menu[order_type]:
                            print(item_food)
                            for price_food in menu[order_type][item_food]:
                                print(price_food, ':$', menu[order_type][item_food][price_food])
                        # input item from the category
                        item_add = input("What kind of {}?".format(order_type))
                        if item_add in menu[order_type]:
                            # how many items
                            quantity = int(input("How {} {} do you want".format(much_many, item_add)))
                            # quantity of item input has to above 0
                            if quantity < 1:
                                print("Please Enter a Quantity above 0")
                                break
                            # layout for cart
                            price_item = menu[order_type][item_add]['price'] * quantity
                            cart[item_add] = {'price': menu[order_type][item_add]['price'], 'quantity': quantity,
                                              'total cost': (menu[order_type][item_add]['price'] * quantity)}

                        else:
                            print("Item not on the menu")

                    except ValueError:
                        print("Enter a Valid Input")
                except IndexError:
                    print("Enter a Valid Input")
        # Option 2 from main menu either remove an item or change the quantity
        elif option == 2:
            print("""
---------------------
Remove From Cart [X]
1: Remove an item
2: Change quantity
0: Back to options
---------------------
""")
            # Item user wants to remove
            while True:
                try:
                    remove = int(input("Would you like to remove an item or quantity?"))
                    if remove < 0:
                        print('Enter a Valid Input')
                        continue
                    break
                except TypeError:
                    print("This is a string")

            while remove != 0:
                try:
                    # remove option 1 --> remove an item from your cart
                    if remove == 1:
                        print("Remove item")
                        item_remove = input("Enter an item: ")
                        if item_remove in cart:
                            # cart.remove(item_remove)
                            cart.pop(item_remove)
                            break
                        else:
                            print("Enter a Valid Item")
                            break
                    # remove option 2 --> change the quantity of an item in your cart
                    elif remove == 2:
                        quantity = 0
                        print("Update quantity")
                        item_change = input("What item change")
                        quantity_change = int(input("What will be the new quantity"))
                        if quantity_change < 0:
                            print("Please Enter a Quantity above 0")
                            break
                        if item_change in cart:
                            cart[item_change]['quantity'] = quantity_change
                            break
                        else:
                            print("Enter a Valid Item")
                            break

                    else:
                        print("Options Menu")
                        break
                except ValueError:
                    print("Enter a Valid Input")
        # Main options --> option 3: print cart
        elif option == 3:
            print_cart(cart)
        # Main options --> options 4: print available items (items in dictionary "Menu")
        elif option == 4:
            for x in menu:
                print(x)
                for y in menu[x]:
                    print(y, ':', menu[x][y])
        # Main options --> option 5: checkout,
        # gives user packaging options for their items in the cart --> paper bags/boxes
        elif option == 5:
            print_cart(cart)
            packaging_option = int(input("""
-----------------
Packaging Options
1: Boxes
2: Paper Bag ($1)
0: Back to options            
-----------------           
"""))
            packaging_loop = True
            while True:
                # Packaging = Boxes
                if packaging_option == 1:
                    try:
                        # Prints total items in the cart and calculates how many boxes are
                        # needed for that amount of items
                        last_quantity = 0
                        for item, info in cart.items():
                            total_quantity = info['quantity'] + last_quantity
                            last_quantity = total_quantity
                        print("Total Items: {}".format(last_quantity))
                        # if total quantity is smaller than 10
                        if int(last_quantity) < 10:
                            box_num = int(last_quantity / 2)
                            print("{} Small Box".format(box_num))
                            print_cart(cart)
                            print("Delivery Charge ${}".format(delivery_cost))
                            print("{} Thank You For Shopping With Us".format(name))
                            loop_options = repeat()
                            break
                        # if total quantity is smaller than 25
                        elif int(last_quantity) < 50:
                            box_num = int(last_quantity / 5)
                            print("{} Medium Box".format(box_num))
                            print_cart(cart)
                            print("Delivery Charge ${}".format(delivery_cost))
                            print("{} Thank You For Shopping With Us".format(name))
                            loop_options = repeat()
                            break
                        # if total quantity is smaller than 100
                        elif int(last_quantity) > 51:
                            box_num = int(last_quantity / 10)
                            print("{} Large Box".format(box_num))
                            print_cart(cart)
                            print("{} Thank You For Shopping With Us".format(name))
                            print("Delivery Charge ${}".format(delivery_cost))
                            loop_options = repeat()
                            break
                        elif last_quantity == 0:
                            print("No items in cart")

                        else:
                            print("AGAIN")

                    except ValueError:
                        print("Enter a Valid Input")
                # Packaging = Paper bags
                elif packaging_option == 2:
                    print("Paper Bags: $1 Each")
                    # Input how many paper bags you want
                    paper_bags = int(input("How many paper bags do you want?"))
                    if paper_bags < 1:
                        print("Please Enter a Quantity above 0")
                        break
                    # Prints order cart, any delivery charge, total price of paper bags, thanks user for shopping
                    print_cart(cart)
                    print("Delivery Charge ${}".format(delivery_cost))
                    print("Total price for paper bags: $", paper_bags * 1)
                    print("{} Thank You For Shopping With Us".format(name))

                    loop_options = repeat()
                    break

                elif packaging_option == 0:
                    break

                else:
                    print("Enter a Valid Input")
                    break

        elif option == 0:
            print("Please Come Again")
            break

        else:
            print("Enter a Valid Input")
            option = int(input("\nEnter an option: "))

    except ValueError:
        print("Enter a Valid Input")
