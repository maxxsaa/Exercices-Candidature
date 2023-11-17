import Exo

def test_imc():
    assert Exo.imc(1,1) == 1

def test_trois():
    assert Exo.trois('salut') == 'sal'


def test_trois_derniers():
    assert Exo.trois_derniers('salut') == 'lut'

def test_inv():
    assert Exo.inv('a','b') == ('b','a')

def test_cui():
    assert Exo.cui(150) == 'Pour x grammes de sucre, il faut 10.0 cuillères à soupe.'

def test_moy():
    assert Exo.moy([5,10,15]) == 10


def test_amende() :
    assert Exo.amende(5,10) == "pas d'amende"
    assert Exo.amende(15,10) == "53 d'amende"
    assert Exo.amende(40,10) == 173


def test_age():
    assert Exo.age(2000) == 23


def test_age2():
    assert Exo.age2('2003-3-3') == (20, 8, 24)

