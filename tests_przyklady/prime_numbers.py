#
# 1 -> []
# 2 -> [2]
# 3 -> [3]
# 4 -> [2,2]
# 5 -> [5]
# 6 -> [2,3]
# 8 -> [2, 2, 2]
def prime_numbers(n):
    lst = []
    divider = 2
    while n > 1:
        while n % divider == 0:
            lst.append(divider)
            n = n // divider
        divider += 1
    return lst


def test_prime_numbers():
    assert prime_numbers(1) == []
    assert prime_numbers(2) == [2]
    assert prime_numbers(3) == [3]
    assert prime_numbers(4) == [2, 2]
    assert prime_numbers(5) == [5]
    assert prime_numbers(6) == [2, 3]
    assert prime_numbers(8) == [2, 2, 2]
    assert prime_numbers(16) == [2, 2, 2, 2]
    assert prime_numbers(9) == [3, 3]
    assert prime_numbers(2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 11) == [2, 2, 2, 3, 3, 5, 5, 7, 11]
