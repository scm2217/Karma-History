init 2 python:
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

        'start1b': StoryEvent(
            'start1b',
            frozenset(['quest1', 'leader', 'startQuest', 'hunt']),
            'In conversation he offers you a quest',
            frozenset(['quest1', 'startQuest', 'hunt']),
            frozenset(['noOption']),
            frozenset(['quest2', 'startQuest'])
        ),

        'start1b': StoryEvent(
            'start1b',
            frozenset(['quest1', 'leader', 'startQuest', 'hunt']),
            'While joking about the good old days, $cPerson leans in to ask you something',
            frozenset(['quest1', 'startQuest', 'hunt']),
            frozenset(['agree']),
            frozenset(['quest3', 'startQuest'])
        ),


        'start1d': StoryEvent(
            'start1d',
            frozenset(['quest3', 'weaponChoice', 'startQuest']),
            'But you realize that you are packing too heavy.',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            frozenset(['quest4', 'startQuest'])
        ),

        'start1d': StoryEvent(
            'start1d',
            frozenset(['quest3', 'weaponChoice', 'startQuest']),
            'You life the bag, the weapons clank together. You realize you must travel light for stealth',
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

        'start1e': StoryEvent(
            'start1e',
            frozenset(['quest4', 'startQuest']),
            'You start making your way to your target.',
            frozenset([]),
            frozenset(['noOption']),
            frozenset(['huntResult', 'startQuest'])
        ),


        'start1f': StoryEvent(
            'start1f',
            frozenset(['huntResult', 'startQuest']),
            'You quickly find the brigands, and their leader approaches you',
            frozenset(['barter', 'life']),
            frozenset(['spare', 'kill'])
        ),

        'red1a': StoryEvent(
            'red1a',
            frozenset(['quest4', 'startQuest']),
            'You make your way down to the stables when suddenly a figure in red blocks your way.',
            frozenset(['redThreat', '$cAlliance']),
            frozenset(['noOption']),
            frozenset(['negotiate', 'fight'])
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
            'But then he revives himself and screams \'The Lord of the Light!\' What do you do?',
            frozenset([]),
            frozenset(['fight', 'options']),
            frozenset(['revival'])
        ),
        'firefight': StoryEvent(
            'firefight',
            frozenset(['revival', 'norm']),
            'He gets up again. "FOOL! You can never hope to kill me!"',
            frozenset([]),
            frozenset(['fight', 'options']),
            frozenset(['revival'])
        ),
        'firefight': StoryEvent(
            'firefight',
            frozenset(['revival', 'norm']),
            'He gets up again. "Stop wasting your time, I cannot be struck down by a nonbeliever!"',
            frozenset([]),
            frozenset(['fight', 'options']),
            frozenset(['revival'])
        ),
        'firefight': StoryEvent(
            'firefight',
            frozenset(['revival', 'norm']),
            'He gets up again. "I cannot lose so long as the Lord of the light is by my side!"',
            frozenset([]),
            frozenset(['fight', 'options']),
            frozenset(['revival'])
        ),
        'firefight': StoryEvent(
            'firefightJoin',
            frozenset(['revival', 'norm']),
            'This time $cPerson pauses. "Maybe you are worthy. You have seen my power, will you renounce your false leaders and join the lord of light?"',
            frozenset([]),
            frozenset(['join', 'reject']),
            frozenset(['firefight'])
        ),
        'firefightJoin': StoryEvent(
            'firefightJoin',
            frozenset(['join', 'firefight']),
            'You pledge yourself to the lord of light and renounce the $cAlliance .',
            frozenset([]),
            frozenset([]),
            frozenset(['endQuest'])
        ),
        'firefight': StoryEvent(
            'firefightDead',
            frozenset(['revival', 'crit', 'dead']),
            'The foul fire heathen finally falls to your blade, his lifeless head rolling on the ground.',
            frozenset([]),
            frozenset([]),
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
        'qeust1e': StoryEvent(
            'quest1e',
            frozenset(['huntResult', 'startQuest']),
            'Noticing your target, on the move, you pounce from above',
            frozenset(['barter', 'life']),
            frozenset(['spare', 'kill']),
            frozenset(['endQuest'])
        ),
        'end1': StoryEvent(
            'end1',
            frozenset(['endQuest', 'crit']),
            'You return to $cLocation .',
            frozenset([]),
            frozenset([]),
            frozenset([])
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
            'relaxLeader',
            'You are in the dining hall, feasting with $cPerson',
            frozenset(['chill', 'leader']),
            set(['leader', '$cLocation'])
        ),
        Action(
            'relaxLeader',
            'You are taking a walk with $cAlliance \'s leader, $cPerson',
            frozenset(['chill', 'leader']),
            set(['leader', '$cAlliance'])
        ),
        Action(
            'startQuest',
            '$cPerson requests for you to hunt bandits in exchange for gold',
            frozenset(['quest1', 'startQuest', 'hunt']),
            set(['leader', '$cLocation'])
        ),
        Action(
            'startQuest',
            '$cPerson exclaims the trouble they have had with a particular group of people. $cPerson offers you gold for your services',
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
            'prep',
            'You do a few pushups to get a good pump',
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
            'weaponChoice',
            'Will you attack from afar, or will you fight honorably?',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            set(['$cPerson'])
        ),
        Action(
            'weaponChoice',
            'Will you utilize distance, or will you charge in?',
            frozenset(['question', 'weaponChoice', 'bow', 'arrow']),
            set(['$cPerson'])
        ),
        Action(
            'moneyForLife',
            'Looking closer, you realize it\'s $cPerson , who offers you a great reward if you just leave',
            frozenset(['barter', 'life']),
            set(['weak', 'calm', 'rich'])
        ),
        Action(
            'moneyForLife',
            'The person instanly begs for their life. They state their name to be $cPerson , and offers you a great reward if you spare their life',
            frozenset(['barter', 'life']),
            set(['weak', 'calm', 'rich'])
        ),
        Action(
            'redStarkThreat',
            'He exclaims: "Nothern dog, you will burn with your false tree gods!"',
            frozenset(['redThreat', 'Stark']),
            set(['redpriest'])
        ),
        Action(
            'redStarkThreat',
            'He exclaims: "Nothern fool, winter is ending!"',
            frozenset(['redThreat', 'Stark']),
            set(['redpriest'])
        ),
        Action(
            'redLannisterThreat',
            'He exclaims: "The lord of light will put you in so much debt, you can\'t repay it!"',
            frozenset(['redThreat', 'Lannister']),
            set(['redpriest'])
        ),
        Action(
            'redMartellThreat',
            'He exclaims: "The sins of a filthy dornishman can only be cleansed by fire!"',
            frozenset(['redThreat', 'Martell']),
            set(['redpriest'])
        ),
    ]

    choices = [
        Choice(
            'agreeLow',
            'After some convincing, you begrudingly agree',
            frozenset(['agree']),
            { 'social': [-5, 1] },
            set([])
        ),
        Choice(
            'agree',
            'You accept the challenge',
            frozenset(['agree']),
            { 'social': [0, 1] },
            set([])
        ),
        Choice(
            'bowPick',
            'This enemy might be dangerous, I should keep my distance and use my bow.',
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
            'swordPick',
            'This is the only honorable option',
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
            'cutHeadOff',
            'You swipe your sword, resulting in a head on the floor.',
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
            'spare',
            'You need the money. You let $cPerson get away',
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
        Choice(
            'crit',
            'You cut his head off.',
            frozenset(['fight', 'options']),
            { 'aggress': [10, 1] },
            set(['crit'])
        ),
        Choice(
            'normal',
            'You land a large strike across $cPerson \'s chest',
            frozenset(['fight', 'options']),
            { 'aggress': [0, 1] },
            set(['norm'])
        ),
        Choice(
            'run',
            'You pee in your pants and run the other way.',
            frozenset(['fight', 'options']),
            { 'aggress': [-1, -5] },
            set(['run'])
        ),
        Choice(
            'join',
            'You pee in your pants and run the other way.',
            frozenset(['reject', 'join']),
            { 'social': [0, -5] },
            set(['accept'])
        ),
        Choice(
            'join',
            'You scramble to escape and run the other way.',
            frozenset(['reject', 'join']),
            { 'social': [0, -5] },
            set(['accept'])
        ),
        Choice(
            'join',
            'You slowly back away, and then sprint the other way as fast as you can',
            frozenset(['reject', 'join']),
            { 'social': [0, -5] },
            set(['accept'])
        ),
        Choice(
            'reject',
            'You reject $cPerson \'s foul scheming.',
            frozenset(['reject', 'join']),
            { 'aggress': [0, 5] },
            set(['reject'])
        ),
    ]

    people = [
        Person("Tywin", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Tywin', 'leader', 'Lannister', 'Lannisport', 'quest'])),
        Person("Eddard", { 'nice': 10.0, 'social': -5.0, 'aggress': 0.0 }, frozenset(['Eddard', 'leader', 'Stark', 'Winterfell', 'quest'])),
        Person("Oberyn", { 'nice': 10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Oberyn', 'leader', 'Martell', 'Sunspear', 'quest'])),
        Person("The Boulder", { 'nice': -10.0, 'social': 5.0, 'aggress': 10.0 }, frozenset(['The Boulder', 'banditLead'])),
        Person("The Pup", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['The Pup', 'banditLead', 'weak', 'calm', 'rich'])),
        Person("Thoros of Myr", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Thoros of Myr', 'redpriest'])),
        Person("Samwell Tarly", { 'nice': 10.0, 'social': -10.0, 'aggress': -10.0 }, frozenset(['Samwell Tarly', 'weak', 'rich', 'kind', 'calm'])),
        Person("Viserys Targaryen", { 'nice': -10.0, 'social': 10.0, 'aggress': 10.0 }, frozenset(['Viserys Targaryen', 'weak', 'rich', 'brat', 'calm'])),
        Person("Lyssa Arryn", { 'nice': -10.0, 'social': -10.0, 'aggress': 10.0 }, frozenset(['Lyssan Arryn', 'weak', 'rich', 'psycho', 'calm'])),
        Person("HIZDAHR ZO LORAQ", { 'nice': -10.0, 'social': 10.0, 'aggress': -10.0 }, frozenset(['HIZDAHR ZO LORAQ', 'weak', 'rich', 'pompous', 'calm'])),
    ]