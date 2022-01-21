from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent / "FiveLetterAlphaWords.txt") as RawFLAWList:
    FLAWList = RawFLAWList.read().splitlines()

with open(Path(__file__).parent / "config.cfg") as RawConfig:
    Config = RawConfig.read().splitlines()

    Letters = []
    for idx, val in enumerate(Config):
        splitI = val.split("=")
        Letters.append(splitI[1])
    print(Letters)
def checkgreens(green, word):
    for idx, val in enumerate(green):
        if val and word[idx] != val:
            return False
    return True

def parsewords(green, orange, grey, words):
    """Takes in 4 parameters:
    green a list containing all green characters and None as filler \norange a set of characters marked orange\ngrey a set of characters marked grey\nand words a set of words to parse through
    returns a list of newly parsed words meeting the parameters
    """
    newlist = set()
    for word in words:
        word = word[:5]
        if checkgreens(green, word) and orange.issubset(charset := set(list(word))) and grey.isdisjoint(charset):
            newlist.add(word)
    return newlist
def parseguesses(green, orange, grey, words):
    newlist = set()
    yesorange = set()
    for word in words:
        word = word[:5]
        if orange.isdisjoint(charset := set(list(word))) and grey.isdisjoint(charset):
            newlist.add(word)
        elif grey.isdisjoint(set(list(word))):
            yesorange.add(word)
    if len(newlist) == 0:
        return yesorange
    else:
        return newlist





def bestword(words):
    """
    Takes in a list of words, finds the best word based on sum of occurrences of each letter
    Needs work, weights for various parts
    """
    if len(words) == 1:
        return words
    charhashmap = defaultdict(lambda:0)
    for word in words:
        for char in word:
            charhashmap[char] += 1
    curmax = 0
    dupemax = 0
    maxval = set()
    maxwithdupes = set()
    for word in words:
        word = word[:5]
        summ = 0
        for char in word:
            summ += charhashmap[char]
        if len(set(list(word))) < len(word):
            if summ > dupemax:
                dupemax = summ
                maxwithdupes = set([word])
            elif summ == dupemax:
                maxwithdupes.add(word)
        else:
            if summ > curmax:
                curmax = summ
                maxval = set([word])
            elif summ == curmax:
                maxval.add(word)
    return maxval.union(maxwithdupes)
def test_run(words):
    _greens = [None,None, None,None, None]
    _oranges = set()
    _grey = set()
    while True:
        print(_greens)
        print(_oranges)
        print(_grey)
        possiblities = parsewords(_greens,_oranges,_grey, words)
        print("possible")
        print(possiblities)
        w = bestword(parseguesses(_greens,_oranges,_grey, words))
        if len(possiblities) == 1:
            print("solve found: " + list(possiblities)[0])
            break
        ("Best words for current params:")
        print(w)
        guess = input("Type your guess\n")
        green = input("Insert all green characters, spaces for non greens\n")
        if len(green) != 5:
            print("Inputted wrong, redo please\n")
            continue
        orange = input("Insert all oranges, no spaces\n")
        _greens = [None if x == " " else x for x in green]
        _oranges = set(list(orange)).union(_oranges) - set(list(green))
        greys = set(list(guess)) - set(list(green)) - set(list(orange))
        _grey.update(greys)
    
    
    
with open(Path(__file__).parent / "FiveLetterAlphaWords.txt") as RawFLAWList:
    words = RawFLAWList.read().splitlines()
    test_run(words)
            
                
        
