from random import seed
from random import randint

#Get a random number
random_number = randint(1, 10)
#set the bool to check answer as false
answered = False
#Get the user's guess
guess = int(input("Guess a number between 1 and 10: "))
#while anwer_bool is false
while not answered:
    #check if the int of the number is equal to the user's guess
    if guess == random_number:
        #if it is equal then display a bravo message and make the answer_bool true
        print("Correct!")
        answered = True
    #else display this is not a correct guess and try again
    else:
        print("Not quite!")
        #display if it must go up or down
        if(guess > random_number):
            print("Your guess is up!")
        else:
            print("Your guess is down!")

        #display how far away the number is from their guess
        print(f"Your guess is {guess - random_number} away!")
        #get another user's guess
        guess = int(input("Guess again a number between 1 and 10: "))

