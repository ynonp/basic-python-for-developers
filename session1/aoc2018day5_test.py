from aoc2018day5 import reduce_polymer


def test_aA():
    assert reduce_polymer("aA") == ""


def test_bug():
    assert reduce_polymer("aAff") == "ff"


def test_abBA():
    assert reduce_polymer("abBA") == ""


def test_abAB():
    assert reduce_polymer("abAB") == "abAB"


def test_dabAcCaCBAcCcaDA():
    assert reduce_polymer("dabAcCaCBAcCcaDA") == "dabCBAcaDA"




