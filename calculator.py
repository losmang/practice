# Enter Calculation:  example...5 * 6
# 5 * 6 = 30

# store user input of 2 numbers and operator
num1, operator, num2 = input("Enter Calculation: ").split()

# convert the strings into integers
num1 = int(num1)
num2 = int(num2)


# if enter + then provide the output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1,num2,num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1,num2,num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1,num2,num1/num2))
elif operator == "%":
    print("{} % {} = {}".format(num1,num2,num1%num2))
else:
    print("Go to Hell!!!")
# print the result
