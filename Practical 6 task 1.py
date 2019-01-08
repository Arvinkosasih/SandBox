def main():
    x = int(input("Enter x value "))
    y = int(input("Enter y value "))
    doMath(x,y)

def doMath(lhs, rhs):
    sum = lhs + rhs
    diff = lhs - rhs
    product = lhs * rhs
    quotient = lhs / rhs
    print("Sum: "+ str(sum) + " diff: "+ str(diff)+ " product: " + str(product)+ " quotient: " +str(quotient))

main()
