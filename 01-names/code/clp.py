
import datetime, user, uuid

# This is the main function file. Handle command line prompts as well as executing user actions: creating users, listing users, creating transactions and so on.
# Call this file to start the execution engine.

"""
Developed by Balazs Reho

Work-Log:

2017-07-10:     Start initial working

2017-07-11:     Some refactoring in clp.py after random meeting notes.

"""


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

# !! IMPORTANT !!
users = []  # Users for bank session

class CommandLineProgram:

    class ACTION:
        EXIT = "exit"; HELP = "help"; ADD_USER = "add user"; LIST_USERS = "list users"; ADD_TRANSACTION = "add transaction"; GENERATE_REPORT = "generate report"
    @staticmethod
    def for_terminal():
        return CommandLineProgram()
    def __init__(self):
        self.gui = False
        self.bank_name = "Example Bank"

    def name_bank(self, new_bank_name: str):

        if (not len(new_bank_name) > 12) and (new_bank_name.isalpha()):
            self.bank_name = new_bank_name
        else:
            return None
        return self


    def run(self):  # Run the main program
        print("Welcome to {}!\nLogin at: {}\nType 'help' for manual, 'exit' to terminate the program.".format(self.bank_name, datetime.datetime.now()))  # Print welcome message
        user_input = ""
        while user_input != "exit":  # Start main loop
            # Wait until user input is 'quit', which terminates the program.
            print('==========================================')
            user_input = input()
            # Do actions for input
            try:
                if user_input == CommandLineProgram.ACTION.HELP:
                    # If user command is 'help'
                    print("'help': This command.\n'exit': Close all session and terminate.\n'add user': Add a new user to the session.\n'list users': List all users.\n'add transaction': Add transaction to an existing user.'generate report': Print report for an existing user.")
                elif user_input == CommandLineProgram.ACTION.ADD_USER:
                    # If user command is 'add user'
                    users.append(user.User(input("Please input username!")))
                elif user_input == CommandLineProgram.ACTION.LIST_USERS:
                    # If user command is 'list users'
                    i = 0
                    for item in users:
                        print("{}. {}".format(i, item.name))
                        i = i + 1
                elif user_input == CommandLineProgram.ACTION.ADD_TRANSACTION:
                    # If user command is 'add transaction'
                    self.prompt_user_selection().add_transaction(Transaction(input("Amount of transaction:")))
                elif user_input == CommandLineProgram.ACTION.GENERATE_REPORT:
                    # If user command is 'print report'
                    self.print_all_transaction(self.prompt_user_selection())
            except Exception:
                print("Try again")

    def prompt_user_selection(self):
        i = 0
        for item in users:
            print("{}. {}".format(i, item.name))
            i = i + 1
        user_input = ""
        while user_input not in range(0, len(users)):
            print("Pick user from above, or type 'cancel'")
            user_input = input()
            if user_input == "cancel":
                raise ValueError
            user_input = int(user_input)
        currently_selected = users[int(user_input)]
        return currently_selected

    def print_all_transaction(self, selected_user):
        for item in selected_user.transactions:
            print("{} at {} [{}]".format(item.amount, datetime.datetime.fromtimestamp(item.timestamp), item.uuid))


# ============ MAIN FUNCTION ============
if __name__ == '__main__':
    CommandLineProgram.for_terminal().name_bank("RapidLab").run()
# ============ END OF MAIN ==============