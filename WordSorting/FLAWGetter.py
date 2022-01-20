import pathlib

with open(pathlib.Path(__file__).parent / "AllAlphaWords.txt") as AlphaList:
    
    SeperatedAlphaList = AlphaList.read().splitlines()
    
    FiveLetterWords = []
    
    for i in SeperatedAlphaList:
        if len(i) == 5:
            FiveLetterWords.append(i)

with open(pathlib.Path(__file__).parent / "FiveLetterAlphaWords.txt", "w") as FiveAlphaList:
    for a in FiveLetterWords:
        writing = "{} \n".format(a)
        FiveAlphaList.write(writing)