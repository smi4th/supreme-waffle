from typing import List, Dict, Callable, Tuple, TypeAlias
from figures import isYAMS, isSuite, isCarre, isFull, isBrelan

Roll: TypeAlias = List[int]
FigureCheck: TypeAlias = Callable[[Roll], bool]
FigureScore: TypeAlias = int
FigureMap: TypeAlias = Dict[FigureCheck, FigureScore]
CalculationResult: TypeAlias = Tuple[FigureScore, FigureCheck | None]

ORDERED_POSSIBLE_FIGURES: FigureMap = {
    isYAMS: 50,
    isSuite: 40,
    isCarre: 35,
    isFull: 30,
    isBrelan: 28,
}


def checkNumberOfDices(dices: Roll) -> None:
    if len(dices) != 5:
        raise ValueError("Number of dices must be 5")


def calculateOneRoll(dices: Roll, available_figures: FigureMap = ORDERED_POSSIBLE_FIGURES) -> CalculationResult:
    checkNumberOfDices(dices)

    for function, value in available_figures.items():
        if function(dices):
            return value, function

    return sum(dices), None


def main(rolls: List[Roll]) -> int:

    resultat: int = 0
    
    available_figures: FigureMap = ORDERED_POSSIBLE_FIGURES.copy()

    for roll in rolls:
        score: FigureScore
        function: FigureCheck | None
        score, function = calculateOneRoll(roll, available_figures)
        
        if function is not None:
            del available_figures[function]
            
        resultat += score

    return resultat
