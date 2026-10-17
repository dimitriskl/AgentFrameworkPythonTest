#coffee shop simulator

#import random libraries
from random import seed
from random import randint

#current day number
day = 1

#starting cash
cash = 100.00

#cofee on hand
coffee = 100

#create an empty sales list
sales = []

#print a welcome message
print("Coffee shop simulator\n")
print("Let's collect some information before we start the game\n")

#get name and shop name
name = False
while not name:
    name = input("What is your name? ")

shop_name = False
while not shop_name:
    shop_name = input("What do you want to name your coffee shop? ")

print("\nThanks, " + name + ". you have created your Coffee Shop: " + shop_name + ".\n")

#print ok lets have some fun
print("\nOk Let's have some fun!!!\n")
#the main game loop
running = True
while running:
    #display the day
    print("\n-----| Day " + str(day) + " @ " + shop_name + " |-----")    #generate random temperature between 20 and 50
    temperature = randint(20, 90)

    #display the cash and weather
    print("Current temperature is " + str(temperature) + " degrees. And our cash is $" + str(cash))

    # #get initial price of cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    #buy advertising
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising would you want to buy? (0 for none)? ")

    #convert advertising to float
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0
    #deduct advertising from  cash on hand
    cash -= advertising

#TODO: Calculate today's performance
#TODO: Display today's performance

    #before we loop around add a day
    day += 1





