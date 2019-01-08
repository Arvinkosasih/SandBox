def stock():
    baseStock = int(input("Enter your current stock "))
    newStock = int(input("Enter your new stock "))
    soldStock = int(input("Enter the amount of stock that is sold "))
    remainStock = baseStock + newStock - soldStock
    print("stock amount at the end of day = "+ str(remainStock))
stock()
