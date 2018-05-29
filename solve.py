#!/usr/bin/python

from collections import defaultdict
from network import *
from sort import *
import re

def build():
    startData = get_data()
    status = startData.get("status")

    buildDict = open("buildDict.txt", "a")

    arr = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 
           'c', 'm', 'f', 'w', 'y', 'p', 'v', 'b', 'g', 'k', 'q', 'j', 'x', 'z']
    arrCnt = 0
    i = 0
    while i < 500:
        curData = post_data(arr[arrCnt])
        arrCnt += 1
        if (arrCnt > 25):
            arrCnt = 0
        if (curData.get("status") != "ALIVE"):
            wordsToAdd = curData.get("lyrics")
            for word in wordsToAdd.split():
                word = re.sub(r'\W+', '\n', word)
                buildDict.write(word + '\n')
            curData = get_data()
            i += 1

    reset_data("smadala98@gmail.com")
        

def solve():
    startData = get_data()
    blanks = startData.get("state")
    status = startData.get("status")
    guesses = startData.get("remaining_guesses")
    
    wordDict = sort("./buildDictClean.txt")

    arr = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 
           'c', 'm', 'f', 'w', 'y', 'p', 'v', 'b', 'g', 'k', 'q', 'j', 'x', 'z']

    wrongGuesses = []
    rightGuesses = []
    i = 0
    curData = startData
    while curData.get("status") == "ALIVE":
        
        wordLen = 0
        wordLenArr = []

        blanks = re.sub('[^A-Za-z_ ]+',' ', blanks)
        blanks = re.sub(' +', ' ', blanks)
        blanksArr = blanks.split(" ")
        
        curGuess = ""
        lowestCnt = 50
        for word in blanksArr:
            blankCnt = 0
            for letter in word:
                if letter == '_':
                    blankCnt += 1
            if blankCnt < lowestCnt and blankCnt != 0:
                lowestCnt = blankCnt
                curGuess = word
        
        notGuess = ""
        for letter in wrongGuesses:
            notGuess += letter

        if len(notGuess) != 0:
            notGuess = "[^" + notGuess + "]"
            regexSearch = re.sub('_', notGuess, curGuess)
        else:
            regexSearch = re.sub('_', '[a-z]', curGuess)
        
#        print(regexSearch)

        possibleWords = []
        r = re.compile(regexSearch)

        letGuess = ''
        possibleWords = filter(r.match, wordDict[len(curGuess)])
        freqLetterDict = {}
 #       print(possibleWords)
        if (possibleWords):
            for word in possibleWords:
                for letter in word:
                    if letter not in rightGuesses:
                        if letter not in freqLetterDict:
                            freqLetterDict[letter] = 1
                        else:
                            freqLetterDict[letter] += 1
                    else:
                        freqLetterDict[letter] = 0
        
            keys = freqLetterDict.keys()
            values = freqLetterDict.values()
            indexHighVal = values.index(max(values))
            letterHigh = keys[indexHighVal]

            letGuess = letterHigh
            if letGuess in rightGuesses:
                for letter in arr:
                    if letter not in rightGuesses and letter not in wrongGuesses:
                        letGuess = letter
                        break;
        else:
            for letter in arr:
                if letter not in rightGuesses and letter not in wrongGuesses:
                    letGuess = letter
                    break;
        
        curData = post_data(letGuess)
        print(letGuess)
        print(curData)

        newGuesses = curData.get("remaining_guesses")
        if(newGuesses < guesses):
            guesses = newGuesses
            wrongGuesses.append(letGuess)
        else:
            rightGuesses.append(letGuess)

        blanks = curData.get("state")

    buildDict = open("buildDict.txt", "a")
    wordsToAdd = curData.get("lyrics")
    for word in wordsToAdd.split():
        word = re.sub(r'\W+', '\n', word)
        buildDict.write(word + '\n')
        
if __name__=="__main__":
    for i in xrange(0,100):
        solve()
