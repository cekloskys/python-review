# The print function prints its parameter to standard out
# and appends a line separator string to the end.
print("Hello World")

# The print method may print its parameter without appending
# a line separator string to the end using the end parameter.
print("Hello World", end=" ")
print("Hello World")

# The print function may be given Strings as well as any of
# the primitive and object types.
print(100)
print(True)
print(100.75)

# We can pass one or more parameters when using the print function.
# By default, they will be separated by a space.
print(100, True, 100.75)

# The default space can be modified and can be made to change to
# any characters, integer, or string using the sep parameter.
print(100, True, 100.75, sep="-")

# The sep and end parameters may be used together in one print statement.
print(100, True, 100.75, sep="-", end="!")

# The string % modulo operator can be used with the print function
# for formatting.
print("\nHello %s %s. You are %d years old." % ("Susan", "Ceklosky", 54))
print("Hello %s %s. You are %.2f years old." % ("Susan", "Ceklosky", 54.5))

# The input function can be used to get data from standard in.
# The returned object will always be a String.
first =  input("Please enter your first name: ")
last =  input("Please enter your last name: ")
print(first, last)

age = input("Please enter your age: ")
print("Hello %s %s. You are %s years old." % (first, last, age))
# This line of code will generate a TypeError because age is a string
# not a float.
# print("Hello %s %s. You are %.2f years old." % (first, last, age))
print(type(first), type(last), type(age))

# We must typecast the returnd object if we want to work with
# it in a form other than String.
intage = int(input("Please enter your age: "))
print("Hello %s %s. You are %d years old." % (first, last, intage))
floatage = float(input("Please enter your age: "))
print("Hello %s %s. You are %.2f years old." % (first, last, floatage))