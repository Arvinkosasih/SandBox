def main():
    import random
    for i in range(1):
        wind = random.randint (0,255)
        print("Cyclone speed(km/h):",wind)
        cycloneStatus (wind)

def cycloneStatus(wind):
    if wind < 119:
        print("It is not yet a cyclone")
    elif wind >= 119 and wind <= 153:
        print("Cat1")
    elif wind >= 154 and wind <= 177:
        print("Cat2")
    elif wind >= 178 and wind <= 208:
        print("Cat3")
    elif wind >= 209 and wind <= 251:
        print("Cat4")
    else:
        print("Cat5")

main()