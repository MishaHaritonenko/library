import os

LIBRARIANS_FILE = "librarians.txt"
READERS_FILE = "readers.txt"
BOOKS_FILE = "books.txt"


def add_librarian(firstname, lastname):
    with open(LIBRARIANS_FILE, 'a') as file:
        file.write(f"{firstname} {lastname}\n")


def add_reader(firstname, lastname):
    with open(READERS_FILE, 'a') as file:
        file.write(f"{firstname} {lastname}\n")


def add_book(title, author, genre):
    with open(BOOKS_FILE, 'a') as file:
        file.write(f"{title};{author};{genre}\n")


def remove_librarian(firstname, lastname):
    with open(LIBRARIANS_FILE, 'r') as file:
        librarians = file.readlines()

    with open(LIBRARIANS_FILE, 'w') as file:
        for librarian in librarians:
            if not (librarian.startswith(firstname) and librarian.endswith(lastname + '\n')):
                file.write(librarian)


def remove_reader(firstname, lastname):
    with open(READERS_FILE, 'r') as file:
        readers = file.readlines()

    with open(READERS_FILE, 'w') as file:
        for reader in readers:
            if not (reader.startswith(firstname) and reader.endswith(lastname + '\n')):
                file.write(reader)


def remove_book(title, author):
    with open(BOOKS_FILE, 'r') as file:
        books = file.readlines()

    with open(BOOKS_FILE, 'w') as file:
        for book in books:
            if not (book.startswith(title) and book.split(';')[1] == author):
                file.write(book)


def search_books_by_genre(genre):
    with open(BOOKS_FILE, 'r') as file:
        books = file.readlines()

    result = []
    for book in books:
        if book.rstrip().split(';')[2] == genre:
            result.append(book.rstrip().split(';')[0])

    return result


def search_books_by_author(author):
    with open(BOOKS_FILE, 'r') as file:
        books = file.readlines()

    result = []
    for book in books:
        if book.split(';')[1] == author:
            result.append(book.rstrip().split(';')[0])

    return result