def airlineMenu(userNameInput):
    print("What can we do for you?")
    print("(I) for information")
    print("(O) to order ticket")
    print("(E) to exit")
    userInput = input(">")
    if userInput == "E" or userInput == "e":
        print("Thank you for visitng our airline services, we hope to see you again!")
    else:
        if userInput == "I" or userInput == "i":
            print(
                " Thankyou for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.")
            airlineMenu(userNameInput)
        else:
            if userInput == "O" or userInput == "o":
                totalPrice(userNameInput)
            else:
                print("You enter the wrong menu choice, please try again..")
                airlineMenu(userNameInput)


def getAge():
    print("Please enter your age/other traveller age...")
    print("How old are you/other traveller? , below 16 years old will receive 50% discount for child fare")
    age = int(input(">"))
    while age < 0 or age > 120:
        print("Invalid input, please try again...")
        age = int(input(">"))
    if age <= 16:
        ageAboveBelow = 2
    else:
        ageAboveBelow = 1

    return ageAboveBelow


def orderForWhoDecision(userNameInput):
    print("Do you want to oder the ticket for yourself or someone else?")
    print("(M) for myself")
    print("(OT) for other traveller")
    userInput2 = input(">")
    if userInput2 == "M" or userInput2 == "m":
        custInput = userNameInput
    else:
        if userInput2 == "OT" or userInput2 == "ot":
            print("Please enter the other traveller's name")
            custInput = input(">")
        else:
            print("You enter the wrong menu choice, please try again..")
            orderForWhoDecision(userNameInput)

    return custInput


def seatType():
    print("Which type of seat do you want?")
    print("1. (W)indow $30")
    print("2. (A)isle $20")
    print("3. (M)iddle $0")
    userInput4 = input(">")
    if userInput4 == "W" or userInput4 == "w":
        ticketPrice3 = 30
    else:
        if userInput4 == "A" or userInput4 == "a":
            ticketPrice3 = 20
        else:
            if userInput4 == "M" or userInput4 == "m":
                ticketPrice3 = 0
            else:
                print("You enter the wrong menu choice, please try again..")
                seatType()

    return ticketPrice3


def ticketCostOneTwoWay():
    print("Please select your destination:")
    print("1. (P1) Perth 1 way ticket for $120")
    print("2. (P2) Perth return ticket for $200")
    print("3. (C1) Cairns 1 way ticket for $130")
    print("4. (C2) Cairns return ticket for $240")
    print("5. (S1) Sydney 1 way ticket for $150")
    print("6. (S2) Sydney return ticket for $280")
    userInput3 = input(">")
    if userInput3 == "P1" or userInput3 == "p1":
        ticketPrice = 120
    else:
        if userInput3 == "P2" or userInput3 == "p2":
            ticketPrice = 200
        else:
            if userInput3 == "C1" or userInput3 == "c1":
                ticketPrice = 130
            else:
                if userInput3 == "C2" or userInput3 == "c2":
                    ticketPrice = 240
                else:
                    if userInput3 == "S1" or userInput3 == "s1":
                        ticketPrice = 150
                    else:
                        if userInput3 == "S2" or userInput3 == "s2":
                            ticketPrice = 280
                        else:
                            print("You enter the wrong menu choice, please try again..")

    return ticketPrice


def ticketFareCost():
    print("Which type of fare do you want?")
    print("1. (B) for business $130")
    print("2. (E) for economy $50")
    print("3. (F) for frugal $0")
    userInput3 = input(">")
    if userInput3 == "B" or userInput3 == "b":
        ticketPrice2 = 130
    else:
        if userInput3 == "E" or userInput3 == "e":
            ticketPrice2 = 50
        else:
            if userInput3 == "F" or userInput3 == "f":
                ticketPrice2 = 0
            else:
                print("You enter the wrong menu choice, please try again..")
                ticketFareCost()

    return ticketPrice2


def totalPrice(userNameInput):
    ticketPrice = ticketCostOneTwoWay()
    ticketPrice2 = ticketFareCost()
    ticketPrice3 = seatType()
    ageAboveBelow = getAge()
    totalCost = (ticketPrice + ticketPrice2 + ticketPrice3) / ageAboveBelow
    print("The total cost of the ticket is",totalCost)


def userNameInput():
    print("Please input your name...")
    userNameInput = input(">")

    return userNameInput



userNameInput = userNameInput()
print("Welcome to our airline services, " + userNameInput + ". What can we do for you today?")
airlineMenu(userNameInput)
