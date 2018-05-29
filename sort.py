from collections import defaultdict

def sort(filename):
    sortedDict = defaultdict(list)
    f = open(filename, "r")
    freqDict = defaultdict(list)
    for word in f:
        word = word.strip()
        sortedDict[len(word)].append(word)
    return sortedDict
        

