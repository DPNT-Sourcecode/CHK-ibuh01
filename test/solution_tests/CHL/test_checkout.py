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
    assert checkout("E") == 40


def test_special_offer_a():
    assert checkout("AAAA") == 180  # 130 + 50
    assert checkout("AAAAA") == 200  # 200
    assert checkout("AAAAAA") == 250
    assert checkout("AAAAAAA") == 300  # 200 + 50*2
    assert checkout("AAAAAAAA") == 330  # 200 + 130


def test_special_offer_b():
    assert checkout("BB") == 45
    assert checkout("BBB") == 75
    assert checkout("BBBB") == 90


def test_special_offer_e():
    assert checkout("EE") == 80
    assert checkout("EEB") == 80  # B is free


def test_special_offer_f():
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("FFFFFF") == 40


def test_combination_offers():
    assert checkout("AAAAAEEB") == 280  # 200 + 80
    assert checkout("FFFE") == 60  # F is free


def test_edge_cases():
    assert checkout("AAAAAAAA") == 330  # 5A for 200 + 3A for 130
    assert checkout("EEEEBBB") == 190  # 4E = 160, two B free, pay for one B



