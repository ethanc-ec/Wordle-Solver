import pathlib
from collections import defaultdict

with open(pathlib.Path(__file__).parent / "FiveLetterAlphaWords.txt") as RawFLAWList:
    FLAWList = RawFLAWList.read().splitlines()

with open(pathlib.Path(__file__).parent / "config.cfg") as RawConfig:
    Config = RawConfig.read().splitlines()

    Letters = []
    for idx, val in enumerate(Config):
        splitI = val.split("=")
        Letters.append(splitI[1])
    print(Letters)

greens = ['a',None, None,None,'e']
oranges = set()
grey = set()
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
        if checkgreens(green, word) and orange.issubset(charset := set(word.split())) and grey.isdisjoint(charset):
            newlist.add(word)
    return newlist
def bestword(words):
    if len(words) == 1:
        return (list(words))[0]
    charhashmap = defaultdict(lambda:0)
    for word in words:
        for char in word:
            charhashmap[char] += 1
    
    
with open(pathlib.Path(__file__).parent / "FiveLetterAlphaWords.txt") as RawFLAWList:
    words = RawFLAWList.read().splitlines()
    print(parsewords(greens,oranges,grey, words))
            
                
        
