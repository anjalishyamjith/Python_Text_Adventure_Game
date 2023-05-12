from game import items
from utilities import partOne, addItem
from actions import *


def crossroad():
    write(
        "You arrive at a crossroad. On your right is the entrance to an unknown \
chamber. On your left, you see a maze of sacrophagi which seems vaguely \
familiar. Ahead, you see a dark passageway, at the end of which you see a \
light.\n"
    )
    write("You decide to go (right/left/ahead): ")
    route = input("> ").lower().strip()
    partOne(route)


def sealedChamber():
    write(
        "\nYou enter the unknown chamber. You shine your torch on the walls, which portrayed \
brilliant depictions of Egyptian afterlife and a lot of hieroglyphs."
    )
    write("\nWould you like to take a look at them? (Yes/No) ")
    examine = input("> ").lower().strip()
    if examine == "yes":
        examineWalls()
    elif examine == "no":
        write(
            "\nYou look at the walls some more and get bored. You decide to return to the \
crossroad."
        )
        crossroad()
    else:
        write("\nA little louder please...")
        sealedChamber()


def maze():
    write(
        "\nYou enter the maze of sacrophagi. You thought you had been there, but it was \
a whole new place. You look around, trying to find an exit. You hear a rustling \
behind you and turn around. You see a mummified carcass moving towards you, hands outstretched \
and smelling of rotten flesh."
    )
    write("\nDo you fight or flee? (Fight/Flee) ")
    response = input("> ").lower().strip()
    if response == "fight":
        write(
            "\nYou have nothing to fight with. You are paralyzed with fear as the beast \
comes at you. You face a horrible end to your courageous tale..."
        )
        dead()
    elif response == "flee":
        write(
            "\nYou try to run away from the mummy as it trudges behind you. You run aimlessly \
till you find an exit and escape."
        )
    else:
        write("\nI can't hear you. Say again?")
        maze()


def passageway():
    write(
        "\nYou go ahead and walk through the dark passageway. The air smells musty and \
cramped. At the end of the passageway, you step out into a chamber where you find a flaming \
torch."
    )
    write("\nDo you want to take the torch? (Yes/No) ")
    takeTorch = input("> ").lower().strip()
    if takeTorch == "yes":
        addItem("torch")
        write(
            "\nYou look around some more. You find that it is a dead end, so you head back to the \
crossroad."
        )
    elif takeTorch == "no":
        write(
            "\nYou leave the torch there and walk around. You find that it is a dead end, \
so you head back to the crossroad."
        )
    else:
        write("\nCome again?")
        passageway()
    crossroad()
