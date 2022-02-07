from pathlib import Path
from collections import defaultdict
   
    
def checkgreens(green, word):
    for idx, val in enumerate(green):
        if val and word[idx] != val:
            return False
    return True


def checkgreyoranged(greyoranges, word):
    for idx, val in enumerate(greyoranges):
        if word[idx] in val:
            return False
    return True


def parsewords(green, orange, grey, greyedoranges, words):
    """Takes in 4 parameters:
    green a list containing all green characters and None as filler \norange a set of characters marked orange\ngrey a set of characters marked grey\nand words a set of words to parse through
    returns a list of newly parsed words meeting the parameters
    """
    newlist = set()
    for word in words:
        word = word[:5]
        our_map = defaultdict(lambda:0)
        for char in word:
            our_map[char] += 1
        for char in green:
            our_map[char] -= 1

        if checkgreens(green, word) and orange.issubset(charset := set(list(word))) and grey.isdisjoint(set([x for x in our_map.keys() if our_map[x] > 0])) and checkgreyoranged(greyedoranges, word):
            newlist.add(word)
    return newlist


def parseguesses(orange, grey, greyedoranges, words):
    newlist = set()
    yesorange = set()
    for word in words:
        word = word[:5]
        if orange.issubset(charset := set(list(word))) and grey.isdisjoint(charset) and checkgreyoranged(greyedoranges, word):
            newlist.add(word)
        elif grey.isdisjoint(set(list(word))):
            yesorange.add(word)
    return newlist

    
def bestguess(possible_words, guess_list):
    """
    Takes in a list of words, finds the best word based on sum of occurrences of each letter
    Needs work, weights for various parts
    """
    if len(guess_list) == 1:
        return set([guess_list])
    charhashmap = defaultdict(lambda:0)
    for word in possible_words:
        for char in word:
            charhashmap[char] += 1
    curmax = 0
    dupemax = 0
    maxval = set()
    maxwithdupes = set()
    for word in guess_list:
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
    """
    The current solve found part only gives the solution when you literally type it in.
    We could swap to using seperate lists for the answers and guesses.
    _greens gets messed up when the guess doesn't use the previous greens
    """
    _greens = [None, None, None, None, None]
    _oranges = set()
    _greyoranges = [set(),set(),set(),set(),set()]
    _grey = set()
    possiblities = words
    guesslist = words
    loop_number = 0
    while True:
        print("Loop number: {}".format(loop_number))
        print("Green letters:", _greens)
        if len(_oranges) == 0:
            print("There are no orange letters")
        else:
            print("Orange letters:", _oranges)
        if len(_grey) == 0:
            print("There are no grey letters")
        else:
            print("Grey letters:", _grey)
        possiblities = parsewords(_greens,_oranges,_grey, _greyoranges, possiblities)
        if loop_number > 0:
            print("Possible words: {}".format(possiblities))
        if len(possiblities) == 1:
            print("solve found: " + list(possiblities)[0])
            break
        guesslist = parseguesses(_oranges,_grey, _greyoranges, words)
        w = bestguess(possiblities, guesslist)
        print("Best words using current params:")
        print(w)
        guess = input("Type your guess:\n")
        if guess == "stop":
            break
        greeninputs = green_input()
        for x in range(5):
            if greeninputs[x] != " ":
                _greens[x] = greeninputs[x]
        orange = orange_input()
        for x in range(5):
            if orange[x] != " ":
                _greyoranges[x].add(orange[x])
        orange = orange.replace(" ", "")
        # Can't take x directly from green, overwrites _greens
        # Check for letters that are already there 
        
        _oranges = set(list(orange)).union(_oranges) - set(list(greeninputs))
        our_map = defaultdict(lambda:0)
        for char in guess:
            our_map[char] += 1
        for char in greeninputs + orange:
            our_map[char] -= 1
        greys = set([x for x in our_map.keys() if our_map[x] > 0])
        _grey.update(greys)
        loop_number += 1
        

def green_input():
    green_test = input("Insert all green characters, spaces for non greens:\n")
    green_test_alpha = green_test.replace(" ", "")

    if (green_test_alpha.isalpha() and len(green_test) == 5):
        return green_test
    elif not green_test:
        green_test = "     "
        return green_test
    else:
        print("Wrong input, try again\n")
        return green_input()


def orange_input(): 
    orange_test = input("Insert all oranges, spaces for non oranges:\n")
    orangealphatest = orange_test.replace(" ", "")
    
    if (orangealphatest.isalpha() and len(orange_test) == 5):
        return orange_test
    elif not orange_test:
        orange_test = "     "
        return orange_test
    else:
        print("Wrong input, try again\n")
        return orange_input()
    
    
def main():
    with open(Path(__file__).parent / "FLAW.txt") as RawFLAWList:
        words = RawFLAWList.read().splitlines()
        test_run(words)


if __name__ == "__main__":
    main()
                
        
