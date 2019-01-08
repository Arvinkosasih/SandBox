def main():
    plaintext = input("Input text : ")
    plaintext = plaintext.lower()
    list=' '
    for i in plaintext:
        if i == ' ':
            num = ' '
        else:
            num = str(ord(i) - 96)
        list = list + num
    print(list)

main()