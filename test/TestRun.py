import sys
import os
sys.path.insert(1, os.getcwd() + '/src')
from datetime import timedelta
from typing import List
from src.Transaction import Transaction
from src.Util import Util
from src.Average import Average

class TestRun():

    def __init__(self, transactions: List[Transaction]) -> None:
        self.transactions = transactions

    @staticmethod
    def get_transactions():
        return Util.get_transaction_data(Util.read_data())

    def get_invalid_transactions(self):
        invalid_transaction_count = 0
        for transaction in self.transactions:
            if transaction.valid == 0:
                invalid_transaction_count += 1
        return invalid_transaction_count


def main():
    transactions = TestRun.get_transactions()
    assert len(transactions) == 3

    Util.validate_transactions(transactions)

    test_run = TestRun(transactions)
    invalid_transaction_count = test_run.get_invalid_transactions()
    assert invalid_transaction_count == 1

    expected_average_time = timedelta(hours=6, minutes=2, seconds=30)
    average_time = Average(transactions).get_average()
    assert average_time == expected_average_time 

if __name__ == '__main__':
    main()
