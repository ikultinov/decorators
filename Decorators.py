"""
Написать декоратор - логгер. Он записывает в файл дату и время вызова
функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
"""
import datetime


def outer(func):
    def inner(*args, **kwargs):
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.now()} - дата и время вызова функции:'
                    f' {func.__name__},\nс параметрами: {args}, {kwargs}\n'
                    f'функция вернула значение: {func(*args, **kwargs)}')
        return func(*args, **kwargs)

    return inner


@outer
def div(a, b):
    return a / b


if __name__ == '__main__':
    div(1, 2)
