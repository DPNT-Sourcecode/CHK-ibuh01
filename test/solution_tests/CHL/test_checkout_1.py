from lib.solutions.CHK.checkout_solution_1 import checkout

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

def test_special_offer_a():
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180
    assert checkout("AAAAAA") == 260

def test_special_offer_b():
    assert checkout("BB") == 45
    assert checkout("BBB") == 75
    assert checkout("BBBB") == 90

def test_combination_of_items():
    assert checkout("ABCD") == 115
    assert checkout("ABCDAA") == 195 # 130 + 30 + 20 + 15

    