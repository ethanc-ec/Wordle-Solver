from pathlib import Path
from collections import defaultdict
 
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
        our_map = defaultdict(lambda:0)
        for char in word:
            our_map[char] += 1
        for char in green:
            our_map[char] -= 1

        if checkgreens(green, word) and orange.issubset(charset := set(list(word))) and grey.isdisjoint(set([x for x in our_map.keys() if our_map[x] > 0])):
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
    _greens = [None, None, None, None, None]
    _oranges = set()
    _grey = set()
    possiblities = words
    while True:
        print("Green letters:", _greens)
        if len(_oranges) == 0:
            print("There are no orange letters")
        else:
            print("Orange letters:", _oranges)  
        print("Grey letters:", _grey)
        possiblities = parsewords(_greens,_oranges,_grey, possiblities)
        print("Possible words:")
        print(possiblities)
        #w = bestword(parseguesses(_greens,_oranges,_grey, words))
        if len(possiblities) == 1:
            print("solve found: " + list(possiblities)[0])
            break
        #print("Best words using current params:")
        #print(w)
        guess = input("Type your guess:\n")
        green = green_input(guess)
        orange = orange_input(green)
        _greens = [None if x == " " else x for x in green]
        _oranges = set(list(orange)).union(_oranges) - set(list(green))
        our_map = defaultdict(lambda:0)
        for char in guess:
            our_map[char] += 1
        for char in green + orange:
            our_map[char] -= 1
        greys = set([x for x in our_map.keys() if our_map[x] > 0])
        _grey.update(greys)
        

def green_input(guess):
    green_test = input("Insert all green characters, spaces for non greens:\n")
    alpha_test_green = green_test.replace(" ", "")

    for i in green_test:
        if green_test != "     ":
            if i in guess or i == " ":
                continue
            else:
                print("Wrong input, try again\n")
                return green_input()

    if (alpha_test_green.isalpha() and len(green_test) == 5) or green_test == "     ":
        return green_test
    else:
        print("Wrong input, try again\n")
        return green_input(guess)


def orange_input(green):
    orange_test = input("Insert all oranges, no spaces:\n")
    if (orange_test.isalpha() and (5 - len(orange_test) - len(green) <= 5)) or not orange_test:
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
                
        
