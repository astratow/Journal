from data import MENU, resources, profit
#print(MENU)
#print(resources)

def resources_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients >= resources[item]:

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
    elif choice == "l":
        print(MENU["latte"])
    elif choice == "c":
        print(MENU["cappuccino"])