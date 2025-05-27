f = open('myfile.txt', 'r')
# Read the contents of the file
print(f)
text = f.read()
print(text)
f.close()

f = open('myfile.txt', 'r')
f.write("Hello, world!")
f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hello, world!")