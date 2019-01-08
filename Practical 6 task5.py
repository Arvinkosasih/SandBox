def main():
    hourlyRate = float(24.95)
    timeWork = int(input("How many hour(s) does your employee work? "))
    finalPayment = pay(hourlyRate,timeWork)
    print(finalPayment)

def pay(hourlyRate, timeWork):
    totalPay = hourlyRate * timeWork
    #print("you pay your employee : $" +str(totalPay))
    return totalPay

main()
