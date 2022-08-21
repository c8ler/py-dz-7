import menu as mn
import real_numbers as rn
import complex_numbers as cp
import logger_printer as lp


def Main_Calc():
    lp.Hello()
    while True:
        start_program = mn.Menu()
        if start_program == 1:
            rn.Real_Calc()
        elif start_program == 2:
            cp.Complex_Calc()
        elif start_program == 3:
            lp.LogOutput()
        elif start_program == 4:
            lp.DrawLine()
            lp.printer('До новых встреч!')
            quit()
        else:
            lp.DrawLine()
            lp.printer('НЕПРАВИЛЬНЫЙ ВВОД! Попробуйте ещё раз.')
            lp.Pause()


Main_Calc()
