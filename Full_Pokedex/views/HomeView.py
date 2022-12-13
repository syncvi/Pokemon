import tkinter as tk
from tkinter import ttk
from views.View import View
import customtkinter as ctk
from PIL import ImageTk, Image
from extras.pokemon_battle import initialize_battle


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""

# ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class HomeView(ctk.CTkToplevel, View):  # change to CTkTopLevel when using "choiceView"
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10
    BTN_CAPTION = [
        "Battle",
        "Pokedex",
        "Settings",
        "Exit"
    ]
    settingsToggle = False

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.title("Pokemon!")
        self.homeController = controller
        self.iconbitmap("assets/poke.ico")
        self.geometry("700x500")
        self.bind('<Control-q>', self._quit_event)
        self.bind('<s>', self._settings_show_event)
        self.bind('<Control-s>', self._settings_hide_event)
        self.bind('<b>', self._battle_event)
        self._make_mainImage()
        self._make_mainFrame()
        # self._make_title()
        self._make_options()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    def _battle_event(self, event):
        initialize_battle()

    def _settings_show_event(self, event):
        self.pack_settings()

    def _settings_hide_event(self, event):
        self.makeInvisible()

    def _quit_event(self, event):
        # print("XD "), repr(event.char)
        self.destroy()

    def _make_mainImage(self):
        self.mainImage = Image.open("assets/logo.png")
        self.newSize = self.mainImage.resize((500, 200))
        self.logo_image = ctk.CTkLabel(self, text='')
        self.img = ImageTk.PhotoImage(self.newSize)

        self.logo_image.configure(image=self.img)
        self.logo_image.image = self.img
        self.logo_image.pack(padx=self.PAD, pady=self.PAD)

    """
        Creates view's frame.
    """

    def _make_mainFrame(self):
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """

    def _make_title(self):
        title = ctk.CTkLabel(
            self.mainFrame, text="Pokemon!", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    """
        Creates view's options.
    """

    def _make_options(self):

        self.frame_btn = ctk.CTkFrame(self.mainFrame)
        self.frame_btn.pack(padx=self.PAD, pady=self.PAD)

        for caption in self.BTN_CAPTION:
            if caption == "Exit":
                btn = ctk.CTkButton(self.frame_btn, text=caption,
                                    command=self.destroy)

            elif caption == "Battle":
                btn = ctk.CTkButton(self.frame_btn, text=caption,
                                    command=initialize_battle)

            elif caption == "Settings":
                btn = ctk.CTkButton(self.frame_btn, text=caption,
                                    command=lambda: [self.changeToggleState(), self.pack_settings()])
            else:
                btn = ctk.CTkButton(
                    self.frame_btn, text=caption, command=lambda txt=caption: self.homeController.btnClicked(txt))

            btn.pack(padx=self.PAD, pady=self.PAD)

    def pack_settings(self):
        self.geometry("700x700")
        self.appearance_mode_label = ctk.CTkLabel(
            self.frame_btn, text="Appearance Mode:", anchor="w")

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_btn, values=["Dark",  "Light", "System"],
                                                             command=self.homeController.change_appearance_mode_event)

        self.scaling_label = ctk.CTkLabel(
            self.frame_btn, text="UI Scaling:", anchor="w")

        self.scaling_optionemenu = ctk.CTkOptionMenu(self.frame_btn, values=["100%", "80%", "90%",  "110%", "120%"],
                                                     command=self.homeController.change_scaling_event)

        self.hide_btn = ctk.CTkButton(self.frame_btn, text='Hide',
                                      command=self.makeInvisible)

        self.appearance_mode_label.pack(padx=self.PAD, pady=self.PAD)
        self.appearance_mode_optionemenu.pack(padx=self.PAD, pady=self.PAD)
        self.scaling_label.pack(padx=self.PAD, pady=self.PAD)
        self.scaling_optionemenu.pack(padx=self.PAD, pady=self.PAD)
        self.hide_btn.pack(padx=self.PAD, pady=self.PAD)

    def changeToggleState(self):

        self.settingsToggle = not self.settingsToggle
        print('Call from toggleState: ' + str(self.settingsToggle))

    def makeInvisible(self):
        self.geometry("700x500")
        self.appearance_mode_label.pack_forget()
        self.appearance_mode_optionemenu.pack_forget()
        self.scaling_label.pack_forget()
        self.scaling_optionemenu.pack_forget()
        self.hide_btn.pack_forget()

        # -------------------------------------
    """
    @Overrite
    """

    def main(self):

        self.mainloop()

    """
    @Overrite
    """

    def close(self):
        return
