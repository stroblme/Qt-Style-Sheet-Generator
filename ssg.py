import sys
import os

from paletteParser import PaletteParser

PALETTEFILENAME = "./palette.txt"

def main():
    paletteParserInst = PaletteParser()

    paletteParserInst.parseDocument(PALETTEFILENAME)

if __name__ == "__main__":
    main()