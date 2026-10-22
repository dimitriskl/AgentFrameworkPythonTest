#This variable exists in the main scope
customer_name = "John"

# Define a new class
class Customer:
    customer_name = "Dim"

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __enter__(self):
        print("Entering scope.")
        #Run code upon entering scope of the statement
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving scope.")
        # Run code upon leaving scope of width statement

    def greet(self):
        print("Hello, " + self.name + "! ")

# Create three objects based on the Customer class
c1 = Customer("Sarah", "Atlanta")
c2 = Customer("Robert", "Florence")
c3 = Customer("Thomas", "Denver")

#Add the customer objects to a list
customers = [c1, c2, c3]

# Iterate throught list, greet, then display information
for c in customers:
    c.greet();
    print(c.name + " lives in " + c.city + ". ")

# Display the name in the main scope
print (c1.customer_name)

# use with to create a scope
with Customer("Yannis", "Athens") as yannis:
    yannis.greet()
