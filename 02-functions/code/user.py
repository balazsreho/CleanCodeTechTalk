
import datetime, uuid

class User:

# ================== CLASS DEFINITION ======================

    def __init__(self, name):
        self.name = name                                    # The name of the customer
        self.transactions = []
    def add_transaction(self, new_transaction):             # Add a new transaction to the list
        self.transactions.append(new_transaction)
    def get_transactions(self):                             # Get transactions in a list format
        # I think we should use this type of implementation.
        yield from self.transactions

    # TODO decide between these methods

    # def get_transactions(self):
    #     for item in self.transactions:
    #         yield item

# ================== END OF CLASS DEFINITION ======================



class Transaction:

# ================== CLASS DEFINITION ======================

    def __init__(self, amount):
        self.amount = amount                                    # Amount of money involved in this transaction
        self.timestamp = datetime.datetime.now().timestamp()    # Timestamp of current time
        # UUIDs are used in the database backend. This UUID provides a nearly unique identifier for the transaction which is reuired
        # by legal laws to make transaction searchable by government.
        self.uuid = uuid.uuid4()                                # The UUID
# ================== END OF CLASS DEFINITION ======================