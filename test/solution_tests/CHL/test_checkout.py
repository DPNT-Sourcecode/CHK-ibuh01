from lib.solutions.CHK.checkout_solution import checkout

def test_invalid_input():
    assert checkout("x") == -1
    assert checkout(" ") == -1
    assert checkout("123") == -1
    assert checkout(123) == -1

