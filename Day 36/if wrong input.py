a= input ("enter the number:")
print (f"table of {a} is:")
try:
    for i in range(1, 11):
        print (f"{a} * {i} = {int(a)*i}")
except ValueError:
    print ("Please enter a valid number.")