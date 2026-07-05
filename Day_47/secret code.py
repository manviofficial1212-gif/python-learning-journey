choice = input("Enter 'code' to encode or 'decode' to decode: ")
message = input("Enter a message: ")
words = message.split()
result = []

if choice == "code":
        r1 = input("Enter a random string to add at the beginning: ")
        r2 = input("Enter a random string to add at the end: ")
        for word in words :
            if len(word)>=3:
        
                encoded_word = (r1 + word[1:] + word[0] +r2 )
                result.append(encoded_word)
            else :
                result.append(word[::-1])
        print(" ".join(result))
elif choice == "decode":
        for word in words :
            if len(word)>=3 :
                word = word[3:]
                word = word[:-3]
                word = word[-1] + word[:-1]
                result.append(word)
            else :
                result.append(word[::-1])
            print(" ".join(result))
else :
        print("Invalid choice. Please enter 'code' or 'decode'.")
    