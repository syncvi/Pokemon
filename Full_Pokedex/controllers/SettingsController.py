from tkinter import messagebox
from tkinter.constants import END
from core.Controller import Controller


"""
    Responsible for AddView behavior.
"""


class SettingsController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.settingsView = self.loadView("settings")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------

    def main(self):
        self.settingsView.main()
