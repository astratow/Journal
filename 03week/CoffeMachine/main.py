from data import MENU, resources, profit
#print(MENU)
#print(resources)

def resources_check(order_ingredients):
    """Returns True if order can be made or False if not enough ingredients"""
    #resources_ok = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            #resources_ok = False
            return False
    return True
def process_coins():
    """Returns total inserted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters:\n")) * 0.25
    total += int(input("How many dimes:\n")) * 0.1
    total += int(input("How many nickles:\n")) * 0.05
    total += int(input("How many pennies:\n")) * 0.01
    return total

def transaction_check(money_received, drink_cost):
    """Returns True if transaction accepted or False not enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Please wait for refund.")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

on = True
while on:
    choice = input(" What would you like? \n(e)spresso\n(l)atte\n(c)appuccino\n").lower()
    if choice == "off":
        on = False
    elif choice == "r" or choice == "report":
        for key in resources:
            print(key, ":", resources[key])
        print(f"money : ${profit}")
    elif choice == "e":
        print(MENU["espresso"])
        drink = MENU["espresso"]
        if resources_check(drink["ingredients"]):
            payment = process_coins()
            transaction_check(payment, drink["cost"])
            make_coffee("espresso", drink["ingredients"])
    elif choice == "l":
        print(MENU["latte"])
        drink = MENU["latte"]
        if resources_check(drink["ingredients"]):
            payment = process_coins()
            transaction_check(payment, drink["cost"])
            make_coffee("latte", drink["ingredients"])
    elif choice == "c":
        print(MENU["cappuccino"])
        drink = MENU["cappuccino"]
        if resources_check(drink["ingredients"]):
            payment = process_coins()
            transaction_check(payment, drink["cost"])
            make_coffee("cappuccino", drink["ingredients"])
    else:
        print("Incorrect choice.")