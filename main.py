from typing import List, Dict, Callable
from figures import isYAMS, isSuite, isCarre, isFull, isBrelan


ORDERED_POSSIBLE_FIGURES: Dict[Callable[[List[int]], bool], int] = {
    isYAMS: 50,
    isSuite: 40,
    isCarre: 35,
    isFull: 30,
    isBrelan: 28,
}


def checkNumberOfDices(dices: List[int]) -> None:
    if len(dices) != 5:
        raise ValueError("Number of dices must be 5")


def calculateOneRoll(dices: List[int]) -> int:
    checkNumberOfDices(dices)

    for function, value in ORDERED_POSSIBLE_FIGURES.items():
        if function(dices):
            return value

    return sum(dices)


def main(rolls: List[List[int]]) -> int:

    resultat: int = 0

    for roll in rolls:
        resultat += calculateOneRoll(roll)

    return resultat
