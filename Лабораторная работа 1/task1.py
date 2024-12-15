# TODO �������� 3 ������ � ������������� � ���������� �����
import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        �������� � ���������� � ������ ������� "�����"

        :param title: �������� �����
        :param author: ����� �����
        :param pages: ���������� �������

        �������:
        >>> book = Book("����� � ���", "��� �������", 1225)  # ������������� ���������� ������
        """
        if not isinstance(title, str):
            raise TypeError("�������� ����� ������ ���� �������")
        if not isinstance(author, str):
            raise TypeError("����� ����� ������ ���� �������")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("���������� ������� ������ ���� ������������� ����� ������")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, page: int) -> str:
        """
        ������ �������� �����.

        :param page: ����� ��������
        :raise ValueError: ���� ����� �������� �������� ������, ��� ����� ������� � �����, �� �������� ������
        :return: ����� ��������

        �������:
        >>> book = Book("����� � ���", "��� �������", 1225)
        >>> book.read(1)
        """
        ...


    def bookmark(self, page: int) -> None:
        """
        ��������� �������� �� ����������� ��������.

        :param page: ����� ��������
        :raise ValueErrror: ���� ����� ������������ �������� ������, ��� ����� ������� � �����, �� �������� ������

        �������:
        >>> book = Book("����� � ���", "��� �������", 1225)
        >>> book.bookmark(100)
        """
        ...


# ����������� ����� ��� "����������"
class Car:
    def __init__(self, brand: str, model: str, fuel_capacity: float):
        """
        �������� � ���������� � ������ ������� "����������"

        :param brand: ����� ����������
        :param model: ������ ����������
        :param fuel_capacity: ����� ���������� ����

        �������:
        >>> car = Car("Toyota", "Camry", 60.0)  # ������������� ���������� ������
        """
        if not isinstance(brand, str):
            raise TypeError("����� ���������� ������ ���� �������")
        if not isinstance(model, str):
            raise TypeError("������ ���������� ������ ���� �������")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("����� ���������� ���� ������ ���� ������������� ������")

        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity


    def drive(self, distance: float) -> None:
        """
        ���� �� ���������� �� ����������� ����������.

        :param distance: ���������� � ����������

        �������:
        >>> car = Car("Toyota", "Camry", 60.0)
        >>> car.drive(100.0)
        """
        ...


    def refuel(self, amount: float) -> None:
        """
        �������� ����������.

        :param amount: ����� ������� ��� ��������

        �������:
        >>> car = Car("Toyota", "Camry", 60.0)
        >>> car.refuel(20.0)
        """
        ...


# ����������� ����� ��� "��������"
class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        �������� � ���������� � ������ ������� "��������"

        :param brand: ����� ���������
        :param model: ������ ���������
        :param battery_capacity: ������� ������������

        �������:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)  # ������������� ���������� ������
        """
        if not isinstance(brand, str):
            raise TypeError("����� ��������� ������ ���� �������")
        if not isinstance(model, str):
            raise TypeError("������ ��������� ������ ���� �������")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("������� ������������ ������ ���� ������������� ����� ������")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity


    def make_call(self, number: str) -> None:
        """
        ���������� ������ �� ��������� �����.


        :param number: ����� ��������

        �������:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)
        >>> smartphone.make_call("+1234567890")
        """
        ...


    def charge(self, amount: int) -> None:
        """
        ������� ���������.

        :param amount: ����� ������ � ����������-�����

        �������:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3200)
        >>> smartphone.charge(1000)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # ������������ ��������, ������� ��������� � ������������


