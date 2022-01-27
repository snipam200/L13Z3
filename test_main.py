import main

def test_przeciwna():
    assert main.przeciwna(2)=-2
    assert main.przeciwna(-5)=5
    assert main.przeciwna(2137)=-2137

def test_razy2():
    assert main.razy2(4)=8
    assert main.razy2(0)=0
    assert main.razy2(-21)=-42