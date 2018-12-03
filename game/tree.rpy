init python:
    import random

    class StoryEvent(object):
        def __init__(self, name, pre_conditions, content, actionTags, choiceTags, postTags=set()):
            self.name = name
            self.pre_conditions = pre_conditions
            self.actionTags = actionTags
            self.choiceTags = choiceTags
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


        def parseTags(self, tags):
            for tg in tags:
                if '$' in tg:
                    tags.remove(tg)
                    tg = tg[1:]
                    tg = tg.split('.')
                    if len(tg) == 1:
                        tg = persistent.history.refTags[tg[0]]
                    elif len(tg) == 2:
                        tg = persistent.history.refTags[tg[0][1]]
                    tags.add(tg)


        def getEvent(self, name):
            return self.storyEvents[name]


        def getValidEventNames(self, postTags):
            self.parseTags(postTags)
            stories = []
            for preTags, names in self.storyByPre.items():
                if preTags >= postTags:
                    stories.extend(names)
            return stories


        def getPerson(self, tags):
            self.parseTags(tags)
            people = []
            for superTags, vals in self.people.items():
                if tags.issubset(superTags):
                    people.extend(vals)

            if not people:
                return False
            return random.choice(people)


        def getActionPerson(self, tags):
            self.parseTags(tags)
            actions = []
            for superTags, vals in self.actions.items():
                if tags <= superTags:
                    actions.extend(vals)

            # find a valid person action pair
            person = None
            random.shuffle(actions)
            for act in actions:
                person = self.getPerson(act.personTags)
                if person:
                    return act, person
            # failed to find any actions with people left
            return False, False


        def getChoices(self, tags, personality):
            self.parseTags(tags)
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
            'It is a beutiful day in $cLocation',
            frozenset(['chill', 'leader']),
            frozenset(['none']),
            frozenset(['quest1', 'leader', 'startQuest'])
        ),

        'start1b': StoryEvent(
            'start1b',
            frozenset(['quest1', 'leader', 'startQuest', 'hunt']),
            'In conversation he offers you a quest',
            frozenset(['quest1', 'startQuest', 'hunt']),
            frozenset(['none']),
            frozenset(['quest2', 'startQuest'])
        ),

        'start1c': StoryEvent(
            'start1c',
            frozenset(['quest2', 'startQuest', 'hunt']),
            'You accept the challenge.',
            frozenset(['prepare', 'hunt']),
            frozenset(['none']),
            frozenset(['quest3', 'startQuest', 'weaponChoice'])
        ),

        'start1d': StoryEvent(
            'start1d',
            frozenset(['quest3', 'weaponChoice', 'startQuest']),
            'You realize that you are packing too heavy.',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['quest4', 'startQuest'])
        )
    }

    actions = [
        Action(
            'relaxLeader',
            'You\'re kickin it with $cPerson',
            frozenset(['chill', 'leader']),
            set(['leader', '$cLocation'])
        ),
        Action(
            'startQuest',
            '$cPerson requets for you to hunt bandits in exchange for gold',
            frozenset(['quest1', 'startQuest', 'hunt']),
            set(['leader', '$cLocation'])
        ),
        Action(
            'startQuest',
            'you sharpen your sword, and ready your bows, preparing for the hunt',
            frozenset(['prepare', 'hunt']),
            set(['leader'])
        ),
        Action(
            'startQuest',
            'Do you want your bow?, or do you want your sword',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            set(['leader'])
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
                word = word[1:]
                word = word.split('.')
                if len(word) == 1:
                    word = persistent.history.refTags[word[0]]
                elif len(word) == 2:
                    word = persistent.history.refTags[word[0][1]]
            result += word + " "
        result = result[:-1] + '.'
        return result


    def displayText(ev, act, person):
        txt = parseText(ev.content)
        if act:
            renpy.show(person.name)
            persistent.history.refTags['cPerson'] = person.name
            txt += " " + parseText(act.content)
            renpy.say(person.name, txt)
        else:
            renpy.say(None, txt)


    def getPlayerChoice(choices):
        # display and retieve choice here
        optionList = [(ch.content, [ch.name, ch.postTags]) for ch in choices]
        playerChoice = menu(optionList)
        return playerChoice


    def executeEvent(name):
        ev = manager.getEvent(name)
        persistent.history.refTags[ev.name] = { "action": "none", "person": "none", "choice": "none" }
        act, person = None, None
        if len(ev.actionTags) > 0:
            act, person = manager.getActionPerson(ev.actionTags)
            persistent.history.refTags[ev.name]["action"] = act.name
            persistent.history.refTags[ev.name]["person"] = person.name

        displayText(ev, act, person)
        choices = manager.getChoices(ev.choiceTags, persistent.history.personality)
        if choices:
            choiceResult = getPlayerChoice(choices)
            persistent.history.refTags[ev.name]["choice"] = choiceResult[0]
            pickEvent(choiceResult[1])
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
