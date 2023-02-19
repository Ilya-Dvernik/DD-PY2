class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = {self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError('Страницы должны быть типа int')
        if new_pages <= 0:
            raise ValueError('Страницы должны быть положительным числом')
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self)-> str:
        super_str = super().__str__()
        return f"{super_str}. Продолжительность {self.duration}"

    def __repr__(self)-> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError('Продолжительность должна быть типа float')
        if new_duration <= 0:
            raise ValueError('Продолжительность должны быть положительным числом')
        self._duration =new_duration


kniga1 = Book('skazki','grimm')

print(kniga1.__repr__())
print(kniga1.__str__())
kniga1= PaperBook('skazki','grimm',30)
print(kniga1.__repr__())
kniga1= AudioBook('skazki','grimm',3.55)
print(kniga1.__str__())
print(kniga1.__repr__())