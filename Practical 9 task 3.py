def main():
    pal = input("Input string : ")
    pal = pal.casefold()
    revpal = reversed(pal)
    if list (pal) == list (revpal):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

main()