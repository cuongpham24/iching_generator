from ._constant import *
from ._ngrams import *
from .hexagrams import Hexagrams
from .calendar import Sexagenary, Converter, Solar, Lunar
import random
from collections import Counter

class TimeIChing():
    """
    Creating hexgram using date and time
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
    
class SeriesIching():
    """
    Creating hexgram using numbers
    """
    @staticmethod
    def seriesHex(series_num: int):
        """
        Use a series of number to create hexagram
        """
        series = str(series_num)
        if len(series) % 2 == 1:
            series = "0" + series
        
        # Define hexagram structure
        half_len = int(len(series) / 2)
        top = TimeIChing.getRemainder(sum([int(i) for i in series[ : half_len]]), 8)
        bottom = TimeIChing.getRemainder(sum([int(i) for i in series[half_len : ]]), 8)
        active = TimeIChing.getRemainder(sum([int(i) for i in series]), 6)

        return Hexagrams(top, bottom, active)

class RandomIching():
    """
    Creating hexgram using a random number
    """
    @staticmethod
    def tossingCoins():
        # Generate a list of random zeros and ones
        count_random = Counter([random.randint(0, 1) for _ in range(3)])
        # Find line and active values
        if count_random.get(0, 0) == 0:
            return (1, True)
        elif count_random.get(0, 0) == 1:
            return (0, False)
        elif count_random.get(0, 0) == 2:
            return (1, False)
        elif count_random.get(0, 0) == 3:
            return (0, True)
    
    @staticmethod
    def randomHex(seed=None):
        random.seed(seed)
        # Generate lines
        lines = []
        actives = []
        for i in range(1, 7):
            line, active = RandomIching.tossingCoins()
            lines.append(str(line))
            if active:
                actives.append(i)

        # Translate lines into top and bottom values
        top = list(trigrams.keys())[list(trigrams.values()).index("".join(lines[ : 3]))]
        bottom = list(trigrams.keys())[list(trigrams.values()).index("".join(lines[3 : ]))]
        return Hexagrams(top, bottom, actives)