with open('file.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('samplee.txt', 'r') as f:
  print(f.read())