from datetime import datetime

import pytest


#
#
# def add(a, b):
#     return a + b
#
#
# def sqrt(x):
#     assert x >= 0
#     precision = 0.0001
#     step = 1
#     start = 0
#     while abs(start * start - x) > precision:
#         start += step
#         if start * start > x:
#             start -= step
#             step /= 10
#     return start
#
# def test_check_if_throw_exception_when_x_below_0():
#     try:
#         sqrt(-1)
#         assert False
#     except Exception:
#         assert True

def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 0 else "female"
    """
    dla lat 1800–1899 – 80
    dla lat 2000–2099 – 20
    dla lat 2100–2199 – 40
    dla lat 2200–2299 – 60.
    058115 -> 1805
    050115 -> 1905
    052115 -> 2005
    """

    month = int(pesel[2:4])  # 30
    years = {
        0: '19',
        1: '20',
        2: '21',
        3: '22',
        4: '18'
    }
    year = int(years[month // 20] + pesel[0: 2])
    month = month % 20
    birth_date = datetime(year, month, int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


def test_if_pesel_field_ok():
    pesel = '11111111111'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


@pytest.mark.parametrize("pesel, result",
 [
     ('03302653459', True),
     ('61080875438', True),
     ('78081172959', False)
 ])
def test_is_valid(pesel, result):
    r = analyze_pesel(pesel)
    assert r['valid'] == result


def test_valid_pesel_03302653459():
    pesel = "03302653459"
    result = analyze_pesel(pesel)
    assert result['valid']


def test_valid_pesel_61080875438():
    pesel = "61080875438"
    result = analyze_pesel(pesel)
    assert result['valid']


def test_valid_pesel_79081172959():
    pesel = "79081172959"
    result = analyze_pesel(pesel)
    assert result['valid']


def test_valid_pesel_54102133577():
    pesel = "54102133577"
    result = analyze_pesel(pesel)
    assert result['valid']


def test_valid_pesel_94071781979():
    pesel = "94071781979"
    result = analyze_pesel(pesel)
    assert result['valid']


def test_invalid_pesel_04302653459():
    pesel = "04302653459"
    result = analyze_pesel(pesel)
    assert not result['valid']


def test_invalid_pesel_62080875438():
    pesel = "62080875438"
    result = analyze_pesel(pesel)
    assert not result['valid']


def test_invalid_pesel_70081172959():
    pesel = "70081172959"
    result = analyze_pesel(pesel)
    assert not result['valid']


def test_invalid_pesel_55102133577():
    pesel = "55102133577"
    result = analyze_pesel(pesel)
    assert not result['valid']


def test_invalid_pesel_95071781979():
    pesel = "95071781979"
    result = analyze_pesel(pesel)
    assert not result['valid']


def test_year_pesel_03302653459():
    pesel = "03302653459"
    result = analyze_pesel(pesel)
    assert result['birth_date'] == datetime(2003, 10, 26)


def test_year_pesel_03502653459():
    pesel = "03502653459"
    result = analyze_pesel(pesel)
    assert result['birth_date'] == datetime(2103, 10, 26)


def test_year_pesel_03702653459():
    pesel = "03702653459"
    result = analyze_pesel(pesel)
    assert result['birth_date'] == datetime(2203, 10, 26)


def test_year_pesel_03902653459():
    pesel = "03902653459"
    result = analyze_pesel(pesel)
    assert result['birth_date'] == datetime(1803, 10, 26)
# 03302653459
# 61080875438
# 99011599333
# 61122925237
# 79081172959
# 54102133577
# 94071781979
# 00291115795
# 50122847454


# def test_birth_day_2000():
#     pesel = '03242276338'
#     result = analyze_pesel(pesel)
#     assert result['birth_date'] == datetime(2003, 4,22)
