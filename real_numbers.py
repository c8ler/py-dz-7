import logger_printer as lp


def Real_Input(num):
    lp.DrawLine()
    real_para = []
    for i in range(0, num):
        temp = (input(f'Введите вещ. число {i+1}: ').replace(' ', ''))
        lp.printer(f'Введено вещ. число {i+1} = {temp}')
        try:
            real_test = float(temp)
            real_para.append(real_test)
        except:
            lp.DrawLine()
            lp.printer("НЕПРАВИЛЬНЫЙ ВВОД! Необходимо ввести вещественное число вида 1.234.")
            lp.Pause()
            break
    return real_para


def Real_Calc():
    list_of_real = Real_Input(2)
    real_oper = input('Введите операцию: ').replace(' ', '')
    lp.printer(f'Введена операция "{real_oper}".')
    if real_oper == '+':
        lp.ResultOf()
        lp.printer(round(list_of_real[0] + list_of_real[1], 5))
        lp.Pause()
    elif real_oper == '*':
        lp.ResultOf()
        lp.printer(round(list_of_real[0] * list_of_real[1], 5))
        lp.Pause()
    elif real_oper == '-':
        lp.ResultOf()
        lp.printer(round(list_of_real[0] - list_of_real[1], 5))
        lp.Pause()
    elif real_oper == '/':
        lp.ResultOf()
        lp.printer(round(list_of_real[0] / list_of_real[1], 5))
        lp.Pause()
    else:
        lp.printer('НЕПРАВИЛЬНЫЙ ВВОД! Допустимы операции "+", "-", "*", "/"')
        lp.Pause()