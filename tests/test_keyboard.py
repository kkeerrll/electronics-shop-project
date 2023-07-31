import pytest
from src.keyboard import Keyboard


def test_repr():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, 'EN')"


def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"

    kb.change_lang()
    assert kb.language == "EN"

    kb.change_lang().change_lang()
    assert kb.language == "EN"

    with pytest.raises(AttributeError):
        kb.language = "CH"
