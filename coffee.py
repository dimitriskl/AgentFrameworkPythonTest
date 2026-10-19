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
def welcome():
	print("Coffee shop simulator(")
	print("Let's collect some information before we start the game\n")

def prompt(display="Please input a string",require=True):
	if require:
		s=false
		while not s:
			s=input(display + " ")
	else:
		s=input(display + " ")
	return s
	
def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
	print("You have $"+str(cash_on_hand)+" cash on hand and the temperature is " + str(weather_temp) +".")
	print("You have enough coffee on hand to make "+ str(coffee_inventory) + " cups")
	
def convert_to_float(s):
	try:
		f=float(s)
	except ValueError:
			f=0
	return f

def get_weather():
	return randint(20,90)

#print welcome meszage
welcome()

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
    temperature = get_weather()

    #display the cash and weather
    daily_stats(cash, temperature,coffee)

    # #get initial price of cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    #buy advertising
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising would you want to buy? (0 for none)? ")

    #convert advertising to float
    advertising = convert_to_float(advertising)
    
    #deduct advertising from  cash on hand
    cash -= advertising

#TODO: Calculate today's performance
#TODO: Display today's performance

    #before we loop around add a day
    day += 1





