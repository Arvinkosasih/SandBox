def main():
    discount = 0.2
    productPrice = int(input("Enter product price "))
    discounted = calDiscount(productPrice, discount)
    print(discounted)

def calDiscount(productPrice, discount):
    discount = productPrice - (productPrice * discount)
    return discount

main()
