#numbers
apples = 4
pears = 8
attendees = 3042
zip_code = 12345

price = 4.95
gpa = 3.74
pi = 3.14159

price = input("What is the price of a cup of coffee? ")
cups = input("How many cups do you want? ")
total = float(price) * int(cups)
print("Your total is $" + str(total) + " for " + cups + " cups." )