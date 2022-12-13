import curses
from dexin import *
import time
from submenu_class import *
from battles import *


class MenuDisplay:

    def __init__(self, menu):
        # set menu parameter as class property
        self.menu = menu

        # run curses application
        curses.wrapper(self.mainloop)

    # --------------------------------------------------------------------------------------------------------------------

    def mainloop(self, stdscr):

        # turn off cursor blinking
        curses.curs_set(0)
        curses.start_color()

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
        curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_YELLOW)

        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

        # set screen object as class property
        self.stdscr = stdscr
        self.submenu = Menu(submenu_items, self.stdscr)

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        # curses.resize_term(self.screen_height-1, self.screen_width-1)
        # set pad object to display ascii
        self.pad = curses.newpad(100, 100)
        self.ascii_pad = curses.newpad(
            500, 500)
        self.bio_win = curses.newwin(20, 5, 2, 2)
        # self.pad.scrollok(True)
        #pad_position = 0
        # def mypad_refresh(): return self.pad.refresh(
        #   pad_position+2, 0, 0, 0, self.screen_height-1, self.screen_width)

        # specify the current selected row
        current_row = 0
        # current_subrow = 0

        # animating logo
        self.logo_animation()

        # print the menu
        self.print_menu(current_row)

        while 1:
            user_input = self.stdscr.getch()

            if user_input == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif user_input == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif user_input == curses.KEY_ENTER or user_input in [10, 13] and current_row == 0:
                self.stdscr.clear()
                self.stdscr.refresh()
                display_battle()

            elif user_input == curses.KEY_ENTER or user_input in [10, 13] and current_row == 1:

                self.stdscr.clear()
                pokemonID = self.pokedex_menu()
                self.stdscr.clear()

                pokemonImg = getPokemon(pokemonID)
                for idx, line in enumerate(pokemonImg.splitlines()):
                    self.ascii_pad.addstr(idx, 2, line, curses.A_BOLD)
                    # self.stdscr.addstr(idx, 2, line)
                    # is displaying something!
                    #culour.addstr(self.stdscr, idx, 2, line)
                self.stdscr.refresh()
                # for i in range(1):
                self.ascii_pad.refresh(
                    0, 0, 0, 0, 29, 119)
                # self.stdscr.refresh()

                info = getPokemonInfo(pokemonID)
                bio = getPokemonBio(pokemonID)
                # self.stdscr.addstr(0, 0, info)
                if "water" in info:
                    self.color_print(0, 0, info, 2)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 2)
                elif "fire" in info:
                    self.color_print(0, 0, info, 3)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 3)
                elif "grass" in info:
                    self.color_print(0, 0, info, 4)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 4)
                elif "electric" in info:
                    self.color_print(0, 0, info, 7)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 7)
                elif "normal" in info:
                    self.color_print(0, 0, info, 1)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 1)
                elif "bug" or "psychic" in info:
                    self.color_print(0, 0, info, 5)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 5)
                else:
                    self.color_print(0, 0, info, 1)
                    for idx, line in enumerate(bio.splitlines()):
                        self.color_print(idx, 70, line, 1)

                self.stdscr.refresh()

                # self.print_center()
                self.stdscr.getch()

            elif user_input == curses.KEY_ENTER or user_input in [10, 13] and current_row == 2:
                self.submenu.display()

                # if user selected last row (Exit), confirm before exit the program
            elif user_input == curses.KEY_ENTER or user_input in [10, 13] and current_row == len(self.menu) - 1:
                if self.confirm("Are you sure you want to exit?"):
                    break

            self.print_menu(current_row)

    # --------------------------------------------------------------------------------------------------------------------
    def pokedex_menu(self):
        self.stdscr.clear()
        curses.curs_set(1)
        prompt_text = "Enter your pokemon's ID: "
        current_input = []
        x = self.screen_width // 2 - len(prompt_text) // 2
        y = self.screen_height // 2

        while True:
            self.stdscr.clear()
            self.stdscr.addstr(y, x, prompt_text)

            for char in current_input:
                self.stdscr.addstr(char)

            self.stdscr.refresh()
            input_key = self.stdscr.getkey()

            if ord(input_key) == 27:
                curses.curs_set(0)
                break
            if ord(input_key) == 10 or ord(input_key) == 13:
                # try:
                curses.curs_set(0)
                self.stdscr.clear()
                s = [str(i) for i in current_input]
                res = int("".join(s))
                return res
                # except ValueError:
                #     self.stdscr.clear()
                #     self.stdscr.addstr("ID is a number, not a word, dumbass.")
                #     self.stdscr.refresh()
                #     break
            if input_key in ("KEY_BACKSPACE", '\b', "\x7f"):
                if len(current_input) > 0:
                    current_input.pop()
            else:
                current_input.append(input_key)

        curses.curs_set(0)

    # --------------------------------------------------------------------------------------------------------------------

    def logo_animation(self):
        logo = getLogo()
        for idx, line in enumerate(logo.splitlines()):
            # self.pad.attron(curses.color_pair(6))
            self.pad.addstr(idx, self.screen_width //
                            2 - len(line)//2, line, curses.A_BOLD)
            # self.pad.attroff(curses.color_pair(6))

            # culour.addstr(self.pad, idx, self.screen_width //
            #               2 - len(line)//2, line)

        for k in range(3):

            for i in range(1):
                self.stdscr.clear()
                self.stdscr.refresh()
                self.pad.refresh(0, 0, i, 0, 20+i, 110)
                time.sleep(0.7)

            for i in range(1):
                self.stdscr.clear()
                self.stdscr.refresh()
                self.pad.refresh(0, 0, 2-i, 0, 22-i, 110)
                time.sleep(0.7)

        self.stdscr.clear()
    # --------------------------------------------------------------------------------------------------------------------

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        s = str(self.screen_height) + " " + str(self.screen_width)
        self.stdscr.addstr(0, 0, s)
        self.color_print(29, 0, "Epilepsy warning!", 1)
        logo = getLogo()
        for idx, line in enumerate(logo.splitlines()):
            # self.stdscr.attron(curses.color_pair(6))
            self.stdscr.addstr(idx, self.screen_width //
                               2 - len(line)//2, line)
            # self.stdscr.attroff(curses.color_pair(6))
        # writeShit(logo)
        # text = "POKEMON LOGO"
        # self.stdscr.addstr(8, self.screen_width//2 - len(text)//2, text)
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 + 10 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    # --------------------------------------------------------------------------------------------------------------------

    # def print_submenu(self, selected_row_idx):
    #     self.stdscr.clear()
    #     for idx, row in enumerate(self.submenu):
    #         x = self.screen_width // 2 - len(row) // 2
    #         y = self.screen_height // 2 + 10 - len(submenu) // 2 + idx
    #         if idx == selected_row_idx:
    #             self.color_print(y, x, row, 1)
    #         else:
    #             self.stdscr.addstr(y, x, row)
    #     self.stdscr.refresh()

    # --------------------------------------------------------------------------------------------------------------------

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    # --------------------------------------------------------------------------------------------------------------------

    def print_confirm(self, selected="Yes"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "Yes"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "No"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    # --------------------------------------------------------------------------------------------------------------------

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "Yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "Yes":
                current_option = "No"
            elif key == curses.KEY_LEFT and current_option == "No":
                current_option = "Yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "Yes" else False

            self.print_confirm(current_option)

    # --------------------------------------------------------------------------------------------------------------------

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()


if __name__ == "__main__":
    menu = ['Battle', 'View Pokedex', 'Settings', 'Exit']
    submenu_items = [('Audio and HRTF',  curses.beep),
                     ('Graphics and Video', curses.flash)]

    MenuDisplay(menu)
