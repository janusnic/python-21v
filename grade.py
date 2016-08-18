# ---------- PROBLEM : DETERMINE GRADE ----------
# If age 5 go to kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 then say go to college
# Try to complete with 10 or less lines

# Ask for the age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too Young for School")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarten")

# Since a number is the result for ages 6 - 17 we can check them all
# with 1 condition
# Use calculation to limit the conditions checked
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))

# Handle everyone else
else:
    print("Go to College")
