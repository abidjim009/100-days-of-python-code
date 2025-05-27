a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
operation = input("Choosen your calculating operation(^,*,+,-,/)")

if operation == '^':
    print(a**b)
elif operation =='*':
    print(a*b)
elif operation =='+':
    print(a+b)
elif operation =='-':
    print(a-b) 
elif operation == '/':
    print(a/b)   
else:
    print("Invalid input")


a