# test/test_main.py

from appl.main import add, subtract

def test_add():
    """Test de la fonction add."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    """Test de la fonction subtract."""
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0