from ._compact import unicode_compatible
from datetime import datetime
from ._constant import *
from ._ngrams import *

class Hexagram():
    def __init__(self, top: int, bottom: int):
        """
        Parameters
        ----------
        top : int
            Number from 1 to 8 represents the top trigram
        bottom : int
            Number from 1 to 8 represents the bottom trigram
        """
        # input validation
        assert (top > 0 and top < 9), "Invalid trigram number. Values must be from 1 to 8"
        assert (bottom > 0 and bottom < 9), "Invalid trigram number. Values must be from 1 to 8"

        self.top = top
        self.bottom = bottom
        self._getConfig()
        self._getSixRelatives()
        self._getData()

    def _getConfig(self):
        self._structure = (self.top, self.bottom)
        self.number = hexagramsStructure[self._structure]
        self._earthBranches = basicHexagramsBranches[self.bottom][:3] + basicHexagramsBranches[self.top][-3:]
        self._mainElement = self._mainHexElement()
        self.name = hexagramsNames[self.number]

    def _mainHexElement(self):
        for hex in hexagramsFamily:
            if self.number in hexagramsFamily[hex]:
                # Return associated original mmain family element 
                return trigramsElements[hex]
            
    def _getData(self):
        """Store hexamgram in a vector"""
        self.config = []
        # Lines configuaration
        self.config += [int(i) for i in trigrams[self.bottom]]
        self.config += [int(i) for i in trigrams[self.top]]
        # Hexagram element
        self.config += [elements[self._mainElement]]
        # Earth branch elements
        self.config += self._earthBranches
        # Six relatives
        self.config += self._sixRelatives
    
    def _getSixRelatives(self):
        self._sixRelatives = []
        mainElement = elements[self._mainElement]
        for lineEarthBranches in self._earthBranches:
            lineElement = elements[earthlyBranchesElement[lineEarthBranches]]
            if lineElement == mainElement:
                self._sixRelatives.append(hexSixRelatives["huynh đệ"])
            elif elementGeneratingCycle[mainElement] == lineElement:
                self._sixRelatives.append(hexSixRelatives["tử tôn"])
            elif elementGeneratingCycle[lineElement] == mainElement:
                self._sixRelatives.append(hexSixRelatives["phụ mẫu"])
            elif sixRelativesControllingCycle[mainElement] == lineElement:
                self._sixRelatives.append(hexSixRelatives["thê tài"])
            elif sixRelativesControllingCycle[lineElement] == mainElement:
                self._sixRelatives.append(hexSixRelatives["quan quỷ"])

    def getMainElement(self):
        """Get hexagram main element (simular to family element)"""
        return self._mainElement

    def getEarthBranches(self):
        """Get earth branch for each line from bottom to top"""
        return " ".join([earthlyBranches[i].capitalize() for i in self._earthBranches])
    
    def getSixRelatives(self):
        """Get six relatives for each line from bottom to top"""
        valueLookup = {hexSixRelatives[key]: key for key in hexSixRelatives}
        return ", ".join([valueLookup[value].capitalize() for value in self._sixRelatives])
    

class Hexagrams():
    def __init__(self, top: int, bottom: int, actives):
        """
        Parameters
        ----------
        top : int
            Number from 1 to 8 represents the top trigram
        bottom : int
            Number from 1 to 8 represents the bottom trigram
        actives : int or list of list
            Position of active lines from 1 to 6
        """
        # input validation
        assert (top > 0 and top < 9), "Invalid trigram number. Values must be from 1 to 8"
        assert (bottom > 0 and bottom < 9), "Invalid trigram number. Values must be from 1 to 8"

        self._mainHex = Hexagram(top, bottom)
        self._actives = actives
        self._transform()
        self._combineConfig()

    def _transform(self):
        mainHex = trigrams[self._mainHex.bottom] + trigrams[self._mainHex.top]
        mainHex = [int(line) for line in mainHex]

        if isinstance(self._actives, list):
            # Handle the case where actives is a list of numbers
            for num in self._actives:
                assert (num > 0 and num < 7), "Invalid active lines. Values must be from 1 to 6"
            
            for line in self._actives:
                if mainHex[line - 1] == 1:
                    mainHex[line - 1] = 0
                else:
                    mainHex[line - 1] = 1

        elif isinstance(self._actives, int):
            # Handle the case where actives is a single number
            assert (self._actives > 0 and self._actives < 7), "Invalid active line. Value must be from 1 to 6"
            if mainHex[self._actives - 1] == 1:
                mainHex[self._actives - 1] = 0
            else:
                mainHex[self._actives - 1] = 1

        transformedHex = "".join(str(i) for i in mainHex)

        hexDict = {trigrams[key]: key for key in trigrams}
        bottom = hexDict[transformedHex[:3]]
        top = hexDict[transformedHex[3:]]
        self._transformedHex = Hexagram(top, bottom)

    def _combineConfig(self):
        self.config = self._mainHex.config + self._transformedHex.config

    def __str__(self):
        return f"Quẻ chính: {self._mainHex.name}; Quẻ biến: {self._transformedHex.name}"

    def __repr__(self):
        return f"Quẻ chính: {self._mainHex.name}; Quẻ biến: {self._transformedHex.name}"
    
    def getMainHexagram(self):
        return self._mainHex
    
    def getTransformedHexagram(self):
        return self._transformedHex