from tkinter import messagebox
from tkinter.constants import END
from core.Controller import Controller
from core.Core import Core
import os


"""
    Responsible for AddView behavior.
"""


class ChoiceController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.choiceView = self.loadView("choice")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------

    def launch_graphical(self):
        app = Core.openController("home")
        app.main()

    def launch_terminal(self):

        os.system("start /B start cmd.exe @cmd /k python TerminalPokedex/main.py")
        # os.system("python TerminalPokedex/main.py")
        # print('Terminal')

    def main(self):
        self.choiceView.main()
