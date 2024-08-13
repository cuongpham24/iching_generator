from ._compact import unicode_compatible
from datetime import datetime
from ._constant import *
from ._ngrams import *

class Hexagram():
    def __init__(self, top: int, bottom: int, ):
        """
        Parameters
        ----------
        top : int
            Number from 1 to 8 represents the top trigram
        bottom : int
            Number from 1 to 8 represents the bottom trigram
        """
        assert (top > 0 and top < 9), "Invalid trigram number. Values must be from 1 to 8"
        assert (bottom > 0 and bottom < 9), "Invalid trigram number. Values must be from 1 to 8"

        self.top = top
        self.bottom = bottom
        self._getConfig()
        self._getData()

    def _getConfig(self):
        self.structure = (self.top, self.bottom)
        self.number = hexagramsStructure[self.structure]
        self._earthBranches = basicHexagramsBranches[self.bottom][:3] + basicHexagramsBranches[self.top][-3:]
        self._mainElement = self._mainHexElement()
        self.name = hexagramsNames[self.number]

    def _mainHexElement(self):
        for hex in hexagramsFamily:
            if self.number in hexagramsFamily[hex]:
                # Return associated original mmain family element 
                return hex
            
    def _getData(self):
        """Store hexamgram in a vector"""
        self.config = []
        # Lines configuaration
        self.config += [int(i) for i in trigrams[self.bottom]]
        self.config += [int(i) for i in trigrams[self.top]]
        # Hexagram element
        self.config += [elements[trigramsElements[self._mainElement]]]
        # Earth branch elements
        self.config += self._earthBranches
    
    def _getRelations(self):
        pass

    def getMainElement(self):
        """Get hexagram main element (simular to family element)"""
        return trigramsElements[self._mainElement]

    def getEarthBranches(self):
        """Get earth branch for each line from bottom to top"""
        return " ".join([earthlyBranches[i].capitalize() for i in self._earthBranches])