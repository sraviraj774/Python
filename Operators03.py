print("Operators")

# Operators - It is basically different types of operators that we use to perform action on datatypes and variables.
# There are three types of operators - Arithmetic operators, Comparison Operators, Logical operators.

# A. Arithmetic Operators - These are mathematical operators. ( +, -, *, /)

# 1. Addition
print("--------------Addition----------------")
print(2 + 3)
print(2.5 + 3.5)
print(2.5 + 3)
print(True + True)
print(True + False)
print(False + False)
print(True + 2.5)
print(False + 1)
#  If we add string with other data types it does not work.
#  If we add string with other string it works and known as concatenation.

# 2. Subtraction
print("--------------Subtraction----------------")
print(2 - 3)
print(2.5 - 3.5)
print(2.5 - 3)
print(True - True)
print(True - False)
print(False - False)
print(True - 2.5)
print(False - 1)


# 3. Multiplication
print("--------------Multiplication-------------")
print(2 * 3)
print(2.5 * 3.5)
print(2.5 * 3)
print(True * True)
print(True * False)
print(False * False)
print(True * 2.5)
print(False * 1)


# 4. Division
print("--------------Division----------------")
print(2 / 3)
print(2.5 / 3.5)
print(2.5 / 3)
print(True / True)
print(True / 2.5)
print(False / 1)

# 5. Floor Division
print("--------Floor Division (Quotient)----------------")
print(18//5)
print(3//2)
print(2.5//5.0)
print(2.5//1)

# 6. Modulo
print("-------------- Modulo (Remainder) ------------------")
print(3 % 2)
print(2.5 % 5.0)
print(2.5 % 1)

# 7. Exponentiation
print("-------------- Exponentiation ------------------")
print(3 ** 2)
print(2.5 ** 5.0)
print(2.5 ** 1)

# 8. Abs
print("----------------- Abs -----------------")
print(abs(-3.5))
print(abs(-35))

# 9. Round
print("----------------- Round -----------------")
print(round(2.123456, 3))
print(round(1.123456, 4))

# 10. Power
print("------------------ Power -------------------")
print(pow(3, 2))
print(pow(5, 3))

# B. Comparison Operators - All the comparison operators give output in True or False.

# 1.  is equal to ==
print("-------------- is equal to == --------")
print(1 == 2)
print(1.0 == 1)
print('A' == 'a')
print(True == 1)
print(False == 0)

# 2.  is not equal to !=
print("-------------- is not equal to == --------")
print(1 != 2)
print(1.0 != 1)
print('A' != 'a')
print(True != 1)
print(False != 0)

# 3. is greater than >
print("-------------- is greater than >  --------")
print(5 > 2)
print(1.0 > 1)
print('A' > 'a')  # . Ascii Value of A = 65 and a = 97
print(True > False)
print(False > 0)

# 4. is less than <
print("-------------- is less than >  --------")
print(1 < 2)
print(1.0 < 1)
print('A' < 'a')  # . Ascii Value of A = 65 and a = 97
print(True < False)
print(False < 1)

# 5. is less than or equal to <=
print("-------------- is less than or equal to <=  --------")
print(1 <= 2)
print(1.0 <= 1)
print('A' <= 'a')  # . Ascii Value of A = 65 and a = 97
print(True <= False)
print(False <= 1)

# 6. is greater than or equal to >=
print("-------------- is greater than or equal to >=  --------")
print(1 >= 2)
print(1.0 >= 1)
print('A' >= 'a')  # . Ascii Value of A = 65 and a = 97
print(True >= False)
print(False >= 1)

# C. Logical Operators -
# The logical operators works as conditions.

# 1. and - If both conditions are true, then only it gives true.
print("-------------- and  --------")
print(True and True)
print(False and False)
print(True and False)
print(False and True)

# 2. or - If first situation is work either second condition is work than it results True.
# If both not work it does not show True.

print("-------------- or  --------")
print(True or True)
print(False or False)
print(True or False)
print(False or True)

# 3. not - it indicates opposite of what is written after that.
print("-------------- not  --------")
print(not(False))
print(not(True))
