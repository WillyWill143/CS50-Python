from bank import value

def test_for0():
    assert value("hello, world") == 0
    assert value("HELLO, WORLD") == 0
def test_for20():
    assert value("hi, world") == 20
    assert value("HI, WORLD") == 20
def test_fro100():
    assert value("wassup, world") == 100
    assert value("WASSUP, WORLD") == 100
