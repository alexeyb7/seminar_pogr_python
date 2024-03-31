# Проверка корректности даты
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
import logging


# Задание файла логирования , уровня логирования и переменной
logging.basicConfig(
    filename="info.log", filemode="a", encoding="utf-8", level=logging.INFO
)
logger = logging.getLogger(__name__)
# ввод даты для проверки
date_to_prove = "15.0l.2023"


# Введите ваше решение ниже
__all__ = ["is_valid_date", "_is_leap"]


def _is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def is_valid_date(date: str) -> bool:
    try:
        day, month, year = map(int, date.split("."))
    # обработка ошибки ввода даты и запись ошибки в файл
    except ValueError as e:
        logger.error(f"Не смог правильно принять дату {date} , ошибка {e}")
        return

    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in (4, 6, 9, 11):
        return day < 31
    elif month == 2:
        if _is_leap(year):
            return day < 30
        else:
            return day < 29
    else:
        return True


if __name__ == "__main__":
    print(is_valid_date(date_to_prove))
