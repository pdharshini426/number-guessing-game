"""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!
Enter your guess: 50
Incorrect! The number is less than 50.
Enter your guess: 25
Incorrect! The number is greater than 25.
Enter your guess: 35
Incorrect! The number is less than 35.
Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts."""


print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")
import random
number = random.randint(1, 100)

difficulty=int(input("""Please select the difficulty level:
      1. Easy (10 chances)
      2. Medium (5 chances)
      3. Hard (3 chances)\nenter:"""))


def easy(chance):
     for i in range(1,chance+1):
          val = int(input("enter your guess:"))
          if val == number:
              print(f"Congratulations! You guessed the correct number in {i} attempts.")
              break
          elif number < val:
               print(f"Incorrect! The number is less than {val}.") 
          elif number > val:
               print(f"Incorrect! The number is greater than {val}.")

match difficulty:
      case 1:
            print("You have 10 chances to guess the correct number.")
            easy(10)
      case 2:
            print("You have 5 chances to guess the correct number.")
      case 3:
            print("You have 3 chances to guess the correct number.")
      case _:
        print("Invalid choice")
            

               
             