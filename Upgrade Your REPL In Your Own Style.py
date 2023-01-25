import sys
import os
import time


def menu(m=0):
    os.system('cls')
    clock = '🕒' + time.strftime("%H:%M:%S",
                                time.localtime())
    clock_color = f'\033[4;{31+m};{47+m}m{clock}\033[0;0m'
    print(f' 🅿🆈🆃🅷🅾🅽 🐍\n{clock_color}\n')


menu()
print('Choose a mode: \n')
m = input('👉 1. Blue \n👉 2. Green \n👉 ')


if m == "1":
    menu(-1)
    sys.ps1 = '\033[7;30;46m ▶▶▶\033[0;0m '
    sys.ps2 = '\033[7;30;46m ...\033[0;0m \033[0;3m '
else:
    menu(1)
    sys.ps1 = '\033[7;32;48m ▶▶▶ \033[0;0m '
    sys.ps2 = '\033[4;32;55m ... \033[0;0m \033[0;3m '
