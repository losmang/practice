#if age is 5 go to kindergarten
# ages 6 - 17 go though grades 1 - 12
# if greater than 17 go to college
# try and complete with 10 lines

# Store age in var
age = eval(input("Enter your Age here: "))


# if 5 go to Kindergarten
if(age < 5):
    print("You are too young for school, go play!!!")
elif(age == 5):
    print("Go to kindergarten!!! :)")

# ages 6- 17 go to grades 1 - 12
elif(age >= 6) and (age <= 17):
    print("You should be in grade {}".format(age - 5))
else:
    print("Go to college or get a job or something!!! :D")
