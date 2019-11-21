import sys
import os
import argparse

from paletteParser import PaletteParser
from generator import Generator

PALETTEFILENAME = "./palette.txt"
TEMPLATEFILENAME = "./dark.template"
OUTPUTFILENAME = "./output/dark.qss"

def argumentHelper():
    """
    Just a helper for processing the arguments
    """

    # Define Help Te
    helpText = 'Register Converter Script'
    # Create ArgumentParser instance
    argparser = argparse.ArgumentParser(description=helpText)

    
    argparser.add_argument('-p', '--palette',
                        help='Your color palette')
    argparser.add_argument('-t', '--template',
                        help='Template file')
    argparser.add_argument('-o', '--output',
                        help='Output file')

    return argparser.parse_args()

def main():
    global PALETTEFILENAME, TEMPLATEFILENAME, OUTPUTFILENAME

    #-----------------------------------------------------
    # ---------------Argument processing------------------
    args = None
    try:
        args = argumentHelper()
    except ValueError as e:
        print("Unable to parse arguments:\n")
        sys.exit(str(e.args))

    if args.palette:
        PALETTEFILENAME = args.palette

    if args.template:
        TEMPLATEFILENAME = args.template
        
    if args.output:
        OUTPUTFILENAME = args.output
        
    paletteParserInst = PaletteParser()

    paletteParserInst.parseDocument(PALETTEFILENAME)

    generator = Generator()

    generator.extractParser(paletteParserInst.paletteDict)

    generator.loadTemplate(TEMPLATEFILENAME)

    generator.modifyTemplate(TEMPLATEFILENAME)

    generator.saveOutput(OUTPUTFILENAME, generator.content)

if __name__ == "__main__":
    main()