"""
Course: CS246
Author: <Brigham Valentine>

Description:
  <A program to help with meal planning>
"""
meals = []
items = []
prices = []
def menu():
    print("These are the options for your meal plan:\n")
    print("Add a meal for your meal plan: a")
    print("Add shopping list items: s")
    print("Display your meal plan: d")
    print("Leave your meal plan: q")
    menuSelect()
    
def menuSelect():
    choice = input("> ")
    if choice == "a":
        add()
    elif choice == "s":
        shopping()
    elif choice == "d":
        display()
    elif choice == "q":
        return 0
    else:
        print("please choose a correct key")
        print()
        print()
        menu()

def add():
    meal = input("Enter the name of your meal: ")
    meals.append(meal)
    menu()
        
def shopping():
    item = input("What would you like to add to your shopping list: ")
    items.append(item)
    price = float(input("How much does this item cost: "))
    prices.append(price)
    menu()
   
def display():
    count = 1
    total = 0
    for i in range(len(prices)):
        total += prices[i]
        
    print( "{:*^40}".format("Meal Plan"))
    for i in range(len(meals)):
        print("{} {} {:<34} {}".format("*", count, meals[i], "*"))
        count += 1
    count2 = 1
    print( "{:*^40}".format("Shopping List"))
    for i in range(len(items)):
        print("{} {} {:>22} {:>10} {:<6}".format("*", count2, items[i], prices[i], "*"))
        count2 += 1
    print("{} {} {:>29} {:>2}".format("*", "Total", total, "*"))
        
    print("*" * 40)
    menu()
        
    
menu()
    

