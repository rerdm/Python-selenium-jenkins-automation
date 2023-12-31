# Umbenennung der Datei zu test_addiere_zahlen.py
import pytest

def add_numbers(a, b):
    return a + b

def test_positive_numbers():
    number1 = 5
    number2 = 10
    expected_result = 15

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"

def test_negative_zahlen():
    number1 = -3
    number2 = -7
    expected_result = -10

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"

def test_gemischte_zahlen():
    number1 = 8
    number2 = -4
    expected_result = 5

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"

if __name__ == "__main__":
    pytest.main()
