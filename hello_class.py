# Define the World class
class World:
    # Define our greeting
    greeting = "Hello, World!"

    # Run this whenever the object is created
    def __init__(self):
        # Print the greeting
        print(self.greeting)

    # Delete the class
    def __del__(self):
        print("I'm gone!")

# Use the class World to create a world object named w
w = World()

print(World.greeting)
del(w)