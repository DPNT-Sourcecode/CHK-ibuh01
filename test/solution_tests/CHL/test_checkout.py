from lib.solutions.CHL import checkout_solution

def test_invalid_input():
    assert checkout_solution.checkout("x") == -1
