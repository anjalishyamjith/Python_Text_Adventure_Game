import time
from game import items
from rooms import *


def write(string):  # TYPWRITER EFFECT
    for i in string:
        print(i, end="")
        time.sleep(0.03)
    time.sleep(0.5)
    print("")


def itemsCount():
    write("\nYour have " + str(len(items)) + " items in your inventory.")
    if len(items) > 0:
        c = 1
        for i in items:
            write(str(c) + ". " + i)
            c += 1


def addItem(item):
    if len(items) == 5:
        write("You have too many items in your inventory.")
        write("Would you like to drop any?")
        ans = input("> ").lower().strip()
        if ans == "yes":
            c = 1
            for i in items:
                write(str(c) + ". " + i)
                c += 1
            while True:
                write("\nEnter the item you want to drop:")
                dropped = input("> ")
                if dropped in items:
                    items.remove(dropped)
                    write(dropped.capitalize() + " removed from inventory.")
                    break
                else:
                    write(
                        "\nThe item you entered is not present in your inventory. Try again."
                    )
                addItem(item)
        else:
            write("\nNo items dropped, none gained...")
    else:
        items.append(item)
        write("\n" + item.capitalize() + " added to inventory.")


def partOne(route):
    if route == "right":
        sealedChamber()
    elif route == "left":
        maze()
    elif route == "ahead":
        passageway()
    else:
        write("\nThat wasn't clear. Could you repeat again?")
        crossroad()


def dead():
    write("\nGAME OVER")
    write(
        "\n---------------------------------------------------------------------------------"
    )
