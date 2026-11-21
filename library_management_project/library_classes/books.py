class Book:

    def __init__(self, book_id, title, author, category, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity



    def display(self):

        print("-" * 50)
        print(f"Book ID       : {self.book_id}")
        print(f"Title         : {self.title}")
        print(f"Author        : {self.author}")
        print(f"Category      : {self.category}")
        print(f"Available     : {self.quantity}")
        print("-" * 50)


    def issue_book(self):

        if self.quantity > 0:
            self.quantity -= 1
            return True

        return False



    def return_book(self):

        self.quantity += 1


    def update_quantity(self, quantity):

        self.quantity = quantity



    def __str__(self):

        return (f"{self.book_id} | "
                f"{self.title} | "
                f"{self.author} | "
                f"{self.category} | "
                f"{self.quantity}")