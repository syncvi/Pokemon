import curses
from dexin import *
import time
import culour
from activity_submenu import *
from pynput.keyboard import Key, Controller


INFO_WINDOW_WIDTH = 20
INFO_WINDOW_HEIGHT = 5
RAPORT_WINDOW_WIDTH = 32
RAPORT_WINDOW_HEIGHT = 5
SCREEN_HEIGHT = 30
SCREEN_WIDTH = 120
stdscr = curses.initscr()
keyboard = Controller()


def init_colors():
    curses.init_pair(89, curses.COLOR_BLACK, 14)  # cr
    curses.init_pair(90, curses.COLOR_BLACK, 49)  # trq
    curses.init_pair(91, curses.COLOR_GREEN, 13)  # pnk
    curses.init_pair(92, 14, curses.COLOR_BLACK)  # cr
    curses.init_pair(93, 49, curses.COLOR_BLACK)
    curses.init_pair(94, 209, curses.COLOR_BLACK)  # orange
    curses.init_pair(95, 178, curses.COLOR_BLACK)  # dirty yellow
    curses.init_pair(96, 206, curses.COLOR_BLACK)  # pink
    curses.init_pair(97, 191, curses.COLOR_BLACK)  # brownish
    curses.init_pair(100, curses.COLOR_BLACK, curses.COLOR_WHITE)


def pokeball_animation(stdscr):
    pad = curses.newpad(500, 500)
    text2 = "Congrats! You've completed the tutorial!"
    screen_height, screen_width = stdscr.getmaxyx()
    pokeball = getPokeball()
    for idx, line in enumerate(pokeball.splitlines()):
        # self.pad.attron(curses.color_pair(6))
        pad.addstr(idx+3, ((screen_width //
                   2) - 4) - len(line)//2, line, curses.A_BOLD)
        # self.pad.attroff(curses.color_pair(6))

        # culour.addstr(self.pad, idx, self.screen_width //
        #               2 - len(line)//2, line)

    for k in range(3):

        for i in range(1):
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, 0, i, 0, 20+i, 110)
            time.sleep(0.7)

        for i in range(1):
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, 0, 2-i, 0, 22-i, 110)
            time.sleep(0.7)
    draw_popup_window(text2)
    time.sleep(2)
    # stdscr.clear()


# def run_escape(stdscr):
#     stdscr.clear()
#     the_string = "Hello world!"
#     for char in the_string:
#         stdscr.addstr(char)
#         stdscr.refresh()
#         time.sleep(0.1)
#     stdscr.getch()


def draw_battle_raport_window():

    window = curses.newwin(RAPORT_WINDOW_HEIGHT, RAPORT_WINDOW_WIDTH, SCREEN_HEIGHT-8,
                           SCREEN_WIDTH-60)

    window.border()
    i = 0
    j = 0
    raport_info = "Opposing Venosaur taunts you!"
    raport_q = "Whatcha gonna do?!"
    for char in raport_info:
        i = i+1
        window.addstr(1, i, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    for char in raport_q:
        j = j+1
        window.addstr(3, j, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    window.refresh()
    # window.getch()


def draw_oponent_window(attack=False):

    window = curses.newwin(INFO_WINDOW_HEIGHT, INFO_WINDOW_WIDTH+10, SCREEN_HEIGHT-28,
                           SCREEN_WIDTH-115)

    window.border()

    bio = "Venosaur Lv.73"
    hp = "Health: "
    bars = "================"

    window.addstr(1, 2, hp, curses.color_pair(92))
    window.addstr(1, 2+len(hp), bars, curses.color_pair(92))
    window.addstr(3, 2, bio, curses.color_pair(93))

    if attack == True:
        i = 0
        for char in bars:
            window.addstr(1, (len(hp+bars)+1)-i, " ", curses.color_pair(92))
            window.refresh()
            i += 1
            time.sleep(0.09)

    window.refresh()


def draw_Chari_pad(stdscr):
    pad = curses.newpad(150, 150)

    pokemonImg = getPokemonFlipped(6)
    for idx, line in enumerate(pokemonImg.splitlines()):
        pad.addstr(idx, 2, line, curses.color_pair(94))
    # pad.addstr(0, 0, "Pokemon 1")

    stdscr.refresh()
    for i in range(2):
        pad.refresh(i, i+2, 10, i, 29, 119)
    # for j in range(7):
    #     pad.refresh(10, j, 22, 20, 29, 119)


def draw_Veno_pad(stdscr):
    pad = curses.newpad(150, 150)
    pokemonImg = getPokemon(3)
    for idx, line in enumerate(pokemonImg.splitlines()):
        if idx > 9:
            pad.addstr(idx, 2, line, curses.color_pair(93))
        # elif idx in (10, 11):
        #     pad.addstr(idx, 2, line, curses.color_pair(97))
        else:
            pad.addstr(idx, 2, line, curses.color_pair(96))
    #pad.addstr(0, 0, "Pokemon 2")

    stdscr.refresh()
    for i in range(7):
        pad.refresh(i, 0, 0, 60, 29, 119)


def percentage(color_pair=90, isRealistic=False):
    win = curses.newwin(3, 32, SCREEN_HEIGHT//2, SCREEN_WIDTH//2-16)
    win1 = curses.newwin(3, 32, SCREEN_HEIGHT//2+3, SCREEN_WIDTH//2-20)

    win.border(0)
    loading = 0
    win1.addstr(1, 16, "Loading...")
    win1.refresh()
    while loading < 100:
        if loading == 65 and isRealistic == True:
            time.sleep(2)
        elif loading in (75, 80) and isRealistic == True:
            time.sleep(0.3)
        elif loading == 85 and isRealistic == True:
            time.sleep(0.5)
        loading += 1
        time.sleep(0.01)
        update_progress(win, loading, color_pair)


def update_progress(win, progress, color_pair=90):

    rangex = (30 / float(100)) * progress
    pos = int(rangex)
    display = ' '
    if pos != 0:
        win.addstr(1, pos, "{}".format(display), curses.color_pair(color_pair))
        win.refresh()


def draw_popup_window(text, flash=False):
    # text = "A wild pokemon appears!"
    win = curses.newwin(2, 45, SCREEN_HEIGHT//2, SCREEN_WIDTH//2-len(text)//2)

    i = 0
    for char in text:
        i = i+1
        win.addstr(1, i, char, curses.color_pair(100))
        win.refresh()
        time.sleep(0.09)

    if flash == True:
        for j in range(4):
            curses.flash()
            win.refresh()
            time.sleep(0.09)


def attack_command():
    window = curses.newwin(RAPORT_WINDOW_HEIGHT, RAPORT_WINDOW_WIDTH, SCREEN_HEIGHT-8,
                           SCREEN_WIDTH-60)
    #newscr = curses.initscr()
    attack = True

    i = 0
    j = 0
    k = 0
    h = 0
    g = 0
    window.clear()
    window.border()
    raport_ven = "Venosaur used Razor Leaf!"
    for char in raport_ven:
        h = h+1
        window.addstr(1, h, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    time.sleep(0.5)
    window.clear()
    window.border()
    raport_ven1 = "It misses!"
    for char in raport_ven1:
        g = g+1
        window.addstr(1, g, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    g = 0
    time.sleep(0.1)
    window.clear()
    window.border()
    raport_ven2 = "That wasn't very effective..."
    for char in raport_ven2:
        g = g+1
        window.addstr(1, g, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    time.sleep(1)
    window.clear()
    window.border()
    raport_info = "Charizard used Inferno!"
    for char in raport_info:
        i = i+1
        window.addstr(1, i, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    time.sleep(1)
    window.clear()
    window.border()
    raport_q = "It was super effective!"
    for char in raport_q:
        j = j+1
        window.addstr(1, j, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    window.refresh()

    draw_oponent_window(attack)

    time.sleep(1)
    window.clear()
    window.border()
    raport_f = "Enemy Venosaur fainted!"
    for char in raport_f:
        k = k+1
        window.addstr(1, k, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    k = 0
    time.sleep(1)
    window.clear()
    window.border()
    raport_f = "Charizard gained 8215xp."
    for char in raport_f:
        k = k+1
        window.addstr(1, k, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)
    k = 0
    time.sleep(1)
    window.clear()
    window.border()
    raport_f = "You won!"
    for char in raport_f:
        k = k+1
        window.addstr(1, k, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    time.sleep(2)
    stdscr.clear()
    stdscr.refresh()
    pokeball_animation(stdscr)
    stdscr.clear()
    stdscr.refresh()
    percentage(89, False)
    stdscr.clear()
    stdscr.refresh()
    keyboard.press('q')
    keyboard.release('q')

    # curses.nocbreak()
    # stdscr.keypad(False)
    # curses.echo()
    # curses.endwin()


def run_escape():
    window = curses.newwin(RAPORT_WINDOW_HEIGHT, RAPORT_WINDOW_WIDTH, SCREEN_HEIGHT-8,
                           SCREEN_WIDTH-60)
    window.border()
    i = 0
    raport_info = "You've managed to escape!"
    for char in raport_info:
        i = i+1
        window.addstr(1, i, char, curses.color_pair(100))
        window.refresh()
        time.sleep(0.09)

    time.sleep(1)


def display_battle():
    #stdscr = curses.initscr()
    curses.curs_set(0)
    init_colors()
    text1 = "A wild pokemon appears!"

    submenu_items = [("PILL", curses.beep),
                     ("TMs", curses.flash)]
    submenu = Activity(submenu_items, stdscr)

    main_menu_items = [
        ("ATK", attack_command),
        ("POK", curses.flash),
        ("BAG", submenu.display),
    ]
    main_menu = Activity(main_menu_items, stdscr)

    # --------------------------
    percentage(90, True)
    time.sleep(0.5)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(0.5)
    draw_popup_window(text1, True)
    stdscr.clear()
    # --------------------------comment this shit for debug
    draw_Chari_pad(stdscr)
    draw_Veno_pad(stdscr)
    time.sleep(0.5)
    draw_oponent_window()
    time.sleep(0.5)
    draw_battle_raport_window()
    # --------------------------comment this shit for debug
    # stdscr.refresh()
    main_menu.display()
    # run_escape()

    # stdscr.refresh()

    stdscr.clear()
    stdscr.refresh()

    # stdscr.getch()
    # draw_battle_raport_window()
    # stdscr.refresh()
    # stdscr.clear()
    # stdscr.refresh()

    # stdscr.getch()
