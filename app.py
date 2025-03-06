def load_books():
    books = []
    try:
        with open("books.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:  
                    continue
                parts = line.split("|")
                if len(parts) != 6: 
                    print(f"Skipping invalid line: {line}")
                    continue
                title, author, isbn, genre, price, quantity = parts
                books.append({
                    "Title": title,
                    "Author": author,
                    "ISBN": isbn,
                    "Genre": genre,
                    "Price": float(price),
                    "Quantity": int(quantity)
                })
    except FileNotFoundError:
        print("books.txt file not found. Creating a new one...")
    return books

def save_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(f"{book['Title']}|{book['Author']}|{book['ISBN']}|{book['Genre']}|{book['Price']}|{book['Quantity']}\n")

def add_book(books):
    title = input("Book Nam Dao: ")
    author = input("Author Nam: ")
    isbn = input("ISBN: ")
    genre = input("Genre: ")
    try:
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        if price <= 0 or quantity < 0:
            print("Zero price hobe na")
            return
        for book in books:
            if book["ISBN"] == isbn:
                print("ISBN name e book already ace!")
                return
        books.append({"Title": title, "Author": author, "ISBN": isbn, "Genre": genre, "Price": price, "Quantity": quantity})
        save_books(books)
        print("Book added successfully ..! ")
    except ValueError:
        print("Vul input.")

def view_books(books):
    if not books:
        print("No books here.")
        return
    for book in books:
        print(f"{book['Title']} by {book['Author']} (ISBN: {book['ISBN']}) - {book['Price']}$, Stock: {book['Quantity']}")

def search_books(books):
    keyword = input("Enter title, author, or ISBN: ").lower()
    matches = [book for book in books if keyword in book["Title"].lower() or keyword in book["Author"].lower() or keyword == book["ISBN"]]
    if matches:
        for book in matches:
            print(f"{book['Title']} by {book['Author']} - {book['Price']}$")
    else:
        print("No Book found.")

def remove_book(books):
    isbn = input("ISBN dao remove korar jonno: ")
    for book in books:
        if book["ISBN"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed.")
            return
    print("Book not found.")

def main():
    books = load_books()
    while True:
        print("\nBook Store Management System")
        print("1. Add Book\n2. View Books\n3. Search Book\n4. Remove Book\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            remove_book(books)
        elif choice == "5":
            save_books(books)
            print("Book/Data saved. Exiting...")
            break
        else:
            print("Vul choice!")

if __name__ == "__main__":
    main()