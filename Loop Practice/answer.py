import sys

sys.path.append("../misc")

import misc #This is the misc.py in the sys.path.append("../misc")
import random


def fizz_buzz():
    
    n = int(input("Enter a number: "))
    
    
    for i in range(1, n+1):
        
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
def sum_of_square():
    result = 0
    
    n = int(input("Enter a number: "))
    
    for i in range(1, n+1):
        square = i ** 2
        
        result += square
        
        print(f"{i}^2 = {square}")
        
    print(result)    

def number_guessing_game():
    
    n = int(input("Enter a number: "))
    misc.clear_screen()
    
    print("Welcome to guess the number game!")
    
    guess = 0
    
    number_to_guess = random.randrange(1, n)
    
    while True:
        
        print(f"Guess a number between 1 to {n}")
        user_guess = int(input("Enter a guess: "))
        if user_guess < number_to_guess:
            misc.clear_screen()
            print("Too Low")
            guess += 1
        else: 
            if user_guess == number_to_guess:
                misc.clear_screen()
                print(f"Your guess is correct {user_guess}")
                print(f"The random number is {number_to_guess}")
                print(f"Your number of guesses is {guess}")
                break
            else:
                misc.clear_screen()
                print("Too High")
                guess += 1
        
        if guess == 5:
            print(f"Game over your number of guesses is {guess}")
            break