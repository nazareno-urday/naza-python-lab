MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(drink):
    """Checks if there is enough resources left in the machine"""
    for i in drink:
        if drink[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def process_coins():
    """Returns the total money paid"""
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def transaction_successful(payment, drink):
    """Returns True if the transaction was successful"""
    if payment >= drink["cost"]:
        change = round(payment - drink["cost"], 2)
        global profit
        profit += drink["cost"]
        print(f"Here is your change: ${change}")
        return True

    else:
        print("Sorry there is not enough money. Money refunded")
        return False

def make_coffe(decision, ingredients):
    """Deducts the resources form the machine and delivers coffee"""
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {decision}. Enjoy! ")

is_on = True

while is_on:

    decision = input("What would you like to have? (espresso, latte, cappuccino): ").lower()

    if decision == "off":
        is_on = False

    elif decision == "report":
        print("The resources of the coffe machine are:")
        print(f"Water left: {resources['water']} ml")
        print(f"Milk left: {resources['milk']} ml")
        print(f"Coffee left: {resources['coffee']} g")
        print(f"The profit is ${profit}")

    else:
        drink = MENU[decision]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink):
                make_coffe(decision, drink["ingredients"])

        """ENJOY UR COFFE ;)"""