from datetime import timedelta
from EventLog import logger

class Average():
    '''
    Average class:

    Returns the average time of all the transactions

    Parameters:
        arg1: transactions
    '''

    def __init__(self, transactions) -> None:
        self.transactions = transactions

    def get_average(self) -> timedelta:
        transaction_time = timedelta(0)
        invalid_transactions = 0
        for transaction in self.transactions:
            if not transaction.valid:
                invalid_transactions += 1
                continue
            transaction_time += transaction.get_time_difference()
        try:
            return transaction_time/(len(self.transactions)-invalid_transactions)
        except ZeroDivisionError as err:
            logger.error("No Valid Transactions, invalid_transactions count: %s", invalid_transactions)