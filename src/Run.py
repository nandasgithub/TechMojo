from Average import Average
from Util import Util

def main():
    # Read the trasactions
    raw_transactions = Util.read_data()
    transactions = Util.get_transaction_data(raw_transactions)

    # Validate the transactions
    Util.validate_transactions(transactions)

    # Get average run time of the transactions
    reference_to_average = Average(transactions)
    return reference_to_average.get_average()

if __name__ == '__main__':
    print(main())