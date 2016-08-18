# ---------- IS BIRTHDAY IMPORTANT ----------
# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

# eval() converts a string into an integer if it meets the guidelines
age = eval(input("Enter age: "))

# Logical operators can be used to combine conditions
# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

# If age is both greater than or equal to 1 and less than or equal to 18 it is true
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# If age is either 21 or 50 then it is true
elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and then convert true to false or vice versa
# This is the same as if we put age > 65
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")
