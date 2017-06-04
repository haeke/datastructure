"""
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

practice - control flow, and functions
"""

import random

# helper functions
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name.lower() == "rock"):
        return 0
    elif(name.lower() == "spock"):
        return 1
    elif(name.lower() == "paper"):
        return 2
    elif(name.lower() == "lizard"):
        return 3
    elif(name.lower() == "scissors"):
        return 4
    else:
        return("Not valid")

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "spock"
    elif(number == 2 ):
        return "paper"
    elif(number == 3 ):
        return "lizard"
    elif(number == 4 ):
        return "scissors"
    else:
        return

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    print('\n')
    print("Player chose: %s" % player_choice)
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(3)
    print("Computer chose: %s" % number_to_name(comp_number))
    comp_choice = number_to_name(comp_number)
    rank = ((player_number - comp_number) % 5)
    #if rank is 1 or 2 player_number wins
    #if rank is 3 or 5 comp_number wins
    print("rank: %d" % rank)
    if(rank == 1 or rank == 2):
        print("winner is %s" % player_choice)
    elif(rank == 3 or rank == 4):
        print("winner is %s" % comp_choice)
    else:
        print("No winner")




    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
