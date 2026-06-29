num=int(input("Enter a number: "))
a=[2,3,5,6]
try:
    print(a[num])
except ValueError:
    print("Please enter a valid number.")
except IndexError:
    print("Index out of range. Please enter a number between 0 and 3.")