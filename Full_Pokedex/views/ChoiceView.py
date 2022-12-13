import tkinter as tk
from tkinter import ttk
from views.View import View
import customtkinter as ctk


class ChoiceView(ctk.CTk, View):
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10
    BTN_CAPTION = [
        'Graphical', 'Terminal', 'Exit'
    ]

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.title("Pokemon!")
        self.choiceController = controller
        self.iconbitmap("assets/poke.ico")
        self.bind('<Control-q>', self._quit_event)
        self.bind('<t>', self._launch_T_event)
        self.bind('<g>', self._launch_G_event)
        self._make_mainFrame()
        self._make_title()
        self._make_options()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Creates view's frame.
    """

    def _launch_T_event(self, event):
        self.choiceController.launch_terminal()

    def _launch_G_event(self, event):
        self.choiceController.launch_graphical()

    def _quit_event(self, event):
        # print("XD "), repr(event.char)
        self.destroy()

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
        frame_btn = ctk.CTkFrame(self.mainFrame)
        frame_btn.pack(fill='x')

        for caption in self.BTN_CAPTION:
            if caption == "Exit":
                btn = ctk.CTkButton(self.mainFrame, text=caption,
                                    command=self.destroy)
                btn.pack(side=ctk.BOTTOM, padx=self.PAD, pady=self.PAD)
            elif caption == "Graphical":
                btn = ctk.CTkButton(frame_btn, text=caption,
                                    command=self.choiceController.launch_graphical)
                btn.pack(side=ctk.RIGHT)
            elif caption == 'Terminal':
                btn = ctk.CTkButton(frame_btn, text=caption,
                                    command=self.choiceController.launch_terminal)
                btn.pack(side=ctk.LEFT)

            # btn.pack(fill="x")

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
