#3.1.2

maskList = ['masked', 'masked', 'nonmasked']
sideList = ['right', 'left']
separator=','


trialList = open('trialList.txt', 'w')
def repetition(numGroups, masks, sides):
    data =[]
    for block in range(numGroups):
        for mask in masks:
            for side in sides:
                data=(separator.join((str(block), mask, side)) +'\n')
                trialList.write(data)


repetition(5, maskList, sideList)
