# Problem: Recieve miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 Miles = 8.04 kilometers


# Ask the user to input miles and assign it to them miles variable
miles = input("Enter Miles here: ")

# convert from string to interger
miles = int(miles)

# perform calculation by multiplying 1.60934 times miles save in a variable called kilometers
kilometers = miles * 1.60934

# print results using format()
print("{} miles is {} kilometers".format(miles,kilometers))