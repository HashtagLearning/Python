# below function will perform add
def add(a,b):
    # add two numbers
    return a+b # a, b are added

# line 1
# line 2
# line 3
print("hello")

"""
This is a comment
written in
more than just one line
"""
print("hello")

# casting
# int to float
x = 100 # int
x_float = float(x)
print(type(x_float),x_float)

# float to int
x_float = 100.5
x = int(x_float)
print(type(x),x)

# str to float
x_str = '3.0'
x_float = float(x_str)
print(type(x_float),x_float)

# int to str
x = 1000
x_str = str(x)
print(type(x_str), x_str)

# boolen 
print(10 > 9) # true
print(10 == 9) # false
print(10 < 9) # false

a = 100
b = 43
if b > a:
    print("b is greater")
else:
    print("a is greater")

print(bool(0))
print(bool(1))
print(bool('hello'))
print(bool(''))

# assignment
xa = 5
xa += 10 # xa = xa + 5
print(xa)
xa -= 5 # xa = xa - 5
print(xa)
xa *= 2
print(xa)
xa /= 2
print(xa)
#xa %= 3
#print(xa)
xa **= 2 
print(xa)

# logics
xl = 5      #0101 
xl &= 3     #0011
print(xl)   #0001 ADD

xl = 5
xl |= 3
print(xl) # OR

xl = 5
xl ^= 3
print(xl) # NOT

xl = 5 
xl >>=1
print("{0:b}".format(xl)) # right shift 
#0101 
# shift-1 = 0010 
# shift-2 = 0001 
# shift-3 = 0000

xl = 5
xl <<=3
print("{0:b}".format(xl))
#0101 
# shift-1 = 1010
# shift-2 = 10100 
# shift-3 = 101000

# comparison
# == Equal x == y
# != Not equal x != y
# > greather than x > y
# < less than x < y
# >= greather than equal x >= y
# <= less than equal x <= y

# logics combine
# && -> and # ((x == y) and (a == b))
# || -> or # ((x == y) or (a == b))
# not -> (not((x == y) and (a == b)))

print("Hello world")