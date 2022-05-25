import random

print("Welcome to Number Guessing Game!")
nr = int(input("Write the number you want to go from 1 to ?: "))
number = random.randint(1, nr)

print("\nRemember you can only try 6 times to guess the number!")
print("Type exit to exit game")

lives = 6
while True:
    player = input("\nGuess the chosen number: ")
    if player == "exit":
        print("Thank you for playing...")
        break
    elif lives == 1:
        print("You Lose!\nYou are out of lives.")
        break
    elif int(player) == number:
        print("Congratulations you guessed the number!")
        break
    elif int(player) > number:
        lives -= 1
        print(f"Too high, you have {lives} lives left!")
    elif int(player) < number:
        lives -= 1
        print(f"Too Low, you have {lives} lives left!")
    else:
        print("Wrong value!")
