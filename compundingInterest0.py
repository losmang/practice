# have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investmetn * interest
# Print out their earnings after a 10 year period

investment = input("Enter your investment amount here: " )
interest = input("Enter your interest rate here: ")

investment = float(investment)
interest = float(interest) * .01

for i in range(1,10):
    investment = investment + (investment * interest)
    print("Total investment after 10 years is {:.2f}".format(investment))