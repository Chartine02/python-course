reading_list = []

menu_prompt = """Please choose one option below
- 'a' to add a book
- 'l' to list all the books
- 'q' to quit
"""

selected_option = input(menu_prompt).strip().lower()

def add_book():
    book_title = input("Enter the book's title: ").strip().title()
    book_author = input("Enter a book's author: ").strip().title()
    book_year = input("Enter a book's year of publication: ").strip()
    book = {"title": book_title, "author": book_author, "year": book_year}

    reading_list.append(book)

def list_books():
    for book in reading_list:
        print(f"{book['title']}, by {book['author']}")


while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        list_books()
    else:
        print("Invalid input")

    selected_option = input(menu_prompt).strip().lower()
