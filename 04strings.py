# Strings: http://localhost:8889/notebooks/Documents/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python%20Object%20and%20Data%20Structure%20Basics/02-Strings.ipynb

print('Hello World 1')
print('Hello World 2')
print('Use \\n to print a new line')
print('\n')
print('See what I mean?')
print('Use \\t to print TAB')
print('\tThis row starts with a tab')

# String Indexing
string1 = 'Hello world'
print(string1[0])

print(string1[9])
print(string1[-3])

print(string1[:3])
print(string1[2:5])
print(string1[2:8:2])
print(string1[::2])
print(string1[::-1])
print(string1[1::2])


# String Properties

name = 'Sam'

newName = 'P' + name[1:]
print(newName)

print(string1 + " it is beautiful outside!")
string2 = string1 + " it is beautiful outside!"
letter = 'z'
print(letter * 7)

print('2' + '2')

print(string2.count('l'))
print(string2.upper())
print(string2.lower())
print(string2.split())
print(string2.title())