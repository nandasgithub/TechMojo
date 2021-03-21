from os import stat
from typing import Dict, List
from Transaction import Transaction
from Validation import Validation

class Util():
    '''
    Util class:

    Maintains helper functions
    '''

    @staticmethod
    def read_data() -> List:
        with open('test/test_data/input.txt') as f:
            transactions = f.read().split('\n')
        return transactions

    @staticmethod
    def get_transaction_data(transactions) -> List:
        transaction_data: Dict[str, Transaction] = {}
        for transaction in transactions:
            transaction_id, date, time, transaction_type = [item.strip() for item in transaction.split(',')]
            if transaction_id not in transaction_data:
                reference_to_transaction = Transaction(transaction_id)
                transaction_data[transaction_id] = reference_to_transaction
            reference_to_transaction = transaction_data.get(transaction_id, None)
            if not reference_to_transaction:
                continue    
            reference_to_transaction.set_time(date, time, transaction_type.lower())
        return transaction_data.values()

    @staticmethod
    def validate_transactions(transactions) -> None:
        for transaction in transactions:
            Validation.validate(transaction)
