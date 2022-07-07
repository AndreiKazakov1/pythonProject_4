# **************************************************************************
from var1.Book import book_list, Book, e_book_list


def main():
    while True:
        print()
        print("*** Main_Menu")
        print("1. Add book")
        print("2. Show all books in list")
        print("3. Find book by author")
        print("4. Find book by year of publication")
        print("5. Delete book from list by id")
        print("6. Use @staticmethod")
        print("7. How old is book ?")
        print("8. Exit program")
        print("*** *** ***     *** *** ***")
        print()
        comand = int(input("Enter the command :"))

        if comand == 1:
            add_book()

        elif comand == 2:
            show_all_books(book_list)

        elif comand == 3:
            find_book_by_author(book_list)

        elif comand == 4:
            find_book_by_year(book_list)

        elif comand == 5:
            delete_by_id(book_list)

        elif comand == 6:
            Book.simple_stat_method()

        elif comand == 7:
            how_old_is_book(book_list)

        elif comand == 8:
            print("EXIT FROM PROGRAM ...")
            break
        else:
            print("no such command")


def add_book():
    print("add book")
    try:
        id = int(input("insert id (int value) :"))
        title = str(input("insert title (string value) :"))
        author = str(input("insert author (string value) :"))
        publisher = str(input("insert publisher (string value) :"))
        year_of_publication = int(input("insert year_of_publication (int value) :"))
        number_of_pages = int(input("insert number_of_pages (int value) :"))
        price = float(input("insert price (float value) :"))
        type_of_binding = str(input("insert type_of_binding (string value) :"))

        book = Book(id, title, author, publisher, type_of_binding)
        book.year_of_publication = year_of_publication
        book.number_of_pages = number_of_pages
        book.price = price
        print("book added successfully")
        print(book)
        book_list.append(book)
    except:
        print("!!! incorect data, insert required data type")
        print("try again")


def show_all_books(book_list):
    if len(book_list) > 0:
        print("book list :")
        for books in book_list:
            print(books)
    else:
        print("book list is empty")


def find_book_by_author(book_list):
    searched_books_list = []
    author_name = input("Input name of author : ")
    for book in book_list:
        if author_name == book.author:
            searched_books_list.append(book)
    if len(searched_books_list) > 0:
        print(f"searched book(s) is(are) ...= {len(searched_books_list)}")
        for s_books in searched_books_list:
            print(s_books)
    else:
        print("no such author, back to main menu ...")


def find_book_by_year(book_list):
    searched_books_list = []
    year = int(input("Input year of publication : "))
    for book in book_list:
        if year < book.year_of_publication:
            searched_books_list.append(book)
    if len(searched_books_list) > 0:
        print(f"searched book(s) is(are) ...= {len(searched_books_list)}")
        for s_books in searched_books_list:
            print(s_books)
    else:
        print(f"no books found after this {year} year, back to main menu ...")


def delete_by_id(book_list):
    print("current ")
    show_all_books(book_list)
    del_id = int(input("input ID for delete book from book list : "))
    for book in book_list:
        if del_id == book.id:
            book_list.remove(book)
            print("after delete :")
            show_all_books(book_list)
        else:
            print("no such ID, back to main menu ...")


def how_old_is_book(book_list):
    s_id = int(input("input ID of  book from book list : "))
    for book in book_list:
        if s_id == book.id:
            c_id = book.id
            year = book.year_of_publication
            book2 = Book.book_year(c_id, year)
            print(f'book with id = {c_id} is {book2.title} years old')  # title is 2-nd param == year
        else:
            print("no such ID, back to main menu ...")

# *********************************************************
# ************************************************************
