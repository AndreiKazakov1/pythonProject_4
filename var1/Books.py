# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические). Создайте три метода (класса,
# объекта и статический). Выберете поле или метод для реализации инкапсуляции. Пропишите запись и считывание (get, set)
# инкапсулированных полей.


# Вар.1 	Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
#  б) список книг, выпущенных после заданного года.

# **************************************************
book_list = []
class Books:
    just_info = "Book-object contains information about book : id, title, author, publisher etc.  "

    @staticmethod
    def simple_stat_method():
        print(Books.just_info)

    @classmethod
    def class_method(cls):
        pass

    def __init__(self, id, title, author, publisher, type_of_binding):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.__year_of_publication = None
        self.__number_of_pages = None
        self.__price = None
        self.type_of_binding = type_of_binding

    def own_method(self):
        pass

    @property
    def year_of_publication(self):
        return self.__year_of_publication

    @year_of_publication.setter
    def year_of_publication(self, year_of_publication):
        if 1444 < year_of_publication < 2023:
            self.__year_of_publication = year_of_publication
        else:
            print("!!!   invalid value of year_of_publication, insert value in range 1445 - 2022")
            self.insert_data_year_of_publication()

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("!!!   invalid value of number_of_pages, insert positive value")
            self.insert_data_number_of_pages()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("!!!  invalid value of price, insert positive value")
            self.insert_data_price()

    def insert_data_year_of_publication(self):
        self.year_of_publication = int(input("insert new year_of_publication :"))

    def insert_data_number_of_pages(self):
        self.number_of_pages = int(input("insert new number_of_pages :"))

    def insert_data_price(self):
        self.price = int(input("insert new price :"))

    def __str__(self):
        return f"id : {self.id} || title : {self.title} || author :{self.author} || publisher :{self.publisher} || " \
               f"year_of_publication :{self.__year_of_publication} || number_of_pages :{self.__number_of_pages} ||" \
               f" price :{self.__price} || type_of_binding :{self.type_of_binding}"


# *******************************
















