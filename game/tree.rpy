init python:
    import random

    curAct = "tree_start"

    actNice = set(['niceSmall1', 'niceSmall2','niceSmall3','niceSmall4','niceSmall5', "niceBig1","niceBig2","niceBig3"])
    actMean = set(['meanSmall1', 'meanSmall2','meanSmall3','meanSmall4','meanSmall5', "meanBig1","meanBig2","meanBig3"])
    actSocial = set(['socialSmall1', 'socialSmall2','socialSmall3','socialSmall4','socialSmall5', "socialBig1","socialBig2","socialBig3"])
    actAntiSo = set(['antisoSmall1', 'antisoSmall2','antisoSmall3','antisoSmall4','antisoSmall5', "antisoBig1","antisoBig2","antisoBig3"])
    actAgress = set(['agressSmall1', 'agressSmall2','agressSmall3','agressSmall4','agressSmall5', "agressBig1","agressBig2","agressBig3"])
    actPass = set(['passSmall1', 'passSmall2','passSmall3','passSmall4','passSmall5', "passBig1","passBig2","passBig3"])

    mainDrama = ""
    mainConflict = ""
    mainConclusion = ""

    def genOptions():
        options = set()
        # make sure at least 2 actions follow player's current personality
        for i in range (0, 2):
            base, val = random.choice(personality.items())
            if base == 'nice':
                if val > 0:
                    options.add(actNice.pop())
                else:
                    options.add(actMean.pop())
            elif base == 'social':
                if val > 0:
                    options.add(actSocial.pop())
                else:
                    options.add(actAntiSo.pop())
            elif base == 'agress':
                if val > 0:
                    options.add(actAgress.pop())
                else:
                    options.add(actPass.pop())

        # and that one does not
        base, val = random.choice(personality.items())
        if base == 'nice':
            if val < 0:
                options.add(actNice.pop())
            else:
                options.add(actMean.pop())
        elif base == 'social':
            if val < 0:
                options.add(actSocial.pop())
            else:
                options.add(actAntiSo.pop())
        elif base == 'agress':
            if val < 0:
                options.add(actAgress.pop())
            else:
                options.add(actPass.pop())

        return options

    def actResolve():
        global curAct
        options = genOptions()
        optionList = [(option, option) for option in options]
        choice = menu(optionList)
        if curAct == 'tree_start':
            curAct = 'act1Scene'
        elif curAct == 'act1Scene' and 'Big' in choice:
            curAct = 'act2Scene'
        elif curAct == 'act2Scene' and 'Big' in choice:
            curAct = 'conclusion'
        renpy.jump(curAct)

label tree_start:
    "Sometime later..."
    $actResolve()

label act1Scene:
    "Some Act 1 text.."
    $actResolve()

label act2Scene:
    "Some Act 2 text.."
    $actResolve()

label conclusion:
    "Conclusion Text"
    "The end"
