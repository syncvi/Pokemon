import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
import customtkinter as ctk
# from pokemon_battle import initialize_battle
from views.View import View
import random


"""
    View responsible for adding new customers.
"""
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class PokedexView(ctk.CTkToplevel, View):
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
        self.pokedexController = controller
        self.title('Pokedex')
        self.iconbitmap("assets/poke.ico")
        self.geometry("600x600")
        self.configure(padx=10, pady=10)

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------

    def _make_main_label(self):
        title_label = ctk.CTkLabel(self, text='Pokedex', text_color='white')
        title_label.configure(font=('Calamity Regular', 25))
        title_label.pack(padx=10, pady=10)

    def _make_pokemon_space(self):
        self.pokemon_image = ctk.CTkLabel(self, text='')
        # self.pokemon_image.configure(fg_color='#272727')

        self.pokemon_identification = ctk.CTkLabel(
            self, text_color='white', text='')
        self.pokemon_identification.configure(font=('Calibri', 12))

        self.pokemon_types = ctk.CTkLabel(self, text_color='white', text='')
        self.pokemon_types.configure(font=('Calibri', 12))

        self.label_id_name = ctk.CTkLabel(
            self, text='Enter ID or Name', text_color='white')
        self.label_id_name.configure(font=('Calibri', 12))

        self.text_id_name = ctk.CTkTextbox(
            self, height=1, text_color='white', border_width=4)
        self.text_id_name.configure(font=('Calibri', 12))

        self.btn_load = ctk.CTkButton(
            self, text='Load Pokemon', command=self.pokedexController.pokemon_button, text_color='white')
        self.btn_load.configure(font=('Arial', 12))
        self.btn_load1 = ctk.CTkButton(
            self, text='Battle Test', text_color='white')
        self.btn_load1.configure(font=('Arial', 12))

        self.pokemon_image.pack(padx=10, pady=10)
        self.pokemon_identification.pack(padx=10, pady=10)
        self.pokemon_types.pack(padx=10, pady=10)
        self.label_id_name.pack(padx=10, pady=10)
        self.text_id_name.pack(padx=10, pady=10)
        self.btn_load.pack(padx=10, pady=10)
        self.btn_load1.pack(padx=10, pady=10)

    def make_bar(self, destroy=False):
        self.slider_progressbar_frame = ctk.CTkFrame(
            self, fg_color="transparent")

        self.progressbar_1 = ctk.CTkProgressBar(
            self.slider_progressbar_frame)

        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

        self.slider_progressbar_frame.pack(padx=10, pady=10)
        self.progressbar_1.pack(padx=10, pady=10)

        for i in range(100+random.randint(10,50)):

            self.update()
            time.sleep(0.01)
            self.update_idletasks()

        if destroy == True:
            self.slider_progressbar_frame.pack_forget()
            self.progressbar_1.pack_forget()

    """
    @Overrite
    """

    def main(self):

        self._make_main_label()
        self._make_pokemon_space()
        self.mainloop()

    """
    @Overrite
    """

    def close(self):
        self.destroy()
