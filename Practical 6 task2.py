def main():
    distance = 500
    fuelCon = 8
    fuel(distance,fuelCon)

def fuel(distance, fuelCon):
    fuelNeeds = (distance * fuelCon)/100
    print("Fuel needed is "+ str(fuelNeeds))

main()