from library_classes.book_services import BookService
from library_classes.member_services import MemberService
from library_classes.transaction_services import TransactionService


book_service = BookService()
member_service = MemberService()
transaction_service = TransactionService()




def book_menu():

    while True:

        print("\n========== BOOK MANAGEMENT ==========")
        print("1. Display Categories")
        print("2. Display Books By Category")
        print("3. Display All Books")
        print("4. Search Book By ID")
        print("5. Search Book By Title")
        print("6. Back")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            book_service.display_categories()

        elif choice == "2":

            category = input("Enter Category : ")
            book_service.display_category(category)

        elif choice == "3":

            book_service.display_all_books()

        elif choice == "4":

            book_id = int(input("Enter Book ID : "))

            book = book_service.search_book_by_id(book_id)

            if book:
                book.display()
            else:
                print("Book Not Found.")

        elif choice == "5":

            title = input("Enter Book Title : ")

            book = book_service.search_book_by_title(title)

            if book:
                book.display()
            else:
                print("Book Not Found.")

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")




def member_menu():

    while True:

        print("\n========== MEMBER MANAGEMENT ==========")
        print("1. Display All Members")
        print("2. Search Member By ID")
        print("3. Search Member By Name")
        print("4. Add Member")
        print("5. Remove Member")
        print("6. Back")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            member_service.display_members()

        elif choice == "2":

            member_id = int(input("Enter Member ID : "))

            member = member_service.search_member_by_id(member_id)

            if member:
                member.display()
            else:
                print("Member Not Found.")

        elif choice == "3":

            name = input("Enter Member Name : ")

            member = member_service.search_member_by_name(name)

            if member:
                member.display()
            else:
                print("Member Not Found.")

        elif choice == "4":

            member_service.add_member()

        elif choice == "5":

            member_id = int(input("Enter Member ID : "))
            member_service.remove_member(member_id)

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")



def issue_book():

    member_id = int(input("Enter Member ID : "))
    book_id = int(input("Enter Book ID : "))

    member = member_service.search_member_by_id(member_id)
    book = book_service.search_book_by_id(book_id)

    transaction_service.issue_book(member, book)




def return_book():

    member_id = int(input("Enter Member ID : "))
    book_id = int(input("Enter Book ID : "))

    member = member_service.search_member_by_id(member_id)
    book = book_service.search_book_by_id(book_id)

    transaction_service.return_book(member, book)




def transaction_menu():

    while True:

        print("\n========== TRANSACTIONS ==========")
        print("1. Display All Transactions")
        print("2. Display Issued Books")
        print("3. Search Transaction")
        print("4. Back")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            transaction_service.display_transactions()

        elif choice == "2":

            transaction_service.display_issued_books()

        elif choice == "3":

            transaction_id = int(input("Enter Transaction ID : "))

            transaction = transaction_service.search_transaction(transaction_id)

            if transaction:
                transaction.display()
            else:
                print("Transaction Not Found.")

        elif choice == "4":

            break

        else:

            print("Invalid Choice.")



def main():

    while True:

        print("\n")
        print("=" * 50)
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Transactions")
        print("6. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            book_menu()

        elif choice == "2":

            member_menu()

        elif choice == "3":

            issue_book()

        elif choice == "4":

            return_book()

        elif choice == "5":

            transaction_menu()

        elif choice == "6":

            print("\nThank You For Using Library Management System.")
            break

        else:

            print("Invalid Choice.")



main()