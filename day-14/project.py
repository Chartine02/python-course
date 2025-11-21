
def add_book():
    title = input("Book's title:").strip().title()
    author = input("Book's author:").strip().title()
    year = input("Book's year of publication:").strip()
    read = input("Have you read the book, (yes/no):").strip().lower()
    # read = True if input("Have you read the book, (yes/no):").strip().lower() == 'yes' else False

    with open("books.csv", "a") as write_file:
            write_file.write(f"{title},{author},{year},{read}")


def get_books():
    books = []
    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read = book.split(',')
            books.append({"title": title, "author": author, "year": year, "read": read})
    return books

def find_book():
    reading_list = get_books()
    title= input("Name the title of the book you are looking for:")
    matching_books = []

    for book in reading_list:
        if title in book["title"]:
            matching_books.append(book)

    return matching_books

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    print()

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        reading_list = get_books()

        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "s":
        matching_books = find_book()

        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    selected_option = input(menu_prompt).strip().lower()