"""input name and print odd characters"""

name=input("Enter name >>> ")

#Check that name is not blank
while len(name)<=0:
    print("Name is blank, please enter again")
    name=input("Enter name >>> ")
#print odd characters is the name
print(name[::2])
#print idd characters in the name
for i in range(0,len(name),2):
    print(name[i],end='')

