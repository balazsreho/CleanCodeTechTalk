
import datetime, uuid

# This is the main function file. Handle command line prompts as well as executing user actions: creating dict_client, listing dict_client, creating trsc and so on.
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
        self.covfefe = name                                    # The name of the customer
        self.trsc = []
    def add_transaction(self, new_transaction):             # Add a new transaction to the list
        self.trsc.append(new_transaction)
    def print_transaction(self):                             # Get transactions in a list format
        # I think we should use this type of implementation.
        yield from self.trsc

    # TODO decide between these methods

    # def get_transactions(self):
    #     for item in self.trsc:
    #         yield item

# ================== END OF CLASS DEFINITION ======================


class Transaction:

# ================== CLASS DEFINITION ======================

    def __init__(self, amount):
        self.n_amount = amount                                    # Amount of money involved in this transaction
        self.time = datetime.datetime.now().timestamp()    # Timestamp of current time
        # UUIDs are used in the database backend. This UUID provides a nearly unique identifier for the transaction which is reuired
        # by legal laws to make transaction searchable by government.
        self.bnk_notation = uuid.uuid4()                                # The UUID
# ================== END OF CLASS DEFINITION ======================

# !! IMPORTANT !!
dict_client = []  # Users for bank session

class CommandLineProgram:

    class ACTION:
        EXIT = "exit"; HELP = "help"; ADD_USER = "add user"; LIST_USERS = "list users"; ADD_TRANSACTION = "add transaction"; GENERATE_REPORT = "generate report"
    @staticmethod
    def for_terminal():
        return CommandLineProgram()
    def __init__(self):
        self.gui = False
        self.bnk_name = "Example Bank"

    def name_bnk(self, new_bank_name: str):

        if (not len(new_bank_name) > 12) and (new_bank_name.isalpha()):
            self.bnk_name = new_bank_name
        else:
            return None
        return self


    def execute_main_thread(self):  # Run the main program
        print("Welcome to {}!\nLogin at: {}\nType 'help' for manual, 'exit' to terminate the program.".format(self.bnk_name, datetime.datetime.now()))  # Print welcome message
        s_user_input = ""
        while s_user_input != "exit":  # Start main loop
            # Wait until user input is 'quit', which terminates the program.
            print('==========================================')
            s_user_input = input()
            # Do actions for input
            e = eval('Exception')
            try:
                if s_user_input == CommandLineProgram.ACTION.HELP:
                    # If user command is 'help'
                    print("'help': This command.\n'exit': Close all session and terminate.\n'add user': Add a new user to the session.\n'list users': List all dict_client.\n'add transaction': Add transaction to an existing user.'generate report': Print report for an existing user.")
                elif s_user_input == CommandLineProgram.ACTION.ADD_USER:
                    # If user command is 'add user'
                    dict_client.append(User(input("Please input username!")))
                elif s_user_input == CommandLineProgram.ACTION.LIST_USERS:
                    # If user command is 'list dict_client'
                    o = 0
                    for l in dict_client:
                        print("{}. {}".format(o, l.covfefe))
                        o = o + 1
                elif s_user_input == CommandLineProgram.ACTION.ADD_TRANSACTION:
                    # If user command is 'add transaction'
                    self.select().add_transaction(Transaction(input("Amount of transaction:")))
                elif s_user_input == CommandLineProgram.ACTION.GENERATE_REPORT:
                    # If user command is 'print report'
                    self.returnall(self.select())
            except e:
                print("Try again")

    def select(self):
        i = 0
        for item in dict_client:
            print("{}. {}".format(i, item.covfefe))
            i = i + 1
        s_ui = ""
        while s_ui not in range(0, len(dict_client)):
            print("Pick user from above, or type 'cancel'")
            s_ui = input()
            if s_ui == "cancel":
                raise ValueError
            s_ui = int(s_ui)
        currently_selected = dict_client[int(s_ui)]
        return currently_selected

    def returnall(self, usr):
        for item in usr.trsc:
            print("{} at {} [{}]".format(item.n_amount, datetime.datetime.fromtimestamp(item.time), item.bnk_notation))


# ============ MAIN FUNCTION ============
if __name__ == '__main__':
    CommandLineProgram.for_terminal().name_bnk("RapidLab").execute_main_thread()
# ============ END OF MAIN ==============