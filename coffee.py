#coffee shop simulator

#current day number
day = 1

#create an empty sales list
sales = []

#print a welcome message
print("Coffee shop simulator\n")
print("Let's collect some information before we start the game\n")

#get name and shop name
name = input("What is your name? ")
shop_name = input("What do you want to name your coffee shop? ")

print("\nThanks, " + name + ". Let's set some initial pricing. \n")

#get initial orice of cup of coffee
cup_price = input("What do you want to charge per cup of coffee? ")

#display what we have
print("\nGreat. Here's what we've collected so far.\n")
print("Your name is " + name + " and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + ".\n")

