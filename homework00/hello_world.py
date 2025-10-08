#!/usr/bin/env python3
"""
Модуль для демонстрации работы с текстовыми сообщениями.
"""


def get_message():
    """
    Возвращает стандартное приветственное сообщение.

    Returns:
        str: Строка с текстом приветствия
    """
    return "Hello World!"


def main():
    """
    Основная функция для запуска модуля.
    """
    message = get_message()
    print(message)


if __name__ == "__main__":
    main()
