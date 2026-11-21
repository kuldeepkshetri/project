from datetime import datetime


class Transaction:

    def __init__(self, transaction_id, member, book):
        self.transaction_id = transaction_id
        self.member = member
        self.book = book
        self.issue_date = datetime.now().strftime("%d-%m-%Y")
        self.return_date = None
        self.status = "Issued"




    def return_book(self):
        self.return_date = datetime.now().strftime("%d-%m-%Y")
        self.status = "Returned"

  

    def display(self):

        print("-" * 50)
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Member ID      : {self.member.member_id}")
        print(f"Member Name    : {self.member.name}")
        print(f"Book ID        : {self.book.book_id}")
        print(f"Book Name      : {self.book.title}")
        print(f"Issue Date     : {self.issue_date}")
        print(f"Return Date    : {self.return_date}")
        print(f"Status         : {self.status}")
        print("-" * 50)

    def __str__(self):

        return (f"{self.transaction_id} | "
                f"{self.member.name} | "
                f"{self.book.title} | "
                f"{self.status}")