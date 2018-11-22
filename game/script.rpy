# The script of the game goes in this file.

init python:

    # store player data
    name = ""
    personality = {
    'nice': 0.0,  # mean to nice, 0 > = mean
    'social': 0.0,  # antisocial to social, 0 > = introverted
    'aggress': 0.0  # agressive to passive, 0 > = passive
    }
    start = ""


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
        "Your family is a minor vassal of house"

        "Lannister":
            $personality['nice'] -= 5
            $personality['social'] += 5
            $personality['aggress'] += 5
            $start = "Lannister"

        "Stark":
            $personality['nice'] += 10
            $personality['social'] -= 5
            $start = "Stark"

        "Martell":
            $personality['social'] += 5
            $personality['aggress'] -= 10
            $start = "Martell"

        "Arryn":
            $personality['social'] -= 5
            $personality['aggress'] -= 10
            $start = "Arryn"

        "Baratheon":
            $personality['nice'] += 5
            $personality['social'] += 5
            $personality['aggress'] += 5
            $start = "Baratheon"

        "Greyjoy":
            $personality['nice'] -= 5
            $personality['social'] -= 5
            $personality['aggress'] += 5
            $start = "Greyjoy"

        "Tyrell":
            $personality['social'] += 10
            $personality['aggress'] += 5
            $start = "Tyrell"

    menu:
        "As a noble born child you:"

        "Tried your best to treat those considered below you with kindness":
            $personality['nice'] += 10

        "Used your status to torment the pathetic peasants when bored":
            $personality['nice'] -= 10

    menu:
        "During castle feasts you would:"

        "Play with the other children":
            $personality['social'] += 10

        "Sneak away as soon as you got the chance":
            $personality['social'] -= 10

    menu:
        "You felt that the combat training you were put through was:"

        "Exciting and prepared for any danger that came your way":
            $personality['aggress'] += 10

        "Uninteresting and a waste of your talents":
            $personality['aggress'] -= 10

    jump tree_start

    # This ends the game.

    return
