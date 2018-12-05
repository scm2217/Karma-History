init 1 python:
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
                preCons = story[0].pre_conditions
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
                if '$' in tg:  # $ tags are meant to be substituted during runtime
                    tags.remove(tg)
                    wEnd = ""
                    space = tg.split()
                    tg = space[0]
                    if len(space) > 1:
                        wEnd = " " + space[1]
                    tg = tg[1:]
                    tg = tg.split('.')
                    if len(tg) == 1:
                        tg = persistent.history.refTags[tg[0]] + wEnd
                    elif len(tg) == 2:
                        tg = persistent.history.refTags[tg[0]][tg[1]] + wEnd
                    tags.add(tg)
                if '~' in tg:  # ~ tags are meant to be used as a blocker
                    k = tg[1:]
                    if k in persistent.history.refTags:
                        tags.remove(tg)  # ~ blocker tag is is removed if event condition has been met
            return tags


        def getEvent(self, name):
            return random.choice(self.storyEvents[name])


        def getValidEventNames(self, postTags):
            postTags = self.parseTags(postTags)
            stories = []
            for preTags, names in self.storyByPre.items():
                if preTags >= postTags:
                    stories.extend(names)
            if not stories:
                for preTags, names in self.storyByPre.items():
                    if preTags >= frozenset([persistent.history.stage]):
                        newEvent = [name for name in names if name not in persistent.history.refTags]
                        # stories.extend(names)
                        stories.extend(newEvent)
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
            finalChoices = choices[:]
            for ch in choices:
                for attr, val in ch.personalityReq.items():
                    val = val[0]
                    if(val < 0 and personality[attr] > val):
                        finalChoices.remove(ch)
                        break
                    elif(val > 0 and personality[attr] < val):
                        finalChoices.remove(ch)
                        break
            return finalChoices

init 3 python:

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
                    word = persistent.history.refTags[word[0]][word[1]]
            result += word + " "
        result = result[:-1] + '.'
        return result


    def displayText(ev, act, person):
        txt = parseText(ev.content)

        if act:
            renpy.show(person.name)
            txt += " " + parseText(act.content)
            renpy.say(person.name, txt)
        else:
            renpy.say(None, txt)


    def getPlayerChoice(choices):
        # display and retieve choice here
        optionList = [(parseText(ch.content), [ch.name, ch.postTags, ch.personalityReq]) for ch in choices]
        playerChoice = menu(optionList)
        for attr, values in playerChoice[2].items():
            persistent.history.personality[attr] += values[1]
        return playerChoice


# update history data based on post tag commands
    def updateHistory(postT):
        for tg in postT:
            if "#" in tg:
                k = tg[1:]
                k = k.split('=')
                persistent.history.refTags[k[0]] = k[1]
                postT.remove(tg)
        return postT

    def executeEvent(name):
        ev = manager.getEvent(name)
        print("Event:", ev.name, ev.pre_conditions, ev.postTags)
        print("History:", persistent.history.refTags)
        persistent.history.refTags[ev.name] = { "action": "none", "person": "none", "choice": "none" }
        act, person = None, None
        if ev.actionTags != set([]):
            act, person = manager.getActionPerson(ev.actionTags)
            persistent.history.refTags[ev.name]["action"] = act.name
            persistent.history.refTags[ev.name]["person"] = person.name
            persistent.history.refTags['cPerson'] = person.name

        displayText(ev, act, person)
        postT = set(ev.postTags)
        choices = None
        if ev.choiceTags != set([]):
            choices = manager.getChoices(ev.choiceTags, persistent.history.personality)
        if choices:
            choiceResult = getPlayerChoice(choices)
            persistent.history.refTags[ev.name]["choice"] = choiceResult[0]
            if choiceResult[1] != set([]):
                postT |= choiceResult[1]
        if person:
            renpy.hide(person.name)
        postT = updateHistory(postT)
        print("Post Tags:", postT)
        return postT


    def pickEvent(post):
        validEvents = None
        if post:
            if set(['end']) in post:
                return
            validEvents = manager.getValidEventNames(post)
        # pick random event matchup pre-con
        else:
            print("Picking random event at current stage")
            validEvents = manager.getValidEventNames(persistent.history.stage)

        print("Possible Next Events:", validEvents)
        if(validEvents):
            return random.choice(validEvents)

    nextTags = None

label tree_start:
    "Sometime later..."
    $nextTags = executeEvent('start1')
    jump tree_event

label tree_event:
    $nextE = pickEvent(nextTags)
    if nextTags:
        $nextTags = executeEvent(nextE)
        jump tree_event
