try:
    print("Enter 1 to code and enter 2 to decode:")
    choice=int(input())
    if(choice==1):
        message=input("Enter the message to be coded:")
        if(len(message)>=3):
            print(f"srd{message[1:len(message)]}jdh{message[0]}")
        else:
            print(f"{message[::-1]}")
    elif(choice==2):
        message=input("Enter the message to be decoded:")
        if(len(message)<3):
            print(f"{message[::-1]}")
        else:
            print(f"{message[len(message)-1]}{message[3:len(message)-4]}")        
except Exception:
    print("Please enter a valid input")      