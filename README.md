# Hangman-AI

This is a Hangman solver that has a 24% win rate over 100 games.

To run the hangman solver for 100 games, simply execute "python solve.py" at the command line, ensuring that all the files in this
repository are in the same directory.

solve.py also has a build function which runs several games, purposefully losing to obtain lyrics to build up the dictionary, which is
held in buildDict.txt. buildDict.txt however contains extra newlines, so buildDictClean.txt holds the dictionary with no duplicate
newlines. This is obtained by running "sed '/^$/d' < buildDict.txt > buildDictClean.txt."

The solver works by looking at a dictionary of previously appeared words from hangman games, and looking at the frequency of each letter
for each length of the word in the current game. It then guesses that letter, if it's wrong, it removes any word containing that letter
from the possible words in the dictionary fitting that length.
