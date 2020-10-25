#4.3  Representing Strings
import string

print("4.3  Representing Strings")
z = """
Hello
    World
"""
print(z)
print("=========================================")
#4.4  What Type Is String
print("4.4  What Type Is String or Int")
my_variable = 'Fachrul Rizki'
print(type(my_variable))

my_variable = 123
print(type(my_variable))
print("=========================================")
#4.5.1  String Concatenation
print("4.5.1  String Concatenation")
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)
print('Fachrul ' + 'Rizki')
print("=========================================")
#4.5.2  Length of a String
print("4.5.2  Length of a String")
print(len(string_3))
nama = "Fachrul Rizki"
print(len(nama))
print("=========================================")
#4.5.3  Accessing a Character
print("4.5.3  Accessing a Character")
nama = "Fachrul Rizki"
print(nama[5])
print("=========================================")
#4.5.4  Accessing a Subset of Characters
print("4.5.4  Accessing a Subset of Characters")
my_string = 'Fachrul Rizki'
print(my_string[4]) #characters at position 4
print(my_string[1:5])#from position 1 to 5
print(my_string[:7])#from start to position 5
print(my_string[2:])# from position 2 to the end
print("=========================================")
#4.5.5  Repeating Strings
print("4.5.5  Repeating Strings")
print('*' * 10)
print('aowk' * 10)
print("=========================================")
#4.5.6  Splitting Strings
print("4.5.6  Splitting Strings")
title = 'Fachrul sedang merangkum program di BAB 4, dan di kumpulkan di email pak zainal abidin'
print('Source string:', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))
print("=========================================")
#4.5.7  Counting Strings
print("4.5.7  Counting Strings")
my_string = 'Fachrul sedang merangkum program di BAB 4, dan di kumpulkan di email pak zainal abidin'
print("my_string.count('a'):", my_string.count('a'))
print("=========================================")
#4.5.8  Replacing Strings
print("4.5.8  Replacing Strings")
welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))
print("=========================================")
#4.5.9  Finding Sub Strings
print("4.5.9  Finding Sub Strings")
print('Edward Alun Rawlings'.find('Alun'))
print("=========================================")
#4.5.10  Converting Other Types into Strings
print("4.5.10  Converting Other Types into Strings")
msg = 'Hello IG saya fachrul_rizki0' + str(3)
print(msg)
print("=========================================")
#4.5.11  Comparing Strings
print("4.5.11  Comparing Strings")
print('Fachrul' == 'Fachrul') #prints True
print('Fachrul' == 'Rizki') #prints False
print('Fachrul' != 'John') #prints True
print("=========================================")
#4.5.12  Other String Operations
print("4.5.12  Other String Operations")
some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')", some_string.startswith('H'))
print("some_string.startswith('h')", some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())
print("=========================================")
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', "   xyz   ".strip())
print("=========================================")
#4.7  String Formatting
print("4.7  String Formatting")
format_string = 'Hello {}!'
print(format_string.format('Fachrul'))

# Allows multiple values to populate the string
print("Allows multiple values to populate the string")
name = "Fachrul"
age = 20
print("{} is {} years old".format(name, age))

# Can specify an index for the substitution
print("Can specify an index for the substitution")
format_string = "Hello {1} {0}, you got {2}%"
print(format_string.format('Fachrul', 'Carol', 75))

print("====Tata Letak=====")
print('|{:<25}|'.format('left aligned'))# The default
print('|{:>25}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))
print("=========================================")
#4.8  String Templates
print("4.8  String Templates")
template = string.Template('$artist sang $song in $year')
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))
print("=========================================")
#4.10  Exercises
print("4.10  Exercises")
#1. Replace string
ini_string = "Denyse,Marie,Smith,21,London,UK"
print(ini_string.replace(",", " "))

#2. Handle user input
string_1 = input("Masukkan String ke1 : ")
string_2 = input("Masukkan String ke2 : ")
new_string = "{} {}".format(string_1, string_2)

#print out the value of new_string
print(new_string)
#print out how long the contents of new_string is
print(len(new_string))
#convert all new_string to uppercase
print(new_string.upper())
#Now check to see if new_string contains the string 'Albus' as a substring.
print(new_string.find('Albus'))
