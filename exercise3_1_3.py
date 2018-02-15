#exercise3_1_3
import random

maskList = ['masked','masked','nonmasked']
sideList = ['right','left']
separator = ","

def repetition(numGroups, masks, sides):
    trialSet = []
    for trial in range(numGroups):
        for mask in masks:
            for sideList in sides:
                trialSet.append([trial+1,mask,sideList])
    return trialSet

trialSet = repetition(5,maskList,sideList)
random.shuffle(trialSet)
for trial in trialSet:
    print separator.join((str(trial[0]), trial[1], trial[2]))
