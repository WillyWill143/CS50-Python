from plates import is_valid

def test_startwith2():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C0") == False
def test_lenofplate():
    assert is_valid("CS") == True
    assert is_valid("HIVE50") == True
    assert is_valid("LOLOLO40") == False
def test_numNdzero():
    assert is_valid("NNN111") == True
    assert is_valid("RRR11R") == False
    assert is_valid("RRR011") == False
def test_puncs():
    assert is_valid("CSDA2!") == False
    assert is_valid("CS.DF4") == False
