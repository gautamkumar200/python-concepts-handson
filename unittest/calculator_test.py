import unittest
from unittest import mock
from unittest.mock import MagicMock

from calculator.calculator import Calculator
from calculator.calculator_service import CalculatorService


class CalculatorTest(unittest.TestCase):

    # def setUp(self):
    #     self.calserv = CalculatorService()
    #     self.calculator = Calculator(calserv)

    def test_add(self, mock_test=None):
        # with mock.patch("calculator.calculator.Calculator")as mock_obj:
        #     instance = mock_obj.return_value
        #
        #     print(instance, mock_obj)

        calserv = MagicMock()
        calserv.add.return_value = 7
        #print(calserv)
        calculator = Calculator(calserv)

        self.assertEqual(calculator.add(2, 5), 7)

        with mock.patch("calculator.calculator_service.CalculatorService")as calculator_service:
            calculator_service.add.return_value = 7
            calculator = Calculator(calculator_service)
            # print(calculator_service.__dict__)
            self.assertEqual(calculator.add(2, 5), 7)


