from main import main
from typing import List


def test_figure_used_once_full_brelan_sum() -> None:
    rolls: List[List[int]] = [
        [1, 1, 1, 2, 2],
        [1, 1, 1, 2, 2],
        [1, 1, 1, 2, 2],
    ]
    assert main(rolls) == 30 + 28 + 7


def test_figure_used_once_yahtzee_carre_brelan() -> None:
    rolls: List[List[int]] = [
        [4, 4, 4, 4, 4],
        [4, 4, 4, 4, 1],
        [4, 4, 4, 1, 2],
    ]
    assert main(rolls) == 50 + 35 + 28


def test_figure_used_once_straight_sum() -> None:
    rolls: List[List[int]] = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
    ]
    assert main(rolls) == 40 + 20


def test_all_figures_used_once() -> None:
    rolls: List[List[int]] = [
        [6, 6, 6, 6, 6],
        [1, 2, 3, 4, 5],
        [5, 5, 5, 5, 1],
        [3, 3, 3, 2, 2],
        [1, 1, 1, 3, 4],
        [1, 1, 1, 1, 1],
    ]
    assert main(rolls) == 50 + 40 + 35 + 30 + 28 + 5
