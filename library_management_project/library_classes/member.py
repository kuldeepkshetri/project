class Member:

    def __init__(self, member_id, name, age, gender, phone, member_type, max_books):

        self.member_id = member_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.member_type = member_type
        self.max_books = max_books


        self.borrowed_books = []



    def display(self):

        print("-" * 50)
        print(f"Member ID     : {self.member_id}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Gender        : {self.gender}")
        print(f"Phone Number  : {self.phone}")
        print(f"Member Type   : {self.member_type}")
        print(f"Book Limit    : {self.max_books}")
        print(f"Books Issued  : {len(self.borrowed_books)}")
        print("-" * 50)



    def borrow_book(self, book):

        if len(self.borrowed_books) < self.max_books:

            self.borrowed_books.append(book)
            return True

        return False



    def return_book(self, book):

        if book in self.borrowed_books:

            self.borrowed_books.remove(book)
            return True

        return False



    def display_borrowed_books(self):

        if len(self.borrowed_books) == 0:

            print("No books issued.")
            return

        print(f"\nBooks issued by {self.name}\n")

        for book in self.borrowed_books:

            print(f"{book.book_id} - {book.title}")



    def __str__(self):

        return (f"{self.member_id} | "
                f"{self.name} | "
                f"{self.member_type} | "
                f"{len(self.borrowed_books)}/{self.max_books}")