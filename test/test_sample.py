
import pytest
from app.calculation_test import BankAccount, add,sub,mul,div

@pytest.mark.parametrize("num1,num2,expected",[
    (3,2,5),(7,1,8),(12,4,16)
])
def test_add(num1,num2,expected):
    assert add(num1,num2) ==expected

def test_sub():
    assert sub(5,3) == 2

def test_mul():
    assert mul(5,3) == 15

def test_div():
    assert div(6,3) == 2

@pytest.fixture
def zero_bank():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("deposit,debit,expected",[
    (200,100,100),(100,20,80)
])
def test_transaction(zero_bank,deposit,debit,expected):
    zero_bank.deposit(deposit)
    zero_bank.debit(debit)
    assert zero_bank.balance == expected

def test_back_initial_amount(zero_bank):
    assert zero_bank.balance ==0

def test_bank_default_amount(zero_bank):
    assert zero_bank.balance==0

def test_withdraw(bank_account):
    bank_account.debit(10)
    assert bank_account.balance == 40

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance ==70

def test_interest(bank_account):
    bank_account.interest()
    assert round(bank_account.balance,6) ==55

