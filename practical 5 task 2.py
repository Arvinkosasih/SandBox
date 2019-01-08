houseCost = int(input("Enter the price of the house "))
landSize = int(input("Enter the land size "))
landCost = int(input("Enter the cost of the land/square "))
totalLandCost = landCost * landSize
totalCost = totalLandCost + houseCost
print("The total price is " + str(totalCost))
