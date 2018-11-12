# The script of the game goes in this file.

init python:

    # store player data
    name = ""
    personality = {
    'nice': 0.0,  # mean to nice, 0 > = mean
    'social': 0.0,  # antisocial to social, 0 > = introverted
    'agress': 0.0  # agressive to passive, 0 > = passive
    }


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Background intro to the world"

    # get player nameW
    $name = renpy.input("Pick a name:").strip()

    # calc initial player personality
    menu:
        "Mean/Nice Choice"

        "Do something nice":
            $personality['nice'] += 1

        "Do something mean":
            $personality['nice'] -= 1

    menu:
        "Social/Antisocial choice"

        "Do something social":
            $personality['social'] += 1

        "Do something antisocial":
            $personality['social'] -= 1

    menu:
        "Agressive/passive choice"

        "Do something agressive":
            $personality['agress'] += 1

        "Do something passive":
            $personality['agress'] -= 1

    jump tree_start

    # This ends the game.

    return
