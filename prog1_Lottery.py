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
        print("\t\33[1m\33[35m       Pick wisely! Goodluck\33[0m\U0001F609")
        return response
    elif response.lower() == "n":
        print("\n\33[35m\33[1m   Thank you! Come back again where you're ready!\33[0m")
        print("\t       You may now exit\U0001F607")
        sys.exit("\n")
    else:
        print("\n\33[3m\33[1m\33[31mxXx\33[0m \33[3m\33[1mSorry you it looks like you type an invalid keyword! \33[31mxXx\33[0m")
        print("\n")
        return readyXnot()

def game():
    name = ("\t\33[35m ▄▀▄▀▄▀▄▀<\33[1m\33[37mKRIZZY'S LOTTERY\33[0m\33[35m>▄▀▄▀▄▀▄\33[0m")
    border = ("\t\33[35m▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀\33[0m")
    print("\n")
    print(border)
    print(name)
    print(border)

def menu():
    list = ["\n 1. Play", " 2. Exit"]
    print(list[0])
    print(list[1])

def start():
    while True:
        pick = input("\nEnter your choice: ")
        if pick == '1':
            string = "\n\t              \33[3m\33[1m\33[35m Starting!\33[0m" 
            print(string)

            playerPICK = ask_player_num()
            lotteryWin = lottery_price_number()
            reveal(playerPICK,lotteryWin)

            again()
        
        elif pick == '2':
            print("\n\t    \33[3m\33[1m\33[35mThank You! You may now exit\33[0m")
            sys.exit("\n")

        print("\n       \33[3m\33[1m\33[35mInvalid Input! Choose from 1 and 2\33[0m \U0001F60A")

def ask_player_num():
    playerPICK = []
    while len(playerPICK) < ask_number:
        pick =input(f"\n\t \33[3m\33[1m\33[35mPick a number from {min_num} to {max_num}\33[0m \n>>")
        try:
            pick = int(pick)
        except:
            print("   \33[3mSorry your input might be an integer!\33[0m")
            continue
        if min_num <= pick <= max_num:
            if pick not in playerPICK:
                playerPICK.append(pick)
            else:
                print(" \33[3m Error! Your not allowed to pick the same number!\33[0m")
        else:
            print(" \33[3mError! You are only allowed to pick from 1 to 9!\33[0m")

    return sorted(playerPICK)


def lottery_price_number():
    return sorted(random.sample(range(min_num, max_num), ask_number))

def reveal(playerPICK, lotteryWin):
    if playerPICK == lotteryWin:
        print("\t   \33[3m\33[1m\33[35mCongratulations! You win ₱{}".format(win_price), 
        "\n Your numbers: ", playerPICK,
        "\nThe winning lottery numbers are: ", lotteryWin, "\n" )
    else:
        print("\n Sorry, you loose", "\n Your numbers:", playerPICK, 
        "\n The winning lottery numbers are:", lotteryWin, "\n")

def again():
    answer = input("\nTry again y/n. \n>> ")
    if answer.lower() == "y":
        return start()
    elif answer.lower() == "n":
        print("\t          \33[3m\33[35mThanks for playing! ")
        sys.exit("\n")
    else: 
        print("\t\33[35m\33[1m        Sorry your input must be a y or n!\33[0m")
        return again()


intro()
readyXnot()
game()
menu()
start()

