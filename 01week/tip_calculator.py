#Tip calculator
print("Welcome to tip calculator")
bill = float(input("How much is bill in total?\n"))
numberOfPeople = int(input("How many people have food?\n"))
tipPercent = float(input("How much % would you like to tip?\n"))
share = (tipPercent/100 + 1) * bill / numberOfPeople
shareFinal = round(share, 2)
print (f"Each person needs to pay ${shareFinal}")
