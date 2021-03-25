#Operator Aritmatika

x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x + y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 50625
print('x ** y =', x ** y)

#Operator Relasional/Comparison

x = 15
x = 10
y = 12

# Output: x > y is False
print('x > y is', x > y)

# Output: x < y is True
print('x < y is', x < y)

# Output: x == is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

#Operasi Logika

x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)

#OPERATOR STRING
#Contact Strings

# srings

str1 = "Hello"
str2 = "World"

# contact

result = str1 + "" + str2

# Output

print(result);

#OPERATOR STRING
#Mereplikasi strings

# string

str = "HA"

# replicate

result = str * 3

# Output

print(result)

#OPERATOR STRING
#Pengecekan membership-in

# strings

needle = "lo"
haystack = "Hello World"

# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#OPERATOR STRING
#Checking membership - not in

#strings

needle = "HA"
haystack = "Hello World"

# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#OPERATOR STRING
#Mengakses karakter dalam string

#string
str = " Jane Doe"

#character
ch = str[1]

#Output
print(ch)   #a

#OPERATOR STRING
#Substring

#string
str = "Hello World"

#substring
substr = str[3:5]

#output
print(substr)   #lo

#OPERATOR STRING
#Skipping character

str = "Hello World"

#skip
new_str = str[0::2]
print(new_str)

#OPERATOR STRING
#Reverse string

#string
str = "Hello World"

#reverse
result = str[::-1]

#output
print(result)