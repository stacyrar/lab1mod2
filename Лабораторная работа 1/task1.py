# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, page: int) -> str:
        """
        Чтение страницы книги.

        :param page: Номер страницы
        :raise ValueError: Если номер читаемой страницы больше, чем всего страниц в книге, то вызываем ошибку
        :return: Текст страницы

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read(1)
        """
        ...


    def bookmark(self, page: int) -> None:
        """
        Установка закладки на определённую страницу.

        :param page: Номер страницы
        :raise ValueErrror: Если номер определенной страницы больше, чем всего страниц в книге, то вызываем ошибку

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.bookmark(100)
        """
        ...


# Абстрактный класс для "Автомобиль"
class Car:
    def __init__(self, brand: str, model: str, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param fuel_capacity: Объём топливного бака

        Примеры:
        >>> car = Car("Toyota", "Camry", 60.0)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Объём топливного бака должен быть положительным числом")

        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity


    def drive(self, distance: float) -> None:
        """
        Езда на автомобиле на определённое расстояние.

        :param distance: Расстояние в километрах

        Примеры:
        >>> car = Car("Toyota", "Camry", 60.0)
        >>> car.drive(100.0)
        """
        ...


    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля.

        :param amount: Объём топлива для заправки

        Примеры:
        >>> car = Car("Toyota", "Camry", 60.0)
        >>> car.refuel(20.0)
        """
        ...


# Абстрактный класс для "Смартфон"
class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Марка смартфона
        :param model: Модель смартфона
        :param battery_capacity: Ёмкость аккумулятора

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка смартфона должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Ёмкость аккумулятора должна быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity


    def make_call(self, number: str) -> None:
        """
        Совершение звонка на указанный номер.


        :param number: Номер телефона

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)
        >>> smartphone.make_call("+1234567890")
        """
        ...


    def charge(self, amount: int) -> None:
        """
        Зарядка смартфона.

        :param amount: Объём заряда в миллиампер-часах

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)
        >>> smartphone.charge(1000)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


