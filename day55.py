'''
print("Welcome to snake water and gun")
import random
l=["snake","water","gun"]
a=int(input("Enter number of times you want to play"))
point =0
for i in range (0,a):
    b=input("enter snake water or gun")
    c=random.choice(l)
    if b==c:
        print("Correct choice")
        point+=1
    else:
        print("Ops wrong choice")
print("Points collected is",point)

'''

import random
print('simple rock paper scissors game :-) ')
x=input('enter your input;- rock,paper or scissors: ')
y=random.choice(['rock','paper','scissors'])

print(f'you have chosed {x} and computer have chosed {y}')

if x=='rock' and y=='paper':
    print('you lose')
elif x=='rock' and y=='scissors':
    print('you won')
elif x=='paper' and y=='scissors':
    print('you lose')
elif x=='paper' and y=='rock':
    print('you won')
elif x=='scissors' and y=='rock':
    print('you lose')
elif x=='scissors' and y=='paper':
    print('you won')
else:
    print('game draw')