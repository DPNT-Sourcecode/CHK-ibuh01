from lib.solutions.CHK.checkout_solution import checkout

def test_invalid_input():
    assert checkout("x") == -1
    assert checkout(" ") == -1
    assert checkout("123") == -1
    assert checkout(123) == -1

def test_emplty_checkout():
    assert checkout("") == 0

def test_single_item():
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15

