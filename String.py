print("STRING - str")

# Concatenation
print("-------------------------")
print("Ravi" + " Raj" + " Singh")

# String Replication
print("-------------------------")
print("Ravi Raj Singh" * 3)
print("-" * 25)

# String Length
print("-------------------------")
print(" Ravi Raj Singh")
print(len(" Ravi Raj Singh"))

# String Slicing
print("-------------------------")
print("Ravi Raj")
# Concept of indexing - Above R- [0], A[1],v[2],i[3], [4],R[5],a[6],j[7] in positive.
# Negative indexing - j [-1], a[-2], R[-3], [-4], i[-5], v[-6], a[-7], R[-8]
print("Ravi Raj"[-6])
# print from one index to other using print ("Ravi Raj" [-8:4]) = Ravi
print("Ravi Raj"[-8:4])
print("Ravi Raj"[5:])
print("Ravi Raj"[:7])
print("Ravi Raj"[-8:-2])

# String Case Conversion (Uppercase / Lowercase)
print("Ravi Raj".lower())
print("Ravi Raj".upper())

# String Stripping
print(" Ravi Raj ". strip())
print("     Ravi Raj    ".strip())

# String Replacing -
print("Ravi Raj")
print("Ravi Raj".replace("a", "A"))

# String Count -
print("Ravi Raj")
print("Ravi Raj".lower(). count("r"))

# String Find-
print("Ravi Raj". find("vi"))

# String Check -
print("Ravi".isalpha())
print("93s9".isdigit())
print("Ravi". lower() .islower())
print("Ravi". upper(). isupper())

# String Capitalization
print("Ravi Raj". capitalize())
print("Ravi raj". title())

# Check for start and end
print("Ravi Raj". startswith("Ravi"))
print("Ravi Raj". endswith("Ravi"))

# Adjust String
print("Ravi Raj". center(20, "-"))
print("Ravi Raj". ljust(20,"*"))
print("Ravi Raj". rjust(20, "*"))
print("--------------------------------")
