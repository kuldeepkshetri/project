from library_classes.transaction import Transaction


class TransactionService:

    def __init__(self):

        self.transactions = []
        self.transaction_id = 1001



    def issue_book(self, member, book):

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.quantity == 0:
            print("Book is not available.")
            return

        if len(member.borrowed_books) >= member.max_books:
            print("Member has reached maximum limit.")
            return

        if member.borrow_book(book):

            book.issue_book()

            transaction = Transaction(
                self.transaction_id,
                member,
                book
            )

            self.transactions.append(transaction)

            self.transaction_id += 1

            print("Book issued successfully.")



    def return_book(self, member, book):

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if member.return_book(book):

            book.return_book()

            for transaction in self.transactions:

                if (transaction.member == member and
                        transaction.book == book and
                        transaction.status == "Issued"):

                    transaction.return_book()

                    print("Book returned successfully.")
                    return

        print("This member has not borrowed this book.")



    def display_transactions(self):

        if len(self.transactions) == 0:
            print("No transactions available.")
            return

        for transaction in self.transactions:
            transaction.display()


    def display_issued_books(self):

        found = False

        for transaction in self.transactions:

            if transaction.status == "Issued":
                transaction.display()
                found = True

        if not found:
            print("No books are currently issued.")



    def search_transaction(self, transaction_id):

        for transaction in self.transactions:

            if transaction.transaction_id == transaction_id:
                return transaction

        return None