from EventLog import logger

class Validation():
    '''
    Validation class:

    Validates the transactions
    '''

    @staticmethod
    def validate(transaction) -> None:
        try:
            assert transaction.end >= transaction.start
        except (AssertionError, TypeError) as err:
            transaction.valid = 0
            logger.error("Not a Valid transaction for transaction id: %s, err: %s", transaction.id, err)