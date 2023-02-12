if __name__ == "__main__":

    import doctest


    class BasicRoom:
        """
        Создание и подготовка к работе базового класса "Базовая Комната"
        :param number: Номер комнаты
        :param width: Ширина комнаты в сантиметрах
        :param length: Длина комнаты в сантиметрах
        """

        def __init__(self, number: int, width: int, length: int):
            self.number = number
            self.width = width
            self.length = length
            if not number > 0:
                raise ValueError("Номер комнаты должен быть не ниже 1")

            if not width > 0:
                raise ValueError("Ширина комнаты должна быть не ниже 1")

            if not length > 0:
                raise ValueError("Длина комнаты должна быть не ниже 1")

        def __repr__(self) -> str:
            return f"{self.__class__}: {self.number}"

        def __str__(self) -> str:
            return 'Комната ' + str(self.number)

        def get_area(self) -> int:
            """
            Функция подсчитывает и возвращает площадь комнаты
            """
            return self.width * self.length

        def get_floor(self) -> int:
            """
            Функция возвращает номер этажа, на котором находится комната - по определению, первая цифра номера комнаты
            """
            return int(str(self.number)[0])


    class LShapedRoom(BasicRoom):
        """
        Создание и подготовка к работе класса "L-образная Комната"
        :param number: Номер комнаты
        :param width: Ширина основной части комнаты в сантиметрах
        :param length: Длина основной части комнаты в сантиметрах
        :param width2: Ширина дополнительной части комнаты в сантиметрах
        :param length2: Длина дополнительной части комнаты в сантиметрах
        """

        def __init__(self, number, width, length, width2, length2):
            """
            Расширяем конструктор базового класса, так как есть дополнительные атрибуты - Ширина и длина дополнительной
            части комнаты (width2, length2)
            """
            BasicRoom.__init__(self, number, width, length)
            self.width2 = width2
            self.length2 = length2

            if not width > 0:
                raise ValueError("Ширина основной части комнаты должна быть не ниже 1")

            if not length > 0:
                raise ValueError("Длина основной части комнаты должна быть не ниже 1")

            if not width2 > 0:
                raise ValueError("Ширина доп. части комнаты должна быть не ниже 1")

            if not length2 > 0:
                raise ValueError("Длина доп. части комнаты должна быть не ниже 1")

        def __repr__(self) -> str:
            return super().__repr__()

        def __str__(self) -> str:
            return super().__str__()

        def get_area(self) -> int:
            """
            Перегружаем функцию get_area, так как у сложной комнаты другая формула подсчета площади
            """
            return (self.width * self.length) + (self.width2 * self.length2)

        def get_floor(self) -> int:
            return BasicRoom.get_floor(self)


    print(BasicRoom(25, 300, 500))
    print(repr(BasicRoom(25, 300, 500)))

    print(LShapedRoom(38, 300, 500, 150, 70))
    print(repr(LShapedRoom(38, 300, 500, 150, 70)))

    room25 = BasicRoom(25, 300, 500)
    print(room25.get_area)
    print(room25.get_floor())

    room38 = LShapedRoom(38, 300, 500, 150, 70)
    print(room38.get_area())
    print(room38.get_floor())

    if __name__ == "__main__":
        doctest.testmod()

    pass
