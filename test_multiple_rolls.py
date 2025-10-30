from main import main
from typing import List


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


def test_two_brelans() -> None:
    rolls: List[List[int]] = [[2, 2, 2, 4, 5], [3, 3, 3, 1, 6]]
    assert main(rolls) == 28 + 28


def test_full_and_suite() -> None:
    rolls: List[List[int]] = [[2, 2, 2, 3, 3], [2, 3, 4, 5, 6]]
    assert main(rolls) == 30 + 40


def test_carre_and_chance() -> None:
    rolls: List[List[int]] = [[5, 5, 5, 5, 2], [1, 2, 3, 4, 6]]
    assert main(rolls) == 35 + 16


def test_multiple_YAMS() -> None:
    rolls: List[List[int]] = [[6, 6, 6, 6, 6], [3, 3, 3, 3, 3]]
    assert main(rolls) == 50 + 50


def test_mixed_rolls() -> None:
    rolls: List[List[int]] = [
        [1, 2, 3, 4, 5],  # Suite
        [2, 2, 2, 3, 4],  # Brelan
        [4, 4, 4, 4, 5],  # Carre
        [1, 1, 2, 2, 2],  # Full
        [6, 6, 6, 6, 6],  # YAMS
        [2, 2, 4, 5, 6],  # Chance
    ]
    assert main(rolls) == 40 + 28 + 35 + 30 + 50 + 19
