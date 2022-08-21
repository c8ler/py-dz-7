import numpy
import logger_printer as lp


def Complex_Input(num):
    lp.DrawLine()
    comp_para = []
    for i in range(0, num):
        temp = (input(f'Введите компл. число {i+1}: ').replace(' ', ''))
        lp.printer(f'Введено компл. число {i+1} = {temp}.')
        try:
            complex_test = complex(temp)
            comp_para.append(complex_test)
        except:
            lp.DrawLine()
            lp.printer("НЕПРАВИЛЬНЫЙ ВВОД! Необходимо ввести комплексное число вида a+bj.")
            lp.Pause()
            break
    return comp_para


def Complex_Calc():
    list_of_complex = Complex_Input(2)
    com_oper = input('Введите операцию: ').replace(' ', '')
    lp.printer(f'Введена операция "{com_oper}".')
    if com_oper == '+':
        lp.ResultOf()
        lp.printer(numpy.around(list_of_complex[0] + list_of_complex[1], 5))
        lp.Pause()
    elif com_oper == '*':
        lp.ResultOf()
        lp.printer(numpy.around(list_of_complex[0] * list_of_complex[1], 5))
        lp.Pause()
    elif com_oper == '-':
        lp.ResultOf()
        lp.printer(numpy.around(list_of_complex[0] - list_of_complex[1], 5))
        lp.Pause()
    elif com_oper == '/':
        lp.ResultOf()
        lp.printer(numpy.around(list_of_complex[0] / list_of_complex[1], 5))
        lp.Pause()
    else:
        lp.printer('НЕПРАВИЛЬНЫЙ ВВОД! Допустимы операции "+", "-", "*", "/"')
        lp.Pause()