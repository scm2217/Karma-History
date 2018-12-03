init python:
    import random

    class StoryEvent(object):
        def __init__(self, name, pre_conditions, content, tags, postTags=set()):
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
        def __init__(self, name, content, tags, personTags):
            self.name = name
            self.content = content
            self.tags = tags
            self.personTags = personTags


    class Choice(object):
        def __init__(self, name, content, tags, personalityReq, postTags):
            self.name = name
            self.content = content
            self.tags = tags
            self.personalityReq = personalityReq
            self.postTags = postTags


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
                self.choices[tags].append(ch)


        def getEvent(self, name):
            return self.storyEvents[name]


        def getValidEventNames(self, postTags):
            stories = []
            for preTags, names in self.storyByPre.items():
                if preTags >= postTags:
                    stories.extend(names)
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
                if tags <= superTags:
                    actions.extend(vals)

            # find a valid person action pair
            person = None
            random.shuffle(actions)
            for act in actions:
                personTags = act.personTags
                for pTag in personTags:
                    if '$' in pTag:
                        personTags.remove(pTag)
                        pTag = persistent.history.refTags[pTag[1:]]
                        personTags.add(pTag)
                person = self.getPerson(personTags)
                if person:
                    return act, person
            # failed to find any actions with people left
            return False, False


        def getChoices(self, tags, personality):
            choices = []
            for superTags, vals in self.choices.items():
                if tags <= superTags:
                    choices.extend(vals)

            # remove all choices that player cannot use
            for ch in choices:
                for attr, val in ch.personalityReq.items():
                    if(val < 0 and personality[attr] > val):
                        choices.remove(ch)
                    elif(val >= 0 and personality[attr] < val):
                        choices.remove(ch)
            return choices


    storyEvents = {
        'start1': StoryEvent(
            'start1',
            frozenset(),
            'It is a beutiful day in $location',
            frozenset(['chill', 'leader']),
            frozenset(['quest1', 'leader', 'startQuest'])
        ),

        'start1b': StoryEvent(
            'start1b',
            frozenset(['quest1', 'leader', 'startQuest', 'hunt']),
            'In conversation he offers you a quest',
            frozenset(['quest1', 'startQuest', 'hunt']),
            frozenset(['quest2', 'startQuest'])
        ),

        'start1c': StoryEvent(
            'start1c',
            frozenset(['quest2', 'startQuest', 'hunt']),
            'You accept the challenge.',
            frozenset(['prepare', 'hunt']),
            frozenset(['quest3', 'startQuest', 'weaponChoice'])
        ),

        'start1d': StoryEvent(
            'start1d',
            frozenset(['quest3', 'weaponChoice', 'startQuest']),
            'You realize that you are packing too heavy.',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['quest4', 'startQuest'])
        )
    }

    actions = [
        Action(
            'relaxLeader',
            'You\'re kickin it with $cPerson',
            frozenset(['chill', 'leader']),
            set(['leader', '$location'])
        ),
        Action(
            'startQuest',
            '$cPerson requets for you to hunt bandits in exchange for gold',
            frozenset(['quest1', 'startQuest', 'hunt']),
            set(['leader', '$location'])
        ),
        Action(
            'startQuest',
            'you sharpen your sword, and ready your bows, preparing for the hunt',
            frozenset(['prepare', 'hunt']),
            set()
        ),
        Action(
            'startQuest',
            'Do you want your bow?, or do you want your sword',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            set()
        )
    ]

    choices = [
        Choice(
            'bowPick',
            'I need range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'social': 0.0 },
            set(['social+'])
        ),
        Choice(
            'arrowPick',
            'I need to be able to fight close range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': 2 },
            set(['aggress+'])
        ),
        Choice(
            'handsPick',
            'forget those weapons, i\'m going to use my thumbs',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': 3},
            set(['social+'])
        ),
        Choice(
            'bowPick',
            'I need range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'social': 0.0 },
            set(['social+'])
        ),
        Choice(
            'arrowPick',
            'I need to be able to fight close range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': -1 },
            set(['aggress-'])
        ),
        Choice(
            'handsPick',
            'forget those weapons, i\'m going to use my thumbs',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': -1},
            set(['social-'])
        )
    ]

    people = [
        Person("Tywin", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Tywin', 'leader', 'Lannister', 'Lannisport', 'quest'])),
        Person("Eddard", { 'nice': 10.0, 'social': -5.0, 'aggress': 0.0 }, frozenset(['Eddard', 'leader', 'Stark', 'Winterfell', 'quest'])),
        Person("Oberyn", { 'nice': 10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Oberyn', 'leader', 'Martell', 'Sunspear', 'quest'])),
        Person("The Bolder", { 'nice': -10.0, 'social': 5.0, 'aggress': 10.0 }, frozenset(['banditLead'])),
        Person("The Pup", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['banditLead'])),
    ]

    manager = StoryManager(storyEvents, people, actions, choices)

    def parseText(txt):
        result = ""
        for word in txt.split():
            word = str(word)
            if '$' in word:
                word = persistent.history.refTags[word[1:]]
            result += word + " "
        result = result[:-1] + '.'
        return result


    def displayText(ev, act, person):
        # can use substitutions to make test better very basic for now
        persistent.history.refTags['cPerson'] = person.name
        txt = parseText(ev.content) + " " + parseText(act.content)
        renpy.say(person.name, txt)


    def getPlayerChoice(evf, act, person, choices):
        # display and retieve choice here
        optionList = [(ch.content, ch.postTags) for ch in choices]
        playerChoice = menu(optionList)
        return playerChoice


    def executeEvent(name):
        ev = manager.getEvent(name)
        act, person = manager.getActionPerson(ev.tags)
        if not person:
            renpy.say(None, "We need to account for if there is no valid people for any valid actions")
            return  # temporary fix
        displayText(ev, act, person)
        choices = manager.getChoices(act.tags, persistent.history.personality)
        if choices:
            choiceResult = getPlayerChoice(ev, act, person, choices)
            pickEvent(choiceResult)
        else:
            postT = ev.postTags
            pickEvent(postT)


    def pickEvent(post):
        validEvents = None
        if post:
            if set(['end']) in post:
                return
            validEvents = manager.getValidEventNames(post)
        # pick random event matchup pre-con
        else:
            validEvents = manager.getValidEventNames(persistent.history.stage)

        if(validEvents):
            executeEvent(random.choice(validEvents))

label tree_start:
    "Sometime later..."
    $executeEvent('start1')
