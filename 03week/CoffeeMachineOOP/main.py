from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item = MenuItem()

#money_machine.report()
#coffee_maker.report()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like to drink:\n({options})\n")
    if choice == "off":
        print("Thank you for using Coffee Machine Simulator. Good Bye!")
        on = False
    elif choice == "r":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
