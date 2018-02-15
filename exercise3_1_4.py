# exercise3_1_4

import random

maskList = ['masked','masked','nonmasked']
sideList = ['right','left']
separator = ','

def repetition(masks, sides):
	trialSet = []
	for mask in masks:
		for sideList in sides:
			trialSet.append([mask,sideList])
	return trialSet

numBlocks= range(5)
for block in numBlocks:
	trialSet = repetition(maskList,sideList)
	random.shuffle(trialSet)
	for trial in trialSet:
		print separator.join((str(block+1),str(trial[0]), trial[1]))
