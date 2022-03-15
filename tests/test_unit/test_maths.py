from something_unique.maths import add_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(10, 100) == 110


def test_add_numbers_2():
    assert add_numbers(1, 3) == 4
    assert add_numbers(10, 2100) == 2110
