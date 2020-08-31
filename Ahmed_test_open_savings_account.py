"""A3. Test cases for function banking_functions.open_savings_account.
"""

import unittest
import banking_functions


class TesOpenSavingsAccount(unittest.TestCase):
    """Test cases for function
    banking_functions.get_client_to_total_balance.
    """

    def test_00_one_person_one_account(self):
        param = {('Bob Bob', 786543210):[[1.0], [1.5]]}
        banking_functions.open_savings_account(param, ('Bob Bob', 786543210), 2.0, 1.1)
        expected = {('Bob Bob', 786543210): [[1.0, 2.0], [1.5, 1.1]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)
        
    def test_01_two_person_two_account(self):
        param = {('Bob Bob', 786543210):[[1.0], [1.5]], ('Ali Ali', 786123210):[[5.0], [2.5]]}
        banking_functions.open_savings_account(param,('Ali Ali', 786123210), 6.0, 3.1)
        expected = {('Bob Bob', 786543210):[[1.0], [1.5]], ('Ali Ali', 786123210):[[5.0, 6.0], [2.5, 3.1]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)
        
        
    def test_02_zero_account_balance(self):
        param = {('Bob Bob', 786543210):[[0.0], [2.0]]}
        banking_functions.open_savings_account(param, ('Bob Bob', 786543210), 400.0, 1.1)
        expected = {('Bob Bob', 786543210): [[0.0, 400.0], [2.0, 1.1]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)    
        
        
    def test_03_zero_interest_rate(self):
        param = {('Bob Bob', 786543210):[[100.0], [0.0]]}
        banking_functions.open_savings_account(param, ('Bob Bob', 786543210), 300.0, 3.1)
        expected = {('Bob Bob', 786543210): [[100.0, 300.0], [0.0, 3.1]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)    
        
    
    def test_00_last_account_balance_zero(self):
        param = {('Bob Bob', 786543210):[[100.0, 54.0, 0.0], [3.0, 0.9, 1.0]]}
        banking_functions.open_savings_account(param, ('Bob Bob', 786543210), 99.0, 2.8)
        expected = {('Bob Bob', 786543210): [[100.0, 54.0, 0.0, 99.0], [3.0, 0.9, 1.0, 2.8]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)  
        
    def test_00_last_interest_rate_zero(self):
        param = {('Bob Bob', 786543210):[[100.0, 54.0, 45.0], [3.0, 0.9, 0.0]]}
        banking_functions.open_savings_account(param, ('Bob Bob', 786543210), 99.0, 2.8)
        expected = {('Bob Bob', 786543210): [[100.0, 54.0, 45.0, 99.0], [3.0, 0.9, 0.0, 2.8]]}
        msg = "Expected {}, but got {}".format(expected, param)
        self.assertEqual(param, expected, msg)    
        
    
        


if __name__ == '__main__':
    unittest.main(exit=False)
