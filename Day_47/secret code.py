choice = input("Enter 'code' to encode or 'decode' to decode: ")
message = input("Enter a message: ")
words = message.split()
result = []
for word in words :
    if choice == "code":
        if len(word)>=3:
            r1 = input("Enter a random string to add at the beginning: ")
            r2 = input("Enter a random string to add at the end: ")
            print(r1 + word[1:] + word[0] +r2 )
        else :
            print(word[::-1])
    elif choice == "decode":
        if len(word)>=3 :
            word = word[3:]
            word = word[:-3]
            word = word[-1] + word[:-1]
            print(word)
        else :
            print(word[::-1])
    else :
        print("Invalid choice. Please enter 'code' or 'decode'.")