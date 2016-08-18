# ---------- PROBLEM : MILES TO KILOMETERS ----------
# Sample knowing that kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.0467 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))
