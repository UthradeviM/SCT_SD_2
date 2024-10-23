import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Prompt the user to enter their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            # Compare the guess to the generated number
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
