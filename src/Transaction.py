from datetime import datetime, timedelta
from EventLog import logger
from env import env_json

class Transaction():
    '''
    Transaction class:

    Keeps track of Start time and End time of each transaction

    Parameters:
        arg1: transaction_id
    '''

    def __init__(self, id) -> None:
        self.id = id
        self.start_date = None
        self.end_date = None
        self.start_time = None
        self.end_time = None
        self.start = None
        self.end = None
        self.valid = 1

    def set_time(self, date, time, transaction_type):
        try:
            if transaction_type == 'start':
                self.start_date = date
                self.start_time = time
                self.start = datetime.strptime(date + ' ' + time, env_json.get('TRANSACTION_DATE_TIME_FMT'))
            elif transaction_type == 'end':
                self.end_date = date
                self.end_time = time
                self.end = datetime.strptime(date + ' ' + time, env_json.get('TRANSACTION_DATE_TIME_FMT'))
        except ValueError:
            logger.error("Unable to convert to datetime object with date: %s and time: %s", date, time)

    def get_start(self) -> datetime:
        return self.start

    def get_end(self) -> datetime:
        return self.end

    def get_time_difference(self) -> timedelta:
        return self.end - self.start
