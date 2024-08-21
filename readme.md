Python assignment 1

Overview:
Designing an interactive ordering system from a food truck menu, using the skills you've learned in Python so far.
Files - menu.py
Repo name - python-challenge--1

Variables used:

menu - Dictionary for the list of items
customer_order - list to hold customer order
menu_items - to select the items
menu_category - this is a digit and int value within the range of selections given in menu list. 
num_item_spaces = calculates the number of space to print result in the desired pattern.
The total - this will calculate the price of the menu item times the quantity selected and will print it as a grand total. 

Code Source: 

Given starter file and building the logic on that. Partial idea/logic for line 143 was given by the Instructor.

Results:

An order list is initialized and user is prompted for their menu item selection.
User input is checked if it is a number or not if not error message will be printed. 
If-else statement is used to check if menu_selection is in the menu_items, if not error message is printed. 
The item name of the customer's selection is taken from the menu_items dict and prompted for quantity
A match case statement is used to check if the customer would like to keep ordering or they are done with an option of 'y' or 'n'. 
A for loop is used to loop the order list. 
Space strings are created using string multiplication
The customers order is printed with item name, price and quantity in the desired format. 
List comprehension is used to calculate the total price of the order. 
The total price is then printed. 




