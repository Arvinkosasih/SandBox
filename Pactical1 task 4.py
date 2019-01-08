print("Welcome to Shop Calculator")
num = int(input("Enter the number of items "))
while(num<=0):
    print("Invalid Value, please enter positive number only!")
    num = int(input("Enter the number of items "))

total = 0.0
for i in range(1, num+1,1):
    price=float(input("Enter price for item "))
    total+=price
if (total>=100.0):
    total=0.9*total
print("The total of all items purchased is ", total)