print(a:=False)
# This is a simple assignment expression that assigns False to the variable 'a' and then prints it.
# The assignment expression allows you to assign a value to a variable as part of an expression.

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while(n :=len(number)) > 0:
    print(number.pop())

    foods =(    )

    while(food := input("Enter food (or 'done' to finish): ")) != "done":
        foods.append(food) 