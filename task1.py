import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Cup:
    def __init__(self, liquid:str,volume: int,place:str):
        """
        Создание и подготовка к работе обьекта "Кружка"
        :param liquid: Жидкость в кружке
        :param volume: Объём кружки в мл
        :param place: Место где находится кружка

        Пример:
        >>> cup_1 = Cup("Вода",250, "Верхний шкаф") #инициализация экземпляра класса
        """
        if not isinstance(liquid, str):
            raise TypeError
        self.liquid=liquid
        if not isinstance(place, str):
            raise TypeError
        self.place = place
        if volume < 0:
            raise ValueError("Обьём должен быть положительным числом")
        self.volume = volume
    def move_the_mug(self):
        ...# Перемещаем кружку (например из шкафа на стол)
    def pour_smt_into_a_mug(self):
        ... # Вылить предыдущую жидкость , налить новую

class Garland:
    def __init__(self,color :str,mode: int,length: int):
        """
        Создание оздание и подготовка к работе обьекта "Гирлянда"
        :param color: Цвет гирлянды
        :param mode: Режим работы гирлянды(1-свечение, 2-мерцание, 3-"волна")
        :param length: Длина гирлянды в метрах

        Пример:
        >>> gerlanda_1 = Garland("Красный",1,6)
        """
        if not isinstance(color, str):
            raise TypeError
        self.color = color
        if mode > 3 and mode <1 :
            raise ValueError
        self.mode = mode
        if length < 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length
    def change_mode(self):
        ...# Изменить режим работы
    def change_color(self):
        ...# Изменить цвет

class Monitor:
    def __init__(self, diagonal: int,screen_resolution: str, manufacturer: str,condition: bool):
        """
        Создание и подготовка к работе обьекта "Монитор"
        :param diagonal: Размер диогонали экрана в дюймах
        :param manufacturer: Компания производитель
        :param condition: Состояние экрана (включен=True / выключен=Fasle)
        :param screen_resolution: Разрешение экрана (Например:SXGA, WXGA, Full HD,...)

        Пример:
        >>> monitor_1 = Monitor(27,"SXGA","Apple",True) #инициализация экземпляра класса
        """
        if diagonal < 0:
            raise ValueError("Диогональ экрана должена быть положительным числом")
        self.diagonal = diagonal
        if not isinstance(screen_resolution, str):
            raise TypeError
        self.screen_resolution = screen_resolution
        if not isinstance(manufacturer, str):
            raise TypeError
        self.manufacturer = manufacturer
        if not isinstance(condition, bool):
            raise TypeError
        self.condition = condition
    def change_monitor_condition(self):
        ...# Изменить состояние монитора
    def change_screen_resolution(self):
        ...# Изменить разрешение экрана



if __name__ == "__main__":
    monitor2 = Monitor(21,"Full HD","Sony",False)
    print(monitor2.diagonal, monitor2.condition)
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
