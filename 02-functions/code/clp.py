
import datetime, user
import transaction


# !! IMPORTANT !!
users = []  # Users for bank session

class CommandLineProgram:

    class ACTION:
        EXIT = "exit"; HELP = "help"; ADD_USER = "add user"; LIST_USERS = "list users"; ADD_TRANSACTION = "add transaction"; GENERATE_REPORT = "generate report"
    @staticmethod
    def for_terminal():
        return CommandLineProgram().disable_gui()
    def __init__(self):
        self.gui = True
        self.bank_name = "Example Bank"


    def disable_gui(self):
        # NOTE: this function now does not work
        self.gui = False
        return self

    def name_bank(self, new_bank_name: str):

        if self.is_bank_name_valid(new_bank_name):
            self.bank_name = new_bank_name
        else:
            raise ValueError("Bank name is not valid!")
        return self

    def is_bank_name_valid(self, name_to_check: str):
        # Here we check if th new name is not longer than 12 and only contains letters
        return True if (not len(name_to_check) > 12) and (name_to_check.isalpha()) else False

    def run(self):  # Run the main program
        self.print_welcome()  # Print welcome message
        self.handle_inputs()  # Start main loop

    def print_welcome(self):
        print("Welcome to {}!\nLogin at: {}\nType 'help' for manual, 'exit' to terminate the program.".format(self.bank_name, datetime.datetime.now()))
    def print_help(self):
        print("'help': This command.\n'exit': Close all session and terminate.\n'add user': Add a new user to the session.\n'list users': List all users.\n'add transaction': Add transaction to an existing user.'generate report': Print report for an existing user.")
    def print_divider(self):
        print('==========================================')

    def input_and_create_user(self):
        print("Please input username!")
        users.append(user.User(input()))

    def print_users(self):
        i = 0
        for item in users:
            print("{}. {}".format(i, item.name))
            i = i + 1

    def prompt_user_selection(self):
        self.print_users()
        user_input = self.input_for_user_selection()
        currently_selected = users[int(user_input)]
        return currently_selected

    def input_for_user_selection(self):
        user_input = ""
        while user_input not in range(0, len(users)):
            print("Pick user from above, or type 'cancel'")
            user_input = input()
            if user_input == "cancel":
                raise ValueError
            user_input = int(user_input)
        return user_input

    def select_user_and_add_transaction(self):
        self.prompt_user_selection().add_transaction(transaction.Transaction(input("Amount of transaction:")))

    def print_all_transaction(self, selected_user):
        for item in selected_user.transactions:
            print("{} at {} [{}]".format(item.amount, datetime.datetime.fromtimestamp(item.timestamp), item.uuid))

    def select_user_and_print_report(self):
        self.print_all_transaction(self.prompt_user_selection())

    def handle_inputs(self):
        user_input = ""
        while user_input != "exit":
            # Wait until user input is 'quit', which terminates the program.
            self.print_divider()
            user_input = input()
            self.do_action_for_input(user_input)

    def do_action_for_input(self, user_input):
        # Do actions for input
        try:
            if user_input == CommandLineProgram.ACTION.HELP:
                # If user command is 'help'
                self.print_help()
            elif user_input == CommandLineProgram.ACTION.ADD_USER:
                # If user command is 'add user'
                self.input_and_create_user()
            elif user_input == CommandLineProgram.ACTION.LIST_USERS:
                # If user command is 'list users'
                self.print_users()
            elif user_input == CommandLineProgram.ACTION.ADD_TRANSACTION:
                # If user command is 'add transaction'
                self.select_user_and_add_transaction()
            elif user_input == CommandLineProgram.ACTION.GENERATE_REPORT:
                # If user command is 'print report'
                self.select_user_and_print_report()
        except Exception:
            print("Try again")