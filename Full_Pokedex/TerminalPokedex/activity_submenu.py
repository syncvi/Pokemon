import curses
from curses import panel
import time


class Activity(object):
    def __init__(self, items, stdscr):
        self.window = stdscr.subwin(22, 100)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()

        panel.update_panels()
        self.screen_height, self.screen_width = self.window.getmaxyx()
        self.position = 0
        self.items = items
        self.items.append(("RUN", "RUN"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()

        self.panel.show()
        self.window.clear()
        self.window.border()

        while True:
            self.window.refresh()
            curses.doupdate()

            y = int(self.screen_height//4+1)  # 1.5-1
            x = int(self.screen_width//4)  # 1.3
            c = int(self.screen_width//1.2)
            i = 0
            j = 0

            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                if index == 2:
                    i = 0
                    j = 8

                msg = "%s%s" % ("", item[0])
                self.window.addstr(
                    y+i, x-len(msg)//2 + j, msg, mode)
                x = x + len(msg)//2
                i += 2
                j -= 1

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    window = curses.newwin(5, 32, 30-8,
                                           120-60)
                    window.border()
                    i = 0
                    raport_info = "You've managed to escape!"
                    for char in raport_info:
                        i = i+1
                        window.addstr(1, i, char, curses.color_pair(100))
                        window.refresh()
                        time.sleep(0.09)

                    time.sleep(1)
                    break
                else:
                    self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

            elif key == ord('q'):
                break
            elif key == 27:
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
