'''PSEUDOCODE
1. Importing os , datetime and random
2.Taking user input in variable name
3.Creating a list called random numbers
4. Adding 0 to 9 random numbers in random_numbers variable list
5.Displaying the elements of random_number
'''

import os
import datetime
import random

date = datetime.datetime.now()
path = os.getcwd()
user_profile = os.environ.get('USERNAME')
print(path)
print("Programmer: ", user_profile)
print(date.strftime("Lab 15.2 %B %d,%Y @ %I:%M:%S\n"))


def main():
    name = input("Enter your name: ")
    random_numbers = []
    # Generate 7 random numbers to later display to the user
    for i in range(1,8):
        random_numbers.append(random.randint(0, 9))
    # Display the random numbers
    print(f"{name}, these are the random numbers in the list:")
    # use * to unpack list items
    print(*random_numbers, sep=",")


main()
