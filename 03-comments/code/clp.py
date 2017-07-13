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
users = []

class CommandLineProgram:
    """
    Command Line Program which handles actions, inputs and reports through terminal.
    """
    class ACTION:
        EXIT = "exit"; HELP = "help"; ADD_USER = "add user"; LIST_USERS = "list users"; ADD_TRANSACTION = "add transaction"; GENERATE_REPORT = "generate report"
    @staticmethod
    def for_terminal():
        """
        Create a terminal based command line interface.
        :return: CommandLineProgram object.
        """
        return CommandLineProgram().disable_gui()
    def __init__(self):
        self.gui = True
        self.bank_name = "Example Bank"


    def disable_gui(self):
        self.gui = False
        return self

    def name_bank(self, new_bank_name: str):
        """
        Set the name of the bank.
        """
        if self.is_bank_name_valid(new_bank_name):
            self.bank_name = new_bank_name
        else:
            raise ValueError("Bank name is not valid!")
        return self

    def is_bank_name_valid(self, name_to_check: str):
        """
        Check if a new bank name is valid.
        """
        return True if (not len(name_to_check) > 12) and (name_to_check.isalpha()) else False

    def run(self):
        """
        Run main loop and handle user inputs.
        """
        self.print_welcome()
        self.handle_inputs()

    def print_welcome(self):
        print("Welcome to {}!\nLogin at: {}\nType 'help' for manual, 'exit' to terminate the program.".format(self.bank_name, datetime.datetime.now()))
    def print_help(self):
        print("'help': This command.\n'exit': Close all session and terminate.\n'add user': Add a new user to the session.\n'list users': List all users.\n'add transaction': Add transaction to an existing user.'generate report': Print report for an existing user.")
    def print_divider(self):
        print('==========================================')

    def input_and_create_user(self):
        """
        Ask for new username and add it to the list of users.
        """
        print("Please input username!")
        users.append(user.User(input()))

    def print_users(self):
        """
        Print all users in ordered list format.
        """
        i = 0
        for item in users:
            print("{}. {}".format(i, item.name))
            i = i + 1

    def prompt_user_selection(self):
        """
        Print and select a user from already added users.
        :return: User object which is selected.
        """
        self.print_users()
        user_input = self.input_for_user_selection()
        currently_selected = users[int(user_input)]
        return currently_selected

    def input_for_user_selection(self):
        """
        Ask for input to select user from users' list.
        :return: Number of selection.
        """
        user_input = ""
        while user_input not in range(0, len(users)):
            print("Pick user from above, or type 'cancel'")
            user_input = input()
            if user_input == "cancel":
                raise ValueError
            user_input = int(user_input)
        return user_input

    def select_user_and_add_transaction(self):
        """
        Select a user and add a transaction with custom amount.
        """
        self.prompt_user_selection().add_transaction(transaction.Transaction(input("Amount of transaction:")))

    def print_all_transaction(self, selected_user):
        for item in selected_user.transactions:
            print("{} at {} [{}]".format(item.amount, datetime.datetime.fromtimestamp(item.timestamp), item.uuid))

    def select_user_and_print_report(self):
        """
        Print report for an already added user.
        """
        self.print_all_transaction(self.prompt_user_selection())

    def handle_inputs(self):
        """
        Accept inputs from the terminal, and try to execute corresponding action for it.
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
        try:
            if user_input == CommandLineProgram.ACTION.HELP:
                self.print_help()
            elif user_input == CommandLineProgram.ACTION.ADD_USER:
                self.input_and_create_user()
            elif user_input == CommandLineProgram.ACTION.LIST_USERS:
                self.print_users()
            elif user_input == CommandLineProgram.ACTION.ADD_TRANSACTION:
                self.select_user_and_add_transaction()
            elif user_input == CommandLineProgram.ACTION.GENERATE_REPORT:
                self.select_user_and_print_report()
        except Exception:
            print("Try again")