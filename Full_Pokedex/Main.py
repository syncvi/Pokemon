# -*- encoding:utf-8 -*-
from core.Core import Core
from extras.splash_screen_gui import *


"""
    Main class. Responsible for running the application.
"""


class Main:
    @staticmethod
    def run():
        try:
            loading_screen()
            app = Core.openController("choice")
            app.main()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
