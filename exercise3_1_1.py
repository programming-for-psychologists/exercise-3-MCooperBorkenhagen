#part 3.1.1

def repetition(letters, numberBeforeSwitch, numRepetitions):
    for curRepeatSequence in range(numRepetitions):
        for curElt in letters:
            for curRepeatElement in range(numberBeforeSwitch):
                print curElt


repetition(['A', 'B'], 3, 1)
