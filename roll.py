import sys
import random
# list will be used to store each individual roll
rolls = []

def roll(num_dice, dice_max):
    """roll a die of a given size a number of times and return the result
    Function calls recursively until with num_dice diminishing to 0

    Arguments:
    num_dice -- the number of dice to be rolled
    dice_max -- the max value of each die
    """
    if num_dice < 1:
        return 0
    my_roll = random.randrange(dice_max) + 1
    rolls.append(my_roll)
    return my_roll + roll(num_dice-1, dice_max)

def main():
    arguments = sys.argv
    command = arguments[1]

    # parse arguments with the convention of XdY
    # where X == number of dice and Y == max value
    dice_information = command.split('d')
    num_dice = int(dice_information[0])
    dice_max = int(dice_information[1])
    print(command + ' : ' + str(roll(num_dice, dice_max)))
    print(rolls)

if __name__ == "__main__":
    main()