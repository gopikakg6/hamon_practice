from problem import palindrome, panagram, prime, freq
def test_palin():
    assert palindrome("gopika") is False
    assert palindrome("malayalam") is True




def test_panag():
    assert panagram("abcdefghijklmnopqrstuvwxyz") is True
    assert panagram("abcd") is False




def test_prime():
    assert prime(11) is True
    assert prime(8) is False





def test_freq():
    test_freq={"h": 1, "a": 1, "p": 2, "y": 1}
    assert freq("happy")==test_freq
    