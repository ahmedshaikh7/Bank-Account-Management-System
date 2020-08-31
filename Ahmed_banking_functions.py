"""Amazing Banking Corporation functions"""
from typing import List, Tuple, Dict, TextIO

# Constants
# client_to_accounts value indexing
BALANCES = 0
INTEREST_RATES = 1

# transaction codes
WITHDRAW_CODE = -1
DEPOSIT_CODE = 1

LOAN_INTEREST_RATE = 2.2 #percent

## ------------ HELPER FUNCTIONS GIVEN BELOW -----------
# do not modify

def display_client_accounts(client_to_accounts: Dict, client: Tuple)-> None:
    ''' Display the indicated client's account balances in a human-friendly
    format, using the client_to_account dictionary.

    The first account is a chequing account, followed by subsequent savings
    account(s). A loan account, if present, is signified as the last account
    if it has a negative balance.
    
    >>> display_client_accounts({('Ali Ashraf', 568123430): [[240.0, 3000.0], \ >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] ,[0.8, \
    >>> 1.2]]}, ('Ali Ashraf', 568123430))
    Chequing Account
    $ 240.00
    Savings Account 1
    $ 3000.00
    
    >>> display_client_accounts({('Ali Ashraf', 568123430): [[240.0, 3000.0], \ >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0, 450.0, \
    >>> -3000.0] ,[0.8, 1.2, 1.5, 1.1]]}, ('Bhav Mehta', 113456090))
    Chequing Account
    $ 900.00
    Savings Account 1
    $ 180.00
    Savings Account 2
    $ 450.00
    Loan Account
    $ -3000.00 '''
    
    i = 0
    for account in client_to_accounts[client][BALANCES]:
        if i == 0:
            # the first account is always a chequing account
            print("Chequing Account")
        elif account > 0:
            print("Savings Account {}".format(i))
        else:
            print("Loan Account")
        print("$ {:.2f}".format(account))
        i += 1
        
def get_fv(present_value: float, r: float, n: int)->float:
    ''' Return the future value calculated using the given present value (pv)
    growing with rate of return (interest rate) r, compounded annually,
    for a total of n years.

    r is given as a percentage value.
    
    >>> get_fv(1090, 0.99, 18)
    1301.4790976812887
    
    >>> get_fv(4110, 1.5, 13)
    4987.700544977508 '''
    
    return present_value * (1 + r/100)**n


def get_sd(x: List[float]) -> float:
    '''
    Return the standard deviation of the values in the list x.
    
    >>>get_sd([300.0, 4000.0, 290.0, 313.0])
    1601.7347431769094
    
    >>>get_sd([200.0, 340.0, 311.0, 779.0])
    220.7583520503811 '''
    
    n = len(x)
    x_bar = (sum(x))/n
    
    sd = 0
    for x_i in x:
        sd += (x_i - x_bar) ** 2

    return (sd/n) ** 0.5


### ----------- END OF PROVIDED HELPER FUNCTIONS --------------
# Implement the required functions below
def get_num_clients(client_to_accounts: Dict[Tuple[str, int],
                                             List[List[float]]])->int:
    ''' Returns the number of clients present in the client_to_accounts dictionary.

    >>> get_num_clients({('Bob', 555555555): [[100.0], [1.0]], \
    >>> ('Sally', 123123123): [[250.0], [2.0]]})
    2
    >>> get_num_clients{('Ali', 568123430): [[240.0, 3000.0] , [4.2, 2.1]]}
    1 '''
    # complete this function
    
    return len(client_to_accounts) 
    

def validate_identity(client_to_accounts: Dict[Tuple[str, int], List[List[float]]], name_client: str, sin_number: int)->bool:
    
    ''' Returns true if the name and SIN  represents a valid client in the clien
    t to accounts dictionary - false otherwise
    
    >>> validate_identity({('Ali Ashraf', 568123430): [[240.0, 3000.0] , [4.2, \ 
    >>> 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8,\
    >>> 1.2]]}, 'Ali Ashraf', 568123430)
    True
    
    >>> validate_identity({('Ali Ashraf', 568123430): [[240.0, 3000.0] , [4.2, \ 
    >>> 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8,\
    >>> 1.2]]}, 'Ali Ahmed', 560023430)
    False
    '''
    
    if (name_client, sin_number) in client_to_accounts.keys():
        return True
    return False



def get_fv_from_accounts(lst_balance: List[float],
                         lst_interest: List[float],time: int) -> float:
    
    ''' Returns the sum of all the future values of all the account balances
    according to their respective interest rates
    
    >>> get_fv_from_accounts([450.0, 200.0], [1.1, 0.7], 3)
    669.2434175499998
    
    >>> get_fv_from_accounts([2000.0, 3000.0, 900.0], [1.5, 3.0, 4.7], 6)
    6954.600855330112
    '''
    
    new_list = []
    for i in range(len(lst_balance)):
        fv = get_fv(lst_balance[i], lst_interest[i], time)    
        new_list.append(fv)
    total = sum(new_list)
    return total




def get_num_accounts(client_to_accounts: Dict[Tuple[str, int], List[List[float]]]
                     , valid_client: Tuple[str, int]) -> int:
    
    ''' Returns the total number of accounts the client has open, not including loan accounts
    
    >>> get_num_accounts({('Ali Ashraf', 568123430): [[240.0, 3000.0] , [4.2, \ >>> 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8,\
    >>> 1.2]]},('Ali Ashraf', 568123430))
    2
    
    >>> get_num_accounts({('Ali Ashraf', 568123430): [[240.0, 500.0, 3000.0], \ >>> [4.2, 2.1, 6.0]] , ('Bhav Mehta', 113456090): [[900.0, 300.0, 180.0], \ >>> [0.8, 1.2, 1.5]]}, ('Bhav Mehta', 113456090))
    3
    
    '''  
    count = 0
    for i in range(len(client_to_accounts[valid_client][BALANCES])):
        if (i>=0):
            count+=1
    return count


def get_client_to_total_balance(client_to_accounts: Dict[Tuple[str, int], List[List[float]]]) -> Dict[Tuple[str, int], float]:
    
    ''' Returns a dictionary summing up the account balances for for each respective client
    
    >>> get_client_to_total_balance({('Ali Ashraf', 568123430): [[240.0, \
    >>> 3000.0] , [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0], \ >>> [0.8, 1.2]]})
    {('Ali Ashraf', 568123430): 3240.0, ('Bhav Mehta', 113456090): 1080.0}'
    
    >>> get_client_to_total_balance({('Ali Ashraf', 568123430): [[240.0, 500.0, >>> 3000.0] , [4.2, 2.1, 6.0]] , ('Bhav Mehta', 113456090): [[900.0, 300.0, >>> 180.0] , [0.8, 1.2, 1.5]]})
    {('Ali Ashraf', 568123430): 3740.0, ('Bhav Mehta', 113456090): 1380.0}  
    
    '''
    new_dictionary = {}
    for key in client_to_accounts:
        account_list = client_to_accounts[key][BALANCES]
        total = sum(account_list)
        new_dictionary.update({key: total})
    return new_dictionary
        
               
                
def get_account_balance(client_to_accounts: Dict[Tuple[str, int]
                                                 , List[List[float]]]
                        , valid_client: Tuple[str, int], acct_number: int) -> float:
    
    '''Returns the specific account balance of the account number given according to the respective client
    
    
    >>> get_account_balance({('Ali Ashraf', 568123430): [[240.0, \
    >>> 3000.0] , [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0], \ >>> [0.8, 1.2]]}, ('Ali Ashraf', 568123430), 1)
    3000.0

    >>> get_account_balance({('Ali Ashraf', 568123430): [[240.0, \
    >>> 3000.0] , [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0], \ >>> [0.8, 1.2]]}, ('Bhav Mehta', 113456090), 0)
    900.0  '''
    
    return client_to_accounts[valid_client][BALANCES][acct_number]
         
        
def load_financial_data(filename: TextIO) -> Dict[Tuple[str, int], List[List[float]]]:
    '''
    This function builds a "client to accounts" dictionary with the data from the open file, and return it accordingly
    
    '''
    
    file_data = filename.readlines()
    for i in range(len(file_data)):
        file_data[i] = file_data[i].strip()
    info = (file_data[0], int(file_data[1].replace(" ", "")))
    account_list = []
    interest_list = []
    flag = False
    counter = 0
    dic = {}
    for i in range(2, len(file_data)):
        if flag and counter == 2:
            flag = False
        if file_data[i] == '':
            account_list = []
            interest_list = []
            info = (file_data[i + 1], int(file_data[i + 2].replace(" ", "")))
            flag = True
            counter = 0
            continue
        if flag and counter < 2:
            counter += 1
            continue
        if i%3 == 0:
            index = file_data[i].find(":")
            account_list.append(float(file_data[i][index+2:]))
        elif i%3 == 1:
            index = file_data[i].find(":")
            interest_list.append(float(file_data[i][index + 2:]))

        dic[info] = [account_list, interest_list]

    return dic    
    
       

def get_financial_range_to_clients(client_ttl: Dict[Tuple[str, int], float], financial_ranges: List[Tuple[float, float]])-> Dict[Tuple[float, float], List[Tuple[str, int]]]:
    
    '''Returns a dictionary for each of the clients whose total balances are within the financial ranges specified
    
    >>> get_financial_range_to_clients({('Azmat Shah', 110893321): 200.0, \
    >>> ('Folan Mar', 821475370): 309453.0, ('Jack Marky', 698887173): 3234.0}, >>> [(300, 11000), (10, 199), (600, 1000)])
    {(300, 11000): [('Jack Marky', 698887173)]}
    
    >>> get_financial_range_to_clients({('Azmat Shah', 110893321): 200.0, \ 
    >>> ('Folan Mar', 821475370): 309453.0, ('Jack Marky', 698887173): 3234.0}, >>> [(100, 1990), (10, 199), (600, 10000)])
    {(100, 1990): [('Azmat Shah', 110893321)],
    (600, 10000): [('Jack Marky', 698887173)]} '''
    
    new_dict = {}
    for item in financial_ranges:
        lst = []
        for v in client_ttl:
            if client_ttl[v] >= item[0] and client_ttl[v]<= item[1]:
                lst+=[v]
                new_dict[item] = lst  
    return new_dict 
                        
    
def time_to_client_goal(client_to_accounts: Dict[Tuple[str, int], List[List[float]]], valid_client: Tuple[str, int], financial_goal: float)->int:
    
    ''' Returns the smallest number of integer years it takes for a client's total balance to exceed his goal given his PV,current bank balance and rates of return
    
    >>> time_to_client_goal({('Ali Ashraf', 568123430): [[240.0, 3000.0], \
    >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8, \
    >>> 1.2]]}, ('Ali Ashraf', 568123430), 1034500)
    199
    
    >>> time_to_client_goal({('Ali Ashraf', 568123430): [[240.0, 3000.0] , \ 
    >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8, \
    >>> 1.2]]}, ('Bhav Mehta', 113456090), 19939)
    322 '''

    time=0
    lst_balance = client_to_accounts[valid_client][BALANCES]
    lst_interest = client_to_accounts[valid_client][INTEREST_RATES]
    while get_fv_from_accounts(lst_balance, lst_interest, time) < financial_goal:
        time+=1
    return time
    
        
def open_savings_account(client_to_accounts: Dict[Tuple[str, int], List[List[float]]], valid_client: Tuple[str, int], balance: float, interest_rate: float) -> None:
    
    ''' Updates the client_to_accounts dictionary when a new account is added (with respective rates) - if the client doesn't have a loan account its added at the end of the list, if the client does have a loan account, its added 1 before the loan account
    
    
    >>> open_savings_account({('Ali Ashraf', 568123430): [[240.0, 3000.0] , \ 
    >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , 180.0] , [0.8, \
    >>> 1.2]]}, ('Ali Ashraf', 568123430), 300, 4.5)
    {('Ali Ashraf', 568123430): [[240.0, 3000.0, 300], [4.2, 2.1, 4.5]], ('Bhav Mehta', 113456090): [[900.0, 180.0], [0.8, 1.2]]}
    
    >>> open_savings_account({('Ali Ashraf', 568123430): [[240.0, 3000.0] , \
    >>> [4.2, 2.1]] , ('Bhav Mehta', 113456090): [[900.0 , -180.0] , [0.8, \
    >>> 1.2]]}, ('Bhav Mehta', 113456090), 1000, 0.5)
    {('Ali Ashraf', 568123430): [[240.0, 3000.0], [4.2, 2.1]], ('Bhav Mehta', 113456090): [[900.0, 1000, -180.0], [0.8, 0.5, 1.2]]} '''
    
    balance_list = client_to_accounts[valid_client][BALANCES]
    interests_list = client_to_accounts[valid_client][INTEREST_RATES]
    
    if balance_list[-1] < 0:
        balance_list.insert(-1, balance)
        interests_list.insert(-1, interest_rate)        
    else:
        balance_list.append(balance)
        interests_list.append(interest_rate)
            
    print(client_to_accounts)
        
    
def update_balance(client_to_accounts: Dict[Tuple[str, int], List[List[float]]], valid_client: Tuple[str, int], account_num: int, change_in_balance: float, withdraw_or_deposit: int) -> None:
    
    ''' This function updates the client to accounts dictionary, where the client's account balance, indicated by the account number, is modified by withdrawing the amount indicated if the transaction code is WITHDRAW_CODE, or depositing the amount indicated if the transaction code is DEPOSIT_CODE. If the transaction is a withdrawal, the function does not need to check if the account has sufficient funds to withdraw the specified amount. 
    
    >>> update_balance({('Karla Hurst', 770898021): [[768.0, 2070.0], [0.92, 
    >>> 1.5]], ('Pamela Dickson', 971875372): [[36358866.0, 5395448.0, 23045442.0,
    >>> 14316660.0, 45068981.0, 4438330.0, 16260321.0, 7491204.0, 23330669.0], >>> [2.3, 2.35, 2.25, 2.35, 2.05, 2.1, 2.45, 2.4, 2.0]], ('Roland Lozano', >>> 853887123): [[1585.0, 1170.0, 1401.0, 3673.0], [0.63, 0.05, 0.34, 
    >>> 0.92]]}, ('Pamela Dickson', 971875372), 1, 300, WITHDRAW_CODE)
    
    >>> update_balance({('Karla Hurst', 770898021): [[768.0, 2070.0], [0.92, 
    >>> 1.5]], ('Pamela Dickson', 971875372): [[36358866.0, 5395448.0, 23045442.0,
    >>> 14316660.0, 45068981.0, 4438330.0, 16260321.0, 7491204.0, 23330669.0], >>> [2.3, 2.35, 2.25, 2.35, 2.05, 2.1, 2.45, 2.4, 2.0]], ('Roland Lozano', >>> 853887123): [[1585.0, 1170.0, 1401.0, 3673.0], [0.63, 0.05, 0.34, 
    >>> 0.92]]}, ('Karla Hurst', 770898021), 2, 400, DEPOSIT_CODE) '''
    
    for key, value in client_to_accounts.items():
        if key == valid_client:
            if (withdraw_or_deposit == WITHDRAW_CODE):
                value[0][account_num] -= change_in_balance
            if (withdraw_or_deposit == DEPOSIT_CODE):
                value[0][account_num] += change_in_balance  
    
      
def get_loan_status(client_to_accounts: Dict[Tuple[str, int], List[List[float]]], client_to_total_balance: Dict[Tuple[str, int], float], valid_client: Tuple[str, int], loan: float) -> bool:
    
    ''' This function return True if the loan is approved and False otherwise. If the loan is approved, the function should modify the balance of the client's chequing account to be increased by the loan amount. Additionally, a new account should be opened at the end of the list with a negative balance of the loan amount, with a loan interest rate of LOAN_INTEREST_RATE. 
    
    
    >>> client_to_accounts = {('Karla Hurst', 778090111): [[768.0, 2070.0, \ 
    >>> -2000,], [0.92, 1.5, 30.0]]}
    >>> client_to_total_balance = {('Karla Hurst', 778090111): 838}
    >>> valid_client = ('Karla Hurst', 778090111)
    >>> get_loan_status(client_to_accounts, client_to_total_balance, 
    >>> valid_client, 8000)
    False
    
    >>> client_to_accounts = {('Karla Hurst', 778090111): [[768.0, 2070.0, \ >>> -500], [0.92, 1.5, 4.1]]}
    >>> valid_client = ('Karla Hurst', 778090111)
    >>> client_to_total_balance = {('Karla Hurst', 778090111): 2338}
    >>> get_loan_status(client_to_accounts, client_to_total_balance, \ 
    >>> valid_client, 400)
    True '''
    
    
    loan_approval = False
    loan_flag = False
    client_accounts = client_to_accounts[valid_client]
    neg_counter = 0
    counter = 0
    for account in client_accounts:
        for i in range(len(account)):
            if counter == 0 and account[i] < 0:
                neg_counter += 1
            if counter == 1 and account[i] == 2.2:
                if client_accounts[0][i] < 0:
                    loan_flag = True
        counter += 1
        if neg_counter == len(client_accounts[0]):
            return loan_approval

    points = 0
    average_total_balance = 0
    for client, value in client_to_total_balance.items():
        average_total_balance += value
    average_total_balance = average_total_balance / len(client_to_total_balance)

    sd_list = []

    for client, balance in client_to_total_balance.items():
        sd_list.append(balance)

    standard_dev = get_sd(sd_list)

    total_balance = client_to_total_balance[valid_client]

    if total_balance > average_total_balance:
        points += 1
    if total_balance >= loan:
        points += 1

    for balance in client_accounts[0]:
        if balance > loan and not loan_flag:
            points += 5
        if balance < average_total_balance - standard_dev:
            points -= 2
        if balance > average_total_balance + standard_dev:
            points += 2

    if points >= 5:
        loan_approval = True

    if loan_approval:
        client_to_accounts[valid_client][0][0] += loan
        client_to_accounts[valid_client][0].append(-1 * loan)
        client_to_accounts[valid_client][1].append(LOAN_INTEREST_RATE)
    return loan_approval    
    
    
if __name__ == "__main__":
    #import doctest
    # uncomment the following line to run your docstring examples
    #doctest.testmod()
    pass


