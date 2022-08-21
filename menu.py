import logger_printer as lp


def Menu():
    lp.ClearScreen()
    print("_____________МЕНЮ______________")
    print("Выберите интересующий Вас пункт:")
    print("1. Вычисление вещественных чисел")
    print("2. Вычисление комплексных чисел")
    print("3. Просмотр логов")
    print("4. Выход из программы")
    button = input("Выберите пункт меню: ").replace(' ', '')
    if button == '1':
        lp.printer(f'Выбран пункт меню 1. Вычисление вещественных чисел.')
    elif button == '2':
        lp.printer(f'Выбран пункт меню 2. Вычисление комплексных чисел.')
    elif button == '3':
        lp.printer(f'Выбран пункт меню 3. Просмотр логов.')
    elif button == '4':
        lp.printer(f'Выбран пункт меню 4. Выход из программы.')
    else:
        lp.printer(f'Введен пункт {button}.')
    try:
        button = int(button)
    except:
        lp.printer("НЕПРАВИЛЬНЫЙ ВВОД! Необходимо ввести целое число от 1 до 4. Попробуйте ещё раз.")
        lp.Pause()
    return button