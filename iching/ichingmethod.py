from ._constant import *
from ._ngrams import *
from .hexagrams import Hexagrams
from .calendar import Sexagenary, Converter, Solar, Lunar

class TimeIChing():
    """
    Class for creating hexgram using different technique
    """
    @staticmethod
    def getTimeIndex(time: float):
        for timeBranch in timeBranches:
            start, end = timeBranches[timeBranch]
            if time >= start and time < end:
                return earthlyBranchesNo[timeBranch]
            elif start == 23 and (time >= start or time < end):
                return earthlyBranchesNo[timeBranch]

    @staticmethod
    def getRemainder(value, divisor):
        remainder = value % divisor
        if remainder == 0:
            return divisor
        else:
            return remainder
    
    @staticmethod
    def datetimeHex(year, month, day, hour, minute):
        solar = Solar(year, month, day)
        lunar = Converter.Solar2Lunar(solar)
        sexagenary = Sexagenary(year, month, day)
        # get day time index
        yearIndex = sexagenary.year[1] + 1
        monthIndex = lunar.month
        dayIndex = lunar.day
        timeIndex = TimeIChing.getTimeIndex(hour + minute / 60)

        # Define hexagram structure
        top = TimeIChing.getRemainder(yearIndex + monthIndex + dayIndex, 8)
        bottom = TimeIChing.getRemainder(yearIndex + monthIndex + dayIndex + timeIndex, 8)
        active = TimeIChing.getRemainder(yearIndex + monthIndex + dayIndex + timeIndex, 6)

        return Hexagrams(top, bottom, active)