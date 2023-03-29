"""
Jake See
3/28/2023
Coffee Machine Project 
"""

MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50, 
            "milk" : 0,
            "coffee": 18,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk": 100, 
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 600,
    "milk" : 350,
    "coffee": 180
}

def is_resource_sufficient(order_ingredients):
    "checks ingredient amounts vs remaining resources in the coffee machine. returns false if there is not enough resources"
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """ Returns the total amount of money based on coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_trainsaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if it isnt"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}.")
        global profit 
        profit += drink_cost
        return True
    else: 
        print("Sorry, that is not enough money. Money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """ Deduct the correct amount of ingredient based off of which drink is chosen"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):\n ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_trainsaction_successful(payment, drink["cost"]): 
                make_coffee(choice, drink["ingredients"])





