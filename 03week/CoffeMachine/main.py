from data import MENU, resources
print(MENU)
print(resources)
on = True
while on:
    choice = input(" What would you like? \n(e)spresso\n(l)atte\n(c)appuccino\n")
    if choice == "off":
        on = False
    elif choice == "r" or choice == "report":
        for key in resources:
            print(key, resources[key])
