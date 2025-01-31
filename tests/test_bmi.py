import sys
import os
from day_01.bmi_calculator import BMICalculator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


def test_normal_bmi():
    assert BMICalculator.calculate(70, 175) == 22.9


def test_invalid_height():
    assert BMICalculator.calculate(70, 0.4) is None
