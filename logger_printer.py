from datetime import datetime
from getch import pause
import os


def Pause():
    pause('Нажмите любую клавишу, чтобы продолжить.')


def printer(printing):
    log_file = open("log.txt", "a")
    print(str(printing))
    now = datetime.now()
    log_file.write(now.strftime("%Y-%m-%d %H:%M:%S") +
                   ' ' + str(printing) + '\n')
    log_file.close()
    return printer


def LogOutput():
    ClearScreen()
    with open("log.txt", "r") as f:
        for line in f:
            print(f'{line}', end='')
    Pause()


def ClearScreen():
    os.system('clear')


def DrawLine():
    printer("________________________________")


def ResultOf():
    DrawLine()
    printer("Результат вычисления: ")


def UnderConstruction():
    DrawLine()
    printer("Работа над программой ещё ведётся, извините.")


def Hello():
    printer("Вас приветсвует калькулятор!")