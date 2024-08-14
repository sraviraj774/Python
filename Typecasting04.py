print("Typecasting")

# Typecasting - To convert from one data type to another.

# Integer
print("-------------------------------")
# Float to Integer
print(3.14)
print(int(3.14))
# String to integer - only possible when text inside string is purely one integer.
print(int("10"))
# Boolean to Integer
print(int(True))
print(int(False))

# Float
print("-------------------------------")
# Integer to Float
print(3)
print(float(3))
# String to float - only possible when text inside string is purely one float.
print(float("10.5"))
# Boolean to float
print(float(True))
print(float(False))

# String
print("-------------------------------")
# Integer to String
print(123)
print(str(123))
# float to String -
print(str("10.5"))
# Boolean to float
print(str(True))
print(str(False))

# Boolean
print("-------------------------------")
# Integer to Boolean - non-zero number is treated as true and zero is treated as false.
print(bool(1))
print(bool(123))
print(bool(-1001))
print(bool(00000))

# String to Boolean -
print(bool("Ravi"))
# float to boolean -
print(bool(30.20))
print(bool(0.00))

# Exceptions
print("------------------------------------------")
a = 3.14
print(a)
print(int(a))
print(float(int(a)))
print(type(float(int(a))))
# int of float 3.14 is 3 and then if we convert it into float again it is 3.0 which is not same as 3.14.
