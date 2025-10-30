from main import main
from typing import List

def test_too_few_dices() -> None:
    dices: List[int] = [1, 2, 3]
    assert main(dices) == 'error'
    
def test_too_many_dices() -> None:
    dices: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert main(dices) == 'error'

def test_brelan_stacked() -> None:
    dices: List[int] = [1, 1, 1, 2, 3]
    assert main(dices) == 28
    
def test_brelan_spaced() -> None:
    dices: List[int] = [1, 2, 1, 3, 1]
    assert main(dices) == 28
    
def test_carre_stacked() -> None:
    dices: List[int] = [1, 1, 1, 1, 2]
    assert main(dices) == 35
    
def test_carre_spaced() -> None:
    dices: List[int] = [1, 2, 1, 1, 1]
    assert main(dices) == 35
    
def test_full_stucked() -> None:
    dices: List[int] = [1, 1, 1, 2, 2]
    assert main(dices) == 30
    
def test_full_spaced() -> None:
    dices: List[int] = [1, 2, 1, 2, 1]
    assert main(dices) == 30
    
def test_suite() -> None:
    dices: List[int] = [1, 2, 3, 4, 5]
    assert main(dices) == 40
    
def test_yams() -> None:
    dices: List[int] = [1, 1, 1, 1, 1]
    assert main(dices) == 50
    
def test_chance() -> None:
    dices: List[int] = [1, 2, 3, 4, 5]
    assert main(dices) == 15