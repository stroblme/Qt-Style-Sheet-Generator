import os, sys
from indexed import IndexedOrderedDict
import re

class PaletteParser():

    paletteDict = IndexedOrderedDict()

    regexp = r"\D+(?P<shadeNumber>\d)\D+(?P<hexValue>\S{6})\D+(?P<rgbValue>\d+\D+\d+\D+\d+)\D+(?P<rgbaValue>\d+\D+\d+\D+\d+\D+\d+)"

    def parseDocument(self, filePath):
        paletteFile = open(filePath, 'r')

        prog = re.compile(self.regexp)
        
        paletteDict = IndexedOrderedDict()
        sectionDict = IndexedOrderedDict()
        shadeDict = IndexedOrderedDict()

        section = ''
        shade = ''

        for line in paletteFile:
            if "*** Primary color:" in line:
                section = 'primary'

                sectionDict = IndexedOrderedDict()

            elif "*** Secondary color (1):" in line:
                section = 'secondary_1'

                sectionDict = IndexedOrderedDict()

            elif "*** Secondary color (2):" in line:
                section = 'secondary_2'

                sectionDict = IndexedOrderedDict()

            elif "*** Complement color:" in line:
                section = 'complementary'

                sectionDict = IndexedOrderedDict()

            # only if a section has been detected, the line is not empty and it's not a comment
            elif line != "" and "#####" not in line:
                res = prog.match(line)

                if res:
                    shadeNum = res.group('shadeNumber')
                    
                    shadeDict['hex'] = res.group('hexValue')
                    shadeDict['rgb'] = res.group('rgbValue')
                    shadeDict['rgba'] = res.group('rgbaValue')

                    sectionDict[shadeNum] = shadeDict

                    shadeDict = IndexedOrderedDict()

            if section != "":
                paletteDict[section] = sectionDict


        # store changes
        self.paletteDict = paletteDict
