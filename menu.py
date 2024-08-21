###############################################
#    Assignment 2 - AI boot camp              #
#                                             #
###############################################

# list of Menu items
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
#Creating empty list for customer order
customer_orders = []
print("Welcome to the variety food truck.")
place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1
    menu_category = input("Type menu number: ")
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            menu_selection = input("Type menu number: ")
            if menu_selection.isdigit(): 
                print(menu_items.keys())
                name = menu_items[int(menu_selection)]["Item name"] + " $" + str(menu_items[int(menu_selection)]["Price"])
                print(f"You selected " + name)
                quantity = input(f"How many " +  name +" would you like to order? (Default is 1)")
                if not quantity.isdigit(): 
                    quantity = 1
                customer_orders.append({
                    "Item Name":  menu_items[int(menu_selection)]["Item name"],
                    "Price": menu_items[int(menu_selection)]["Price"],
                    "Quantity": quantity
                })  
            else:
                print("Item selected does not exist")
                
            
            getCorrectInput = True
            while getCorrectInput:
                keep_ordering = input("Would you like to continue ordering? ")
                match keep_ordering.lower():
                    case 'y':
                        place_order = True
                        getCorrectInput = False
                    case 'n':
                        place_order = False
                        print("Thank you for your order")
                        getCorrectInput = False
                    case _:
                        print("Invalid input Y/N only")

        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")
#testing to see what customer_order is saving and printing
#customer_orders=[{'Item Name': 'Burger - Beef', 'Price': 8.49, 'Quantity': '2'}, {'Item Name': 'Apple', 'Price': 0.49, 'Quantity': '3'}, {'Item Name': 'Rice pudding', 'Price': 4.99, 'Quantity': '4'}, {'Item Name': 'Granola bar', 'Price': 1.99, 'Quantity': 1}]
#print(customer_orders)
total_price = []
print("Item name                     \t Price     Quantity")
print("----------------------------|---------|----------")
for order in customer_orders:
    num_of_char = 28 - len(order["Item Name"])
    num_of_char = " " * num_of_char

    print(f'{order["Item Name"]}{num_of_char}| {order["Price"]}    |  {order["Quantity"]}')
    # print(order["Item Name"])
    # print(order["Price"])
    # print(order["Quantity"])
    total_price.append(float(order["Price"])*float(order["Quantity"]))
print("                          ")
print("**************************")
print("Total Price $",sum(total_price))
print("**************************")
print("$"+"{:.2f}".format(sum(total_price)))

