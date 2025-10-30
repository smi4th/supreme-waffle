from main import calculateOneRoll
from typing import List
import pytest

def test_too_few_dices() -> None:
    dices: List[int] = [1, 2, 3]
    with pytest.raises(ValueError, match="Number of dices must be 5"):
        assert calculateOneRoll(dices) == 'error'
    
def test_too_many_dices() -> None:
    dices: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(ValueError, match="Number of dices must be 5"):
        assert calculateOneRoll(dices) == 'error'

def test_brelan_stacked() -> None:
    dices: List[int] = [1, 1, 1, 2, 3]
    assert calculateOneRoll(dices) == 28
    
def test_brelan_spaced() -> None:
    dices: List[int] = [1, 2, 1, 3, 1]
    assert calculateOneRoll(dices) == 28
    
def test_carre_stacked() -> None:
    dices: List[int] = [1, 1, 1, 1, 2]
    assert calculateOneRoll(dices) == 35
    
def test_carre_spaced() -> None:
    dices: List[int] = [1, 2, 1, 1, 1]
    assert calculateOneRoll(dices) == 35
    
def test_full_stucked() -> None:
    dices: List[int] = [1, 1, 1, 2, 2]
    assert calculateOneRoll(dices) == 30
    
def test_full_spaced() -> None:
    dices: List[int] = [1, 2, 1, 2, 1]
    assert calculateOneRoll(dices) == 30
    
def test_suite() -> None:
    dices: List[int] = [1, 2, 3, 4, 5]
    assert calculateOneRoll(dices) == 40
    
def test_yams() -> None:
    dices: List[int] = [1, 1, 1, 1, 1]
    assert calculateOneRoll(dices) == 50
    
def test_chance() -> None:
    dices: List[int] = [2, 2, 3, 4, 5]
    assert calculateOneRoll(dices) == 16