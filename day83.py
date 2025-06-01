import pyttsx3 as p

# Initialize the text-to-speech engine
a = p.init()

# Set voice properties
voices = a.getProperty('voices')
a.setProperty('voice', voices[0].id)  # You can change index for different voices
a.setProperty('rate', 150)            # Speed of speech
a.setProperty('volume', 1)            # Volume (0.0 to 1.0)

# Input: safely get a list of names from user
names_input = input("Enter the list of names to give shoutout to (comma-separated): ")
b = [name.strip() for name in names_input.split(',') if name.strip()]

# Loop through names and give shoutouts
for i in b:
    text_to_say = f"Shout out for solve the problem {i}!"
    a.say(text_to_say)
    a.runAndWait()

print("Everyone has been given a shoutout.")
#Shout out for solve the problem