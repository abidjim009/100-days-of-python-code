import pyttsx3 as py

names = []
while True:
    name = input("Enter a name or quit to quit: ")
    if name.lower() == 'quit':
        break
    names.append(name)

for name in names:
    engine = py.init()
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()
