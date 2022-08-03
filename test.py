import pytest
from palindrome import palindrome

def test_palin():
    assert palindrome("gopika") is False
    assert palindrome("malayalam") is True





import pytest
from panagram import panagram
def test_panag():
    assert panagram("abcdefghijklmnopqrstuvwxyz") is True
    assert panagram("  abcdefghijklmnopqstuvwxyz  ") is False





import pytest 
from prime import prime
def test_prime():
   
    assert prime(11) is True
    assert prime(8) is False





import pytest
from freq import freq
def test_freq():
    s="happy"
    test_freq={"h": 1, "a": 1, "p": 2, "y": 1}
    assert freq(s)==test_freq
    