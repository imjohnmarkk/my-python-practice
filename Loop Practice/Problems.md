Here's a fun problem to practice your loop skills:
 
The FizzBuzz Challenge
 
Problem:
 
Write a program that prints the numbers from 1 to 100.  But for multiples of 3, print "Fizz" instead of the number.  For multiples of 5, print "Buzz".  For numbers that are multiples of both 3 and 5, print "FizzBuzz".
 
Example Output:
```plaintext
1
2
Fizz
4
Buzz
Fizz
...
14
FizzBuzz
...
97
98
Fizz
Buzz
```
 
Hints:
 
- Use a for loop to iterate from 1 to 100.
- Use the modulo operator (%) to check if a number is divisible by 3 or 5.
- Use if statements to determine what to print based on the divisibility rules.
 
Bonus Challenge:
 
- Modify the program to take the upper limit (instead of 100) as input from the user.

----

The Sum of Squares
 
Problem:
 
Write a program that calculates the sum of squares of all numbers from 1 to a given number n.
 
Example:
 
If n = 5, the sum of squares would be:
 ```plaintext
1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55
```
Hints:
 
- Use a for loop to iterate from 1 to n.
- Calculate the square of each number using the exponentiation operator (**).
- Keep track of the sum using a variable.
 
Bonus Challenge:
 
- Modify the program to take the number n as input from the user.
 
Let me know if you'd like more hints or want to discuss your solution!  😊

___

The Number Guessing Game
 
Problem:
 
Write a program that lets the user play a number guessing game. The program should:
 
1. Generate a random secret number:  The secret number should be between 1 and 100 (inclusive).
2. Prompt the user to guess the number:  The program should keep asking the user to guess until they guess correctly.
3. Provide feedback:  After each guess, the program should tell the user if their guess was too high, too low, or correct.
4. Count the number of guesses:  The program should keep track of how many guesses the user took.
 
Example Gameplay:
```plaintext 
I'm thinking of a number between 1 and 100.

Guess the number: 50
Too high!

Guess the number: 25
Too low!

Guess the number: 37
Too high!

Guess the number: 31
You got it! It took you 4 guesses.
```
 
 
Hints:
 
- You'll need to use the  random  module to generate a random number.
- Use a  while  loop to keep asking for guesses until the user guesses correctly.
- Use  if  statements to provide feedback based on the user's guess.
 
Bonus Challenge:
 
- Add a feature to limit the number of guesses the user gets (e.g., 7 guesses).
- Add a feature to keep track of the user's best score (the fewest guesses taken).
 