import pytest
from numb3rs import validate


def test_validateCorrect():
    assert validate("69.42.40.255") == True
    assert validate("17.0.0.1") == True


def test_validateWwrong():
    assert validate("cat") == False
    assert validate("540.1445.6764.13") == False


def test_validatePeriods():
    assert validate("0") == False
    assert validate("69.420") == False
    assert validate("300.69.69.69") == False
    assert validate("1.420.69.0") == False
