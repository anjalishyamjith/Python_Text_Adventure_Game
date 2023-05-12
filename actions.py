from game import items
from rooms import crossroad
from utilities import write, dead


def examineWalls():
    write(
        "\nYou examine the walls intently, hoping to find a clue about the artifact \
that you are after. Suddenly, you notice a picture that looks very similar to \
the artifact. You also find writings in hieroglyphs, which confirmed your \
hunch. You look at the adjacent wall, and finds some spells."
    )
    write("\nDo you want to recite the spells? (Yes/No) ")
    spells = input("> ").lower().strip()
    if spells == "yes":
        write(
            "\nYou decide to try the spells. You know that Egyptian spells are really \
dangerous when it comes to backfiring and a single mistake could might as well be \
the end of your journey."
        )
        confidence()
    elif spells == "no":
        write(
            "\nYou look at the walls some more and get bored. You decide to return to the \
crossroad."
        )
        crossroad()
    else:
        write("\nWhat was that again?")
        examineWalls()


def confidence():
    write("\nAre you confident that you can pull it off? (Yes/No) ")
    confidence = input("> ").lower().strip()
    if confidence == "yes":
        write(
            "\nYou recite the spells confidently, knowing that all the years of research \
has given you enough knowledge on hieroglyphs. As you reach the end of the spell, the \
hieroglyphs on the wall starts to glow and a small portion of the wall slides smoothly \
to reveal the artifact you were looking for! You pick it up and return back to the \
crossroad."
        )
        crossroad()
    elif confidence == "no":
        write(
            "\nYou recite the spells nervously, fear gripping your heart. Suddenly you falter, \
stumbling upon a word. The spell instantly backfires."
        )
        write("\nBOOM!")
        write("\nThat's the last thing you hear before your soul leaves your body.")
        write("\nSorry to break it to you, but you are DEAD....")
        dead()
