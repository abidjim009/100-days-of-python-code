class Person:
  name = "JIM"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Ayesha"
a.occupation = "Bayadob"

b.name = "Abid"
b.occupation = "Vlo manush"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
