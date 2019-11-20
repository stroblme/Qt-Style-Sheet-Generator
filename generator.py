import os, sys
from indexed import IndexedOrderedDict

class Generator():

    def extractParser(self, paletteDict):
        self.primary_shade_0 = paletteDict["primary"]["0"]["hex"]
        self.primary_shade_1 = paletteDict["primary"]["1"]["hex"]
        self.primary_shade_2 = paletteDict["primary"]["2"]["hex"]
        self.primary_shade_3 = paletteDict["primary"]["3"]["hex"]
        self.primary_shade_4 = paletteDict["primary"]["4"]["hex"]
        self.secondary_1_shade_0 = paletteDict["secondary_1"]["0"]["hex"]
        self.secondary_1_shade_1 = paletteDict["secondary_1"]["1"]["hex"]
        self.secondary_1_shade_2 = paletteDict["secondary_1"]["2"]["hex"]
        self.secondary_1_shade_3 = paletteDict["secondary_1"]["3"]["hex"]
        self.secondary_1_shade_4 = paletteDict["secondary_1"]["4"]["hex"]
        self.secondary_2_shade_0 = paletteDict["secondary_2"]["0"]["hex"]
        self.secondary_2_shade_1 = paletteDict["secondary_2"]["1"]["hex"]
        self.secondary_2_shade_2 = paletteDict["secondary_2"]["2"]["hex"]
        self.secondary_2_shade_3 = paletteDict["secondary_2"]["3"]["hex"]
        self.secondary_2_shade_4 = paletteDict["secondary_2"]["4"]["hex"]

    def loadTemplate(self, fileName):
        f = open(fileName, 'r')
        content = f.read()

        self.content = self.modifyTemplate(content)

    def modifyTemplate(self, content):
        content = content.replace("primary_shade_0", self.primary_shade_0)
        content = content.replace("primary_shade_1", self.primary_shade_1)
        content = content.replace("primary_shade_2", self.primary_shade_2)
        content = content.replace("primary_shade_3", self.primary_shade_3)
        content = content.replace("primary_shade_4", self.primary_shade_4)
        content = content.replace("secondary_1_shade_0", self.secondary_1_shade_0)
        content = content.replace("secondary_1_shade_1", self.secondary_1_shade_1)
        content = content.replace("secondary_1_shade_2", self.secondary_1_shade_2)
        content = content.replace("secondary_1_shade_3", self.secondary_1_shade_3)
        content = content.replace("secondary_1_shade_4", self.secondary_1_shade_4)
        content = content.replace("secondary_2_shade_0", self.secondary_2_shade_0)
        content = content.replace("secondary_2_shade_1", self.secondary_2_shade_1)
        content = content.replace("secondary_2_shade_2", self.secondary_2_shade_2)
        content = content.replace("secondary_2_shade_3", self.secondary_2_shade_3)
        content = content.replace("secondary_2_shade_4", self.secondary_2_shade_4)

        return content

    def saveOutput(self, fileName, content):
        f = open(fileName, 'w')
        f.write(content)
        
primary_shade_0 = ""
primary_shade_1 = ""
primary_shade_2 = ""
primary_shade_3 = ""
primary_shade_4 = ""

secondary_1_shade_0 = ""
secondary_1_shade_1 = ""
secondary_1_shade_2 = ""
secondary_1_shade_3 = ""
secondary_1_shade_4 = ""

secondary_2_shade_0 = ""
secondary_2_shade_1 = ""
secondary_2_shade_2 = ""
secondary_2_shade_3 = ""
secondary_2_shade_4 = ""
