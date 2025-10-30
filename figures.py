from typing import List
from collections import Counter


def isBrelan(dices: List[int]) -> bool:
    counter = Counter(dices)
    return max(counter.values()) == 3


def isCarre(dices: List[int]) -> bool:
    counter = Counter(dices)
    return max(counter.values()) == 4


def isFull(dices: List[int]) -> bool:
    counter = Counter(dices)
    counts = sorted(counter.values())
    return counts == [2, 3]


def isSuite(dices: List[int]) -> bool:
    min_dice: int = min(dices)
    max_dice: int = max(dices)
    return len(set(dices)) == max_dice - min_dice + 1 == len(dices)


def isYAMS(dices: List[int]) -> bool:
    counter = Counter(dices)
    return max(counter.values()) == 5
