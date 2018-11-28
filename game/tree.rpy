init python:
    import random

    class StoryEvent(object):
        def __init__(self, name, pre_conditions, content, tags, postTags=None):
            self.name = name
            self.pre_conditions = pre_conditions
            self.tags = tags
            self.content = content
            self.postTags = postTags


    class Person(object):
        def __init__(self, name, personality, tags):
            self.name = name
            self.personality = personality
            self.tags = tags


    class Action(object):
        def __init__(self, name, content, tags):
            self.name = name
            self.personality = personality
            self.tags = tags


    class Choice(object):
        def __init__(self, name, tags, personalityReq, postTags):
            self.name = name
            self.tags = tags
            self.personalityReq = personalityReq
            self.postTags = postTags


    class PlayerHistory(object):
        def __init__(self):
            self.eventsDone = set()
            self.choices = set()
            self.loyalty = ""


    class StoryManager(object):
        def __init__(self, storyEvents, people, actions, choices):
            self.storyEvents = storyEvents

            self.storyByPre = {}
            for name, story in storyEvents.items():
                preCons = story.pre_conditions
                if preCons not in self.storyByPre:
                    self.storyByPre[preCons] = []
                self.storyByPre[preCons].append(name)

            # organize people, actions, and choices by their tags
            self.people = {}
            for person in people:
                tags = person.tags
                if tags not in self.people:
                    self.people[tags] = []
                self.people[tags].append(person)

            self.actions = {}
            for act in actions:
                tags = act.tags
                if tags not in self.actions:
                    self.actions[tags] = []
                self.actions[tags].append(act)

            self.choices = {}
            for ch in choices:
                tags = ch.tags
                if tags not in self.choices:
                    self.choices[tags] = []
                self.choices[tags].append(act)


        def getEvent(self, name):
            return self.storyEvents[name]


        def getValidEventNames(self, doneTags):
            stories = []
            for subTags, names in self.StoryByPre.items():
                if subTags.issubtset(doneTags):
                    stories.extend(doneTags)
            return stories


        def getPerson(self, tags):
            people = []
            for superTags, vals in self.people.items():
                if tags.issubset(superTags):
                    people.extend(vals)

            if not people:
                return False
            return random.choice(people)


        def getActionPerson(self, tags):
            actions = []
            for superTags, vals in self.actions.items():
                if tags.issubset(superTags):
                    actions.extend(vals)

            # find a valid person action pair
            person = None
            random.shuffle(actions)
            for act in actions:
                person = self.getPerson(act.tags)
                if person:
                    return act, person
            # failed to find any actions with people left
            return False, False


        def getChoices(self, tags, personality):
            choices = []
            for superTags, vals in self.choices.items():
                if tags.issubset(superTags):
                    choices.extend(vals)

            # remove all choices that player cannot use
            for ch in choices:
                for attr, val in ch.items():
                    if(val < 0 and personality[attr] > val):
                        choices.remove(ch)
                    elif(val > 0 and personality[attr] < val):
                        choices.remove(ch)
            return choices

    history = PlayerHistory()

    actions = [
        Action('startQuest', 'Go hunt some bandits', frozenset(['Quest']))
    ]

    choices = [
        Choice('fight', frozenset('fight'), { 'aggress': 0.0 }, frozenset(['Aggress+']))
    ]

    people = [
        Person("Tywin", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Tywin', 'Lannister', 'Quest'])),
        Person("Eddard", { 'nice': 10.0, 'social': -5.0, 'aggress': 0.0 }, frozenset(['Stark', 'Eddard', 'Quest']))
    ]

    storyEvents = {
        'start': StoryEvent('start', 'None', 'Starting in Castle, may need grammar here', frozenset(['start']), None)
    }

    manager = StoryManager(storyEvents, people, actions, choices)

    def executeEvent(name):
        ev = manager.getEvent(name)
        act, person = manager.getActionPerson(ev.tags)
        if not person:
            print("We need to account for if there is no valid people for any valid actions")
            return  # temporary fix

        choices = manager.getChoices(act.tags)

    def pickEvent(post=None):
        if post:
            if post != 'end':
                executeEvent(post)
        # pick random event matchup pre-con
        else:
            validEvents = manager.getValidEventNames(history.done)


label tree_start:
    "Sometime later..."
    $history.loyalty = start
    $executeEvent('start')
