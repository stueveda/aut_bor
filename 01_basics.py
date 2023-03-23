# Automate the Boring Stuff with Python
# Chapter 1
# Python Basics




# when running through the interactive shell, >>> is the python prompt

# 2 + 2 is an expression
# it has values (2), an operator (+), and can always evaluate (reduce down to) a single value

num = 2 + 2
print(num)

#Math operators include:

# **  exponent
num = 2 ** 3
print(num) # 8

# %   modulus
num = 22 % 8
print(num) # 6

# //  integer division
num = 22 // 8
print(num) # 2

# /   division
num = 22 / 8
print(num) # 2.75

# *   multiplication
num = 3 * 5
print(num) # 15

# -   subtraction
num = 5 - 2
print(num) # 3

# +   addition
num = 2 + 2
print(num) # 4


# order of operations in Python is similar to normal mathematics:
# 1. **
# 2. *, /, //, % (from left to right)
# 3. +, - (left to right)
# Note - parens () can override usual precedence


num = (5 - 1) * ((7 + 1) / (3 - 1))
print(num) # 16.0


# Data Types

# integers are whole numbers
# ex: -2, -1, 0, 1, 2, 10, 1000, 348743298

# floating point numbers have decimals
# ex: -1.25, -1.0, 0.0, 0.23455, 1.0, 37329.832

# Strings have characters surrounded by single or double quotes
# ex: 'a', 'aa', 'Hello!', '1', '5 golden rings', ''

# Operators may change meanings based on the data types next to it
# + is addition operator for ints/floats, but concatenation for strings

foo = 2 + 5
print(foo)

bar = 'Alice' + 'Bob'
print(bar)

# trying to mix these datatypes will give an error

# baz = 'Alice' + 42

# you can do string replication with a string and * operator though:
baz = 'Alice' * 3
print(baz)



# Variables

# you can store values in variables with assignment statements
# (variable name) = (value)
spam = 42

# think of a variable as a labeled box with a value placed in it.
# label = spam, value = 42

eggs = 15

print(spam + eggs)

# when a new value is assigned to a variable, the old value is forgotten

eggs = eggs + 5
print(eggs)

# you can assign any type to any variable, even if it doesn't match what was there before

eggs = 'Howdy!'

# Variable Names

# Should describe what the represent concisely

# rules:
#   can only be one word with no spaces
#   can only use letters, numbers, and underscore (_)
#   can't begin with a number

# Variable names are case sensitive - spam is different from Spam is different from SPaM


# Comments

# a line starting with the (#) symbol is a comment
# Python ignores these lines; they aren't executed



# Useful Functions

# print() displays the string value inside its parens to the screen
# can be a string, value, or expression

print('Hello World!')

# input() waits for the user to type some text and press ENTER
# this function evaluates to a string equal to the user's text

name = input('What is your name? ')

# remember we can use string concatenation to make this greeting!
print('Hi there, ' + name + ', nice to meet you!')

# len() returns the length of various objects passed to it (such as a string)

print('The length of your name is: ')
print(len(name))


# str(), int(), float() can be used to change datatypes of values

print(str(0))

print(str('-3.14'))

print(int('42'))

print(int('-99'))

print(int(1.45))

print(float('3.14'))

print(float(10))