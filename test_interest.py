import pytest
from interest import InterestCalculator
from interest import DataValidator

def testCalculatorNominalValues():
    calculator = InterestCalculator()
    expected_output = 1467.6331510028724

    actual_output = calculator.calculate_interest(10000.0, 10.0, 12.0)

    assert actual_output == expected_output

def testCalculatorLowerBounaryValues():
    calculator = InterestCalculator()
    expected_output = 0.1

    actual_output = calculator.calculate_interest(0.1, 0.1, 1)

    assert actual_output == expected_output

def testDataValidatorNominalValues():
    validator = DataValidator()
    expected_output = True

    actual_output = validator.validate_data(10000.0, 10.0, 12.0)

    assert actual_output == expected_output