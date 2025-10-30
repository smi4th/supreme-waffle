from main import main
from typing import List
import pytest

def test_no_rolls() -> None:
    rolls: List[List[int]] = []
    assert main(rolls) == 0
    
def test_one_brelan() -> None:
    rolls: List[List[int]] = [[1, 1, 1, 2, 3]]
    assert main(rolls) == 28
    
def test_one_carre() -> None:
    rolls: List[List[int]] = [[1, 1, 1, 1, 2]]
    assert main(rolls) == 35
    
def test_one_full() -> None:
    rolls: List[List[int]] = [[1, 1, 1, 2, 2]]
    assert main(rolls) == 30
    
def test_on_suite() -> None:
    rolls: List[List[int]] = [[1, 2, 3, 4, 5]]
    assert main(rolls) == 40
    
def test_one_YAMS() -> None:
    rolls: List[List[int]] = [[1, 1, 1, 1, 1]]
    assert main(rolls) == 50

def test_one_chance() -> None:
    rolls: List[List[int]] = [[2, 2, 3, 4, 5]]
    assert main(rolls) == 16