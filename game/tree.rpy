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
            tags = set(tags)
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
            return tags


        def getEvent(self, name):
            return self.storyEvents[name]


        def getValidEventNames(self, postTags):
            postTags = self.parseTags(postTags)
            stories = []
            for preTags, names in self.storyByPre.items():
                if preTags >= postTags:
                    stories.extend(names)
            return stories


        def getPerson(self, tags):
            tags = self.parseTags(tags)
            people = []
            for superTags, vals in self.people.items():
                if tags.issubset(superTags):
                    people.extend(vals)

            if not people:
                return False
            return random.choice(people)


        def getActionPerson(self, tags):
            tags = self.parseTags(tags)
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
            return None, None


        def getChoices(self, tags, personality):
            tags = self.parseTags(tags)
            choices = []
            for superTags, vals in self.choices.items():
                if tags <= superTags:
                    choices.extend(vals)

            # remove all choices that player cannot use
            for ch in choices:
                for attr, val in ch.personalityReq.items():
                    if(val < 0 and personality[attr] > val):
                        choices.remove(ch)
                    elif(val > 0 and personality[attr] < val):
                        choices.remove(ch)
            return choices

    storyEvents = {
        'start1': StoryEvent(
            'start1',
            frozenset(),
            'It is a beutiful day in $cLocation',
            frozenset(['chill', 'leader']),
            frozenset(['noOption']),
            frozenset(['quest1', 'leader', 'startQuest'])
        ),

        'start1b': StoryEvent(
            'start1b',
            frozenset(['quest1', 'leader', 'startQuest', 'hunt']),
            'In conversation he offers you a quest',
            frozenset(['quest1', 'startQuest', 'hunt']),
            frozenset(['noOption']),
            frozenset(['quest2', 'startQuest'])
        ),

        'start1c': StoryEvent(
            'start1c',
            frozenset(['quest2', 'startQuest', 'hunt']),
            'You accept the challenge.',
            frozenset(['prepare', 'hunt']),
            frozenset(['noOption']),
            frozenset(['quest3', 'startQuest', 'weaponChoice'])
        ),

        'start1d': StoryEvent(
            'start1d',
            frozenset(['quest3', 'weaponChoice', 'startQuest']),
            'But you realize that you are packing too heavy.',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['quest4', 'startQuest'])
        ),

        'start1e': StoryEvent(
            'start1e',
            frozenset(['quest4', 'startQuest']),
            'You ride into the night to go hunting. Your horse breathes heavy while galloping.',
            frozenset([]),
            frozenset(['noOption']),
            frozenset(['huntResult', 'startQuest'])
        ),

        'red1a': StoryEvent(
            'red1a',
            frozenset(['quest4', 'startQuest']),
            'You make your way down to the stables when suddenly a figure in red blocks your way.',
            frozenset(['redThreat', '$cAlliance']),
            frozenset(['noOption']),
            frozenset(['redThreat', 'startQuest'])
        ),

        'start1f': StoryEvent(
            'start1f',
            frozenset(['huntResult', 'startQuest']),
            'You catch your prey',
            frozenset(['barter', 'life']),
            frozenset(['spare', 'kill'])
        ),

        'quest1a': StoryEvent(
            'quest1a',
            frozenset(['stage1']),
            'You are walking down a street when a mysterious man jumps out at you',
            frozenset([]),
            frozenset(['noOption']),
            frozenset(['surprise', 'attack', 'defense'])
        ),

        'quest1b': StoryEvent(
            'quest1b',
            frozenset(['surprise', 'attack', 'defense']),
            'You side step and parry his attack. He challenges you to a duel, what do you do?',
            frozenset([]),
            frozenset(['negotiate', 'fight'])
        ),

        'quest1c': StoryEvent(
            'quest1c',
            frozenset(['negotiate', 'fight', 'prepareToFight']),
            'You lunge at his heart, he takes it and dies',
            frozenset([]),
            frozenset(['noOption']),
            frozenset(['revival'])
        ),

        'qeust1d': StoryEvent(
            'qeust1d',
            frozenset(['revival']),
            'But then he revives himself and screaming \'The Lord of the Light!\' What do you do?',
            frozenset([]),
            frozenset(['fight', 'options']),
            frozenset(['endQuest'])
        ),

        'qeust1e': StoryEvent(
            'quest1e',
            frozenset(['huntResult', 'startQuest']),
            'You catch your prey',
            frozenset(['barter', 'life']),
            frozenset(['spare', 'kill']),
            frozenset(['endQuest'])
        ),


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
            'prep',
            'You sharpen your sword, and ready your bows, preparing for the hunt.',
            frozenset(['prepare', 'hunt']),
            set(['$cPerson'])
        ),
        Action(
            'weaponChoice',
            'Do you want your bow, or do you want your sword?',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            set(['$cPerson'])
        ),
        Action(
            'moneyForLife',
            '$cPerson offers you a great reward if you spare his life',
            frozenset(['barter', 'life']),
            set(['$cPerson'])
        ),
        Action(
            'redStarkThreat',
            'He exclaims: /"Nothern dog, you will burn with your false tree gods!/"',
            frozenset(['redThreat', 'Stark']),
            set(['redpriest'])
        ),
        Action(
            'redLannisterThreat',
            'He exclaims: /"The lord of light will smite down you and your greedy masters!/"',
            frozenset(['redThreat', 'Lannister']),
            set(['redpriest'])
        ),
        Action(
            'redMartellThreat',
            'He exclaims: /"The sins of a filthy dornishman can only be cleansed by fire!/"',
            frozenset(['redThreat', 'Martell']),
            set(['redpriest'])
        ),
    ]

    choices = [
        Choice(
            'bowPick',
            'I need range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'social': [-5, 0] },
            set([])
        ),
        Choice(
            'swordPick',
            'I need to be able to fight close range',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': [0, 0] },
            set([])
        ),
        Choice(
            'handsPick',
            'Forget those weapons, I\'m going to use my thumbs.',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            { 'aggress': [10, 5] },
            set([])
        ),
        Choice(
            'cutHeadOff',
            'You cut his head off.',
            frozenset(['spare', 'kill']),
            { 'aggress': [0, 5] },
            set(['killed'])
        ),
        Choice(
            'spare',
            'You let him run for his life.',
            frozenset(['spare', 'kill']),
            { 'aggress': [0, -5], 'nice': [0, 5] },
            set(['spared'])
        ),
        Choice(
            'arrowToKnee',
            'You shoot him in the knee with an arrow.',
            frozenset(['spare', 'kill']),
            { 'aggress': [10, 5] },
            set(['killed'])
        ),
        Choice(
            'peacefulFightNegotiation',
            'You try to talk him out of the fight',
            frozenset(['peaceful', 'fight', 'negotiation']),
            { 'aggress': [0, -5], 'social': [0, 5] },
            set(['talk'])
        ),
        Choice(
            'aggressiveFightNegotiation',
            'You raise your sword to prepare for the fight',
            frozenset(['aggressive', 'fight', 'negotiation']),
            { 'aggress': [0, 5] },
            set(['prepareToFight'])
        ),
    ]

    people = [
        Person("Tywin", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Tywin', 'leader', 'Lannister', 'Lannisport', 'quest'])),
        Person("Eddard", { 'nice': 10.0, 'social': -5.0, 'aggress': 0.0 }, frozenset(['Eddard', 'leader', 'Stark', 'Winterfell', 'quest'])),
        Person("Oberyn", { 'nice': 10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Oberyn', 'leader', 'Martell', 'Sunspear', 'quest'])),
        Person("The Boulder", { 'nice': -10.0, 'social': 5.0, 'aggress': 10.0 }, frozenset(['The Boulder', 'banditLead'])),
        Person("The Pup", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['The Pup', 'banditLead'])),
        Person("Thoros of Myr", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Thoros of Myr', 'redpriest'])),
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
        optionList = [(ch.content, [ch.name, ch.postTags, ch.personalityReq]) for ch in choices]
        playerChoice = menu(optionList)
        for attr, values in playerChoice[2].items():
            persistent.history.personality[attr] += values[1]
        return playerChoice


    def executeEvent(name):
        ev = manager.getEvent(name)
        persistent.history.refTags[ev.name] = { "action": "none", "person": "none", "choice": "none" }
        act, person = None, None
        if ev.actionTags != set():
            act, person = manager.getActionPerson(ev.actionTags)
            persistent.history.refTags[ev.name]["action"] = act.name
            persistent.history.refTags[ev.name]["person"] = person.name

        displayText(ev, act, person)
        postT = set(ev.postTags)
        choices = manager.getChoices(ev.choiceTags, persistent.history.personality)
        if choices:
            choiceResult = getPlayerChoice(choices)
            persistent.history.refTags[ev.name]["choice"] = choiceResult[0]
            if choiceResult[1] != set():
                postT |= choiceResult[1]
        if person:
            renpy.hide(person.name)
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
