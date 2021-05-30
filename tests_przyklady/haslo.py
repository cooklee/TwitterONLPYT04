from password_validator import check_password

def test_correct():
    assert check_password('A' + 6 * 'a')

def test_incorrect_length():
    assert not check_password('aA' * 3)

def test_if_has_not_big_letter():
    assert not check_password("a" * 7)

def test_if_has_not_small_letter():
    assert not check_password("A" * 7)



