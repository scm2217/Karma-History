# The script of the game goes in this file.

python early:

    # store player data

    class PlayerHistory(object):
        def __init__(self):
            self.name = ''
            self.personality = {
            'nice': 0.0,  # mean to nice, 0 > = mean
            'social': 0.0,  # antisocial to social, 0 > = introverted
            'aggress': 0.0  # agressive to passive, 0 > = passive
            }
            self.stage = 'stage1'
            self.refTags = {
                'cLocation': '',
                'cAlliance': '',
                'cPerson': ''
            }

        def __eq__(self, other):
            if not other:
                return False
            if self.name != other.name:
                return False
            if self.stage != other.stage:
                return False
            if self.personality != other.personality:
                return False
            if self.refTags != other.refTags:
                return False
            return True

init python:
    if persistent.history is None:
        persistent.history = PlayerHistory()

    def resetHistory():
        persistent.history = PlayerHistory()


init:
    image Oberyn = "oberynFun.jpg"
    image Eddard = "eddard.jpg"
    image Tywin = "tywin.png"
    image bg Lannister = "lannister.jpg"
    image bg Martell = "martell.jpg"
    image bg Stark = "stark.jpg"

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

    $resetHistory()

    "It's game of thrones"

    # get player name
    $persistent.history.name = renpy.input("Pick a name:").strip()

    # calc initial player personality
    menu:
        "Your family is a minor vassal of house"

        "Lannister":
            $persistent.history.personality['nice'] -= 5
            $persistent.history.personality['social'] += 5
            $persistent.history.personality['aggress'] += 5
            $persistent.history.refTags['cAlliance'] = "Lannister"
            $persistent.history.refTags['cLocation'] = "Lannisport"
            scene bg Lannister

        "Stark":
            $persistent.history.personality['nice'] += 10
            $persistent.history.personality['social'] -= 5
            $persistent.history.refTags['cAlliance'] = "Stark"
            $persistent.history.refTags['cLocation'] = "Winterfell"
            scene bg Stark

        "Martell":
            $persistent.history.personality['social'] += 5
            $persistent.history.personality['aggress'] -= 10
            $persistent.history.refTags['cAlliance'] = "Martell"
            $persistent.history.refTags['cLocation'] = "Sunspear"
            scene bg Martell

    menu:
        "As a noble born child you:"

        "Tried your best to treat those considered below you with kindness":
            $persistent.history.personality['nice'] += 10

        "Used your status to torment the pathetic peasants when bored":
            $persistent.history.personality['nice'] -= 10

    menu:
        "During castle feasts you would:"

        "Play with the other children":
            $persistent.history.personality['social'] += 10

        "Sneak away as soon as you got the chance":
            $persistent.history.personality['social'] -= 10

    menu:
        "You felt that the combat training you were put through was:"

        "Exciting and prepared for any danger that came your way":
            $persistent.history.personality['aggress'] += 10

        "Uninteresting and a waste of your talents":
            $persistent.history.personality['aggress'] -= 10

    jump tree_start

    # This ends the game.

    return
