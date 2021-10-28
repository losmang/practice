# We'll provide different outputs based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# everyone else -> not important

# receive age and store in a var called age
age = eval(input("Enter age here: "))

# and : if both condition are true returen true
# or : if either condition is true then true
# not : convert a true condition into a false

# if age is greater than or equal to 1 or less than or equal to 18 print important
if(age >= 1) and (age <= 18):
    print("People care about you!")



# if age is 21 or 50 -> important
elif(age ==21) or (age == 50):
    print("You area douche fuck but people like you on this day!!")

# we check if age is less than 65 and then we convert true to false
elif(age > 65):
    print("Congrats!  Your\'re going to die soon")

# everybody else sucks
else:
    print("No one cares about you!!! :D")