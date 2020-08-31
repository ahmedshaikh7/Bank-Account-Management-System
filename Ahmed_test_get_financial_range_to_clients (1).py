"""A3. Test cases for function banking_functions.get_financial_range_to_clients.
"""

import unittest
import banking_functions


class TestGetFinancialRangeToClients(unittest.TestCase):
    """Test cases for function
    banking_functions.get_financial_range_to_clients.
    """

    def test_00_empty(self):
        param1 = {}
        param2 = [()]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_within_one_range(self):
        param1 = {('Bob Bob', 786543210): 10.0}
        param2 = [(0, 100000)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {(0, 100000): [('Bob Bob', 786543210)]}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_02_two_person_within_range(self):
        param1 = {('Bob Bob', 786543210): 10.0, ('Ali Ali', 989090123): 45.0}
        param2 = [(0, 100000), (10,200)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {(0, 100000): [('Bob Bob', 786543210), ('Ali Ali', 989090123)], (10, 200): [('Bob Bob', 786543210), ('Ali Ali', 989090123)]}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
        
        
    def test_03_upper_limit_value(self):
        param1 = {('Bob Bob', 786543210): 10.0}
        param2 = [(0, 10)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {(0, 10): [('Bob Bob', 786543210)]}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
        
               
    def test_04_lower_limit_value(self):
        param1 = {('Bob Bob', 786543210): 10.0}
        param2 = [(10, 50)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {(10, 50): [('Bob Bob', 786543210)]}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_05_one_above_upper_limit_value(self):
        param1 = {('Bob Bob', 786543210): 11.0}
        param2 = [(0, 10)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     
    
    def test_06_one_below_lower_limit_value(self):
        param1 = {('Bob Bob', 786543210): 10.0}
        param2 = [(11, 20)]
        actual = banking_functions.get_financial_range_to_clients(param1, param2)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     


if __name__ == '__main__':
    unittest.main(exit=False)
