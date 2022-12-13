import tkinter as tk
from tkinter import ttk
from views.View import View
import customtkinter as ctk


"""
    View responsible for adding new customers.
"""


class SettingsView(ctk.CTk, View):
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.settingsController = controller
        self.iconbitmap("assets/poke.ico")
        self.geometry("200x200")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    def _make_mainFrame(self):
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_title(self):
        title = ctk.CTkLabel(
            self.mainFrame, text="Settings", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    def main(self):
        self._make_mainFrame()
        self._make_title()

        self.mainloop()

    """
    @Overrite
    """

    def close(self):
        self.destroy()
