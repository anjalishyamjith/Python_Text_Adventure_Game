"""TEXT-ADVENTURE GAME"""

# IMPORTS

from rooms import *
from utilities import *


# GAME EXECUTION
write(
    """Hi!
Welcome to TEXT-ADVENTURE GAME, where you can follow \
along a storyline and make decisions which will decide your fate."""
)

while True:
    write("Firstly, may I know your name?")
    name = input("> ").capitalize()
    if name.strip() == "":
        write("That's not a name!")
        continue
    else:
        break


while True:
    write("\nAlright " + name + ", would you like to play? (Yes/No)")
    start = input("> ")
    if start.lower().strip() == "yes":
        items = ["item1", "item2", "item3", "item4", "item5"]
        print("")
        write("\nEGYPTIAN ADVENTURE")
        write("------------------")
        itemsCount()
        write("You can carry a maximum of 5 items with you at a time.")
        write(
            "\nYou are an archaeologist traversing through the catacombs in the heart of Egypt \
in search of a precious artifact. After a while, you realise that you are lost."
        )
        crossroad()
    elif start.lower().strip() == "no":
        write("\nWell, goodbye then. Hope to see you again!")
        break
    else:
        write("\nPardon?")
        continue
