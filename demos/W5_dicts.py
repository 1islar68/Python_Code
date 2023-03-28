#Initilise empty dictionary
d = {}
dictio = dict()
#Initilise non-empty dictionary
phonebook = {"Thomas":77654321783, "Aga":788792912, "MD":7777727723}
#Print full dictionary
print(phonebook)
#Print/access individual elements
name = input("Who you gonna call: ")
if name in phonebook:
    print(f"Calling... {phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two lists together to compose a dictionary
names = ["Garry", "Ian", "Laura"]
age = [56, 21, 16]
people = dict(zip(names, age))
print(people)
#Traversing Dictionaries - accessing keys/values/both
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for thing in people.keys():
    print(thing)
for k, v in people.items():
    print(f"Person {k} is {v} years old")