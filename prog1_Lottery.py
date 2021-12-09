# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit

import random
import sys

ask_number = 3
min_num = 0
max_num = 9
win_price = 5,550,000

def intro():
    print("\n\t\33[1m\33[35m     Welcome to Krizzy's Lottery\33[0m")
    print("\t\33[3mGet a chance to win 5,550,000 pesos!\33[0m")
    name = input("\nKindly, enter your name\33[1m: ")
    print(f"\n\t\33[1m\33[35m            Hello {name.capitalize()}\U0001F601\33[0m")
    print("\t\33[3m     Are you ready win prizes?\33[0m")

def readyXnot():
    print("\n\t\33[1m Kindly, type \33[35my\33[0m \33[1mif yes and \33[35mn\33[0m \33[1mif no.\33[0m")
    response = input(">>\33[1m ")
    print("\33[0m")
    if response.lower() == "y":
        print("\t\33[1m       Pick wisely! Goodluck\33[0m\U0001F609")
    elif response.lower() == "n":
        print("\n   Thank you! Come back again where you're ready!")
        print("\t       You may now exit\U0001F607")
        sys.exit("\n")
    else:
        print("\33[31m\33[3m\33[1m  Sorry you it looks like you type an invalid keyword!\33[0m")
        return readyXnot()

intro()
readyXnot()