# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core
import customtkinter


"""
    Main controller. It will be responsible for program's main screen behavior.
"""


class HomeController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """

    def btnClicked(self, caption):
        if caption == "Pokedex":
            c = Core.openController("pokedex")
            c.main()
        elif caption == "Settings":
            c = Core.openController("settings")
            c.main()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    """
        @Override
    """

    def main(self):
        self.homeView.main()
