import art
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True
print(art.logo)
print("Welcome to the OOP cafeteria!, Please take a seat and enjoy!")

while is_on:

    choice = input(f"What would you like to have ({menu.get_items()})?: ").lower()

    if choice == "report":
        print("Welcome Administrator!, this are the resources of the machine and the profit.")
        money_machine.report()
        for i in coffee_maker.resources:
            print(f"{i} : {coffee_maker.resources[i]}")

    elif choice == "off":
        is_on = False

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print(f"Sorry, {choice} is not a valid choice.")