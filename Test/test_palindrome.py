import pytest
from palindrome import is_palindrome


def test_invalid_input():
    with pytest.raises(ValueError):
        is_palindrome(123)


def test_empty_string():
    assert is_palindrome("") is False

def test_single_character():
    assert is_palindrome("a") is True

def test_two_same_characters():
    assert is_palindrome("bb") is True

def test_non_palindrome():
    assert is_palindrome("abc") is False

def test_long_palindrome():
    assert is_palindrome("racecar") is True

def test_mixed_case_palindrome():
    assert is_palindrome("RaceCar") is True

def test_palindrome_with_spaces():
    assert is_palindrome("nurses run") is True

def test_palindrome_with_punctuation():
    assert is_palindrome("Madam, I'm Adam") is True