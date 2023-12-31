from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("faizan") == "fzn"
    assert shorten("test") == "tst"

    # print("worked lower")


def test_uppercase():
    assert shorten("FAIzAN") == "FzN"
    assert shorten("tEST") == "tST"
#     print("worked upper")

def test_numb():
    assert shorten("FAIzAN1") == "FzN1"
    assert shorten("3tEST") == "3tST"
#     print("worked upper")

def test_punc():
    assert shorten(".FAIzAN1") == ".FzN1"
    assert shorten("1.twitter") == "1.twttr"
