import clp

# This is the main function file. Handle command line prompts as well as executing user actions: creating users, listing users, creating transactions and so on.
# Call this file to start the execution engine.

"""
Developed by Balazs Reho

Work-Log:

2017-07-10:     Start initial working

2017-07-11:     Some refactoring in clp.py after random meeting notes.

"""

# ============ MAIN FUNCTION ============
if __name__ == '__main__':
    clp.CommandLineProgram.for_terminal().name_bank("RapidLab").run()
# ============ END OF MAIN ==============