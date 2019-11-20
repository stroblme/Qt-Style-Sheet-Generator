import sys
import os

from paletteParser import PaletteParser
from generator import Generator

PALETTEFILENAME = "./palette.txt"
TEMPLATEFILENAME = "./breeze/dark.template"
OUTPUTFILENAME = "./output/dark.qss"

def main():
    paletteParserInst = PaletteParser()

    paletteParserInst.parseDocument(PALETTEFILENAME)

    generator = Generator()

    generator.extractParser(paletteParserInst.paletteDict)

    generator.loadTemplate(TEMPLATEFILENAME)

    generator.modifyTemplate(TEMPLATEFILENAME)

    generator.saveOutput(OUTPUTFILENAME, generator.content)

if __name__ == "__main__":
    main()