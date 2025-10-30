from typing import List
from collections import Counter

def checkNumberOfDices(dices: List[int]) -> None:
    if len(dices) != 5:
        raise ValueError('Number of dices must be 5')

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

def main(dices: List[int]) -> int:
    
    checkNumberOfDices(dices)
    
    if isCarre(dices):
        return 35
    
    if isFull(dices):
        return 30
    
    if isBrelan(dices):
        return 28
        
    return sum(dices)