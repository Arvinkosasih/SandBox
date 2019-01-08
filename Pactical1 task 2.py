
sales = float(input("Enter sales: $"))

if sales > 999:
    bonus = sales * 0.15
    print("Bonus: $" + str(bonus))
    print("TOTAL : $" + str(bonus + sales))
if sales < 1000:
    bonus = sales * 0.1
    print("Bonus: $" + str(bonus))
    print("TOTAL : $" + str(bonus + sales))


