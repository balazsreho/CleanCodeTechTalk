#! /usr/bin/env/python
# coding=utf-8

# OS packages
import datetime
# Custom imports
import user
import transaction

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2017, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"


class CommandLineProgram:
    """
    Command Line Program which handles actions, inputs and reports through terminal.
    """

    @classmethod
    def for_terminal(cls):
        """
        Create a terminal based command line interface.
        :return: CommandLineProgram object.
        """
        _clp = CommandLineProgram()
        _clp.disable_gui()
        return _clp

    def __init__(self):
        self.gui = True
        self.bank_name = "Example Bank"
        self.users = []

    def disable_gui(self):
        self.gui = False

    def name_bank(self, new_bank_name: str):
        """
        Set the name of the bank.
        """
        if self.is_bank_name_valid(new_bank_name):
            self.bank_name = new_bank_name
        else:
            raise ValueError("Bank name is not valid!")

    def is_bank_name_valid(self, name_to_check: str):
        """
        Check if a new bank name is valid.
        """
        def is_name_too_long():
            return True if len(name_to_check) >= 12 else False

        def is_name_only_letter():
            return True if name_to_check.isalpha() else False

        return True if not is_name_too_long() and is_name_only_letter() else False

    def run(self):
        """
        Run main loop and handle user inputs.
        """
        self.print_welcome()
        self.handle_inputs()

    def print_welcome(self):
        print("Welcome to {}!".format(self.bank_name))
        print("Login at: {}".format(datetime.datetime.now()))
        print("Type 'help' for manual, 'exit' to terminate the program.")

    def print_help(self):
        print("'help': This command.")
        print("'exit': Close all session and terminate.")
        print("'add user': Add a new user to the session.")
        print("'list users': List all users.")
        print("'add transaction': Add transaction to an existing user.")
        print("'generate report': Print report for an existing user.")

    def print_divider(self):
        print('==========================================')

    def input_and_create_user(self):
        """
        Ask for new username and add it to the list of users.
        """
        print("Please input username!")
        new_username = input()
        new_user = user.User(new_username)
        self.users.append(new_user)

    def print_users(self):
        """
        Print all users in ordered list format.
        """
        i = 0
        for item in self.users:
            print("{}. {}".format(i, item.name))
            i = i + 1

    def select_a_user(self):
        """
        Print and select a user from already added users.
        :return: User object which is selected.
        """
        self.print_users()
        user_input = self.input_for_user()
        currently_selected = self.users[int(user_input)]
        return currently_selected

    def input_for_user(self):
        """
        Ask for input to select user from users' list.
        :return: Number of selection.
        """
        user_input = ""
        while user_input not in range(0, len(self.users)):
            print("Pick user from above, or type 'cancel'")
            user_input = input()
            if user_input == "cancel":
                raise ValueError
            user_input = int(user_input)
        return user_input

    def select_user_and_add_transaction(self):
        """
        Select a user and add a custom amount of transaction.
        """
        def add_transaction(to_user):
            print("Amount of transaction:")
            amount = input()
            new_transaction = transaction.Transaction(amount)
            to_user.add_transaction(new_transaction)

        try:
            selected_user = self.select_a_user()
            add_transaction(selected_user)
        except ValueError:
            print("No changes made.")

    def print_all_transaction(self, user):
        for item in user.transactions:
            transaction_time = datetime.datetime.fromtimestamp(item.timestamp)
            print("{} at {} [{}]".format(item.amount, transaction_time, item.uuid))

    def select_user_and_print_report(self):
        """
        Print report for an already added user.
        """
        try:
            selected_user = self.select_a_user()
            self.print_all_transaction(selected_user)
        except ValueError:
            print("No changes made.")

    def handle_inputs(self):
        """
        Accept inputs from the terminal, and try to execute corresponding action for it.
        :return:
        """
        user_input = ""
        while user_input != "exit":
            self.print_divider()
            user_input = input()
            self.do_action_for_input(user_input)

    def do_action_for_input(self, user_input):
        """
        Execute action for an input
        """
        if user_input == "help":
            self.print_help()
        elif user_input == "add user":
            self.input_and_create_user()
        elif user_input == "list users":
            self.print_users()
        elif user_input == "add transaction":
            self.select_user_and_add_transaction()
        elif user_input == "generate report":
            self.select_user_and_print_report()

