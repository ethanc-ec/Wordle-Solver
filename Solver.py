import pathlib


with open(pathlib.Path(__file__).parent / "FiveLetterAlphaWords.txt") as RawFLAWList:
    FLAWList = RawFLAWList.read().splitlines()

with open(pathlib.Path(__file__).parent / "config.cfg") as RawConfig:
    Config = RawConfig.read().splitlines()

    Letters = []
    for idx, val in enumerate(Config):
        splitI = val.split("=")
        Letters.append(splitI[1])
    print(Letters)