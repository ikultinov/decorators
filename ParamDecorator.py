"""
Написать декоратор аналогичный Decorators.py, но с параметром – путь к логам.
"""
import datetime
import os


def second_outer(path):
    def outer(func):
        def inner(*args, **kwargs):
            if not os.path.isdir('logs'):
                os.mkdir('logs')
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now()} - дата и время вызова '
                        f'функции: {func.__name__},\n'
                        f'с параметрами: {args}, {kwargs}\n'
                        f'функция вернула значение: {func(*args, **kwargs)}')
            return func(*args, **kwargs)

        return inner

    return outer


@second_outer(path='logs/log_2.txt')
def div(a, b):
    return a / b


if __name__ == '__main__':
    div(1, 2)
