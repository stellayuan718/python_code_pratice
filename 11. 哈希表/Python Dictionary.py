dict = {'Name': 'Alice', 'Age': 7, 'Class': 'First'}

print("Name: ", dict['Name'])
print("Age: ", dict['Age'])
print(dict)

print("\n Updating Dictionary")

dict['Age'] = 8;
dict['Sex'] = 'F'
dict['School'] = "Elementary school"
print("Name: ", dict['Name'])
print ("Age: ", dict['Age'])
print ("Sex: ", dict['Sex'])
print(dict)

print("\n Delete Dictionary Elements")
del dict['Name']
print(dict)
dict.clear()  # remove all entries in dict
print(dict)

print("\n Properties of Dictionary Kyes")
print("\n 1. More than one entry per key not allowed")
dict = {'Name': 'Alice', 'Age': 7, 'Class':'First', 'Age':8}
print(dict)

'''print("\n 2. Kyes must be immutable")
dict = {['Name']: 'Zara', 'Age':7}
print("dict['Name']: ", dict['Name'])'''

a = "abc"
b = "xyz"

dict[a] = 123
dict[b] = 456
