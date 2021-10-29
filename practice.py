age = int(input("How old are you? "))

if (age <= 5):
    print("You are to young for schoool...Go out and play!")
elif (age == 6):
    print("Go to kindergarten")
elif (age > 6) and (age < 19):
    print("You should be in grade {}".format(age - 6))
else:
    print("Go to college or get a job or something")
