import os
import time

items = os.listdir()

to_be_operated_on = []
answer = 1
while answer != "done":
    answer = input("Enter the extension of the files you would like to rename. You may add as many extensions as you want one by one. When you are done simply answer with a \"done\" in lower case.")
    if answer != "done":
        to_be_operated_on.append(answer)
to_be_name = 1
for item in items:
    name, extension = os.path.splitext(item)
    print(name, extension)
    if extension in to_be_operated_on:
        try:
            os.rename(item, f"{to_be_name}{extension}")
            to_be_name += 1
            print(f"File \"{item}\" has been operated on!")
        except:
            print(f"File \"{item}\" couldn't be operated on!")

time.sleep(5)