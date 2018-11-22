init python:
    import random


    class StoryEvent(object):
        def __init__(self, name, pre_conditions, tags, grammar, choices):
            self.name = name
            self.pre_conditions = pre_conditions
            self.tags = tags
            self.grammar = grammar


    class Person(object):
        def __init__(self, name, personality, rank, allegiance="None"):
            self.name = name
            self.personality = personality
            self.rank = rank
            self.allegiance = allegiance

        def relativeNice(self, personality):
            diff = 0
            mean = False
            if self.personality['nice'] < 0:
                mean = True
                diff = self.personality['nice'] - personality['nice']
            else:
                diff = personality['nice'] - self.personality['nice']
            return diff, mean


    class Choice(object):
        def __init__(self, dTag, content):
            self.dTag = dTag
            self.content = content


    class PlayerHistory(object):
        def __init__(self):
            self.eventsDone = set()
            self.choices = set()
            self.loyalty = ""


    history = PlayerHistory()

    people = {
        "Tywin": Person("Tywin", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, 10, "Lannister"),
        "Eddard": Person("Eddard", { 'nice': 10.0, 'social': -5.0, 'aggress': 0.0 }, 10, "Stark")
    }


    story = {
        "startLannister": StoryEvent("startLannister", set(),
        {
            'Leader': '',
            'DiffNice': 'Leader'
        },
        {
            'Event': 'Leader + \"calls you to the great hall of Casterly Rock.\" + Judgement + Task',
            'Judgement': 'DiffNice',
            'PosDiffNice': '\"You have served me well in the past, I have an important task for you.\"',
            'NegDiffNice': '\"I cannot afford to have any soft-hearted knights in my service. You shall have one last chance to prove yourself.\"',
            'Task': '\"I want you to make an example of the nearby bandits who dare raid Lannister territory.\"',
        },
        {
            'aggress': Choice("aggressProm1", "tbd....")
        }
        )
    }

    leaders = { "Lannister": "Tywin", "Stark": "Eddard" }


    def useGrammar(grammar, mem, skey):
        options = grammar[skey].split('|')
        tasks = random.choice(options).split('+')
        result = ''
        for task in tasks:
            task = task.strip()
            if task != '':
                if task[0] == '\"':
                    result += task[1:-1] + ' '
                elif task in mem:
                    if task == "Leader":
                        leader = leaders[history.loyalty]
                        mem["Leader"] = leader
                        result += leader + ' '
                    elif task == "DiffNice":
                        name = mem[mem[task]]
                        target = people[name]
                        diff, mean = target.relativeNice(personality)
                        if diff < -5:
                            result += useGrammar(grammar, mem, "NegDiffNice")
                        else:
                            result += useGrammar(grammar, mem, "PosDiffNice")
                else:
                    result += useGrammar(grammar, mem, task)
        return result

    def playEvent(name):
        current = story[name]
        e(useGrammar(current.grammar, current.tags, 'Event'))

label tree_start:
    "Sometime later..."
    $history.loyalty = start
    $playEvent('start'+history.loyalty)
