from library_classes.books import Book


class BookService:

    def __init__(self):

        self.library = {
            "History": [],
            "Sci-Fi": [],
            "Comics": [],
            "Mystery": [],
            "Fantasy": [],
            "Biography": []
        }

        self.load_books()

    def load_books(self):

       

        self.library["History"] = [

            Book(101, "Sapiens", "Yuval Noah Harari", "History", 10),
            Book(102, "India After Gandhi", "Ramachandra Guha", "History", 10),
            Book(103, "Guns, Germs, and Steel", "Jared Diamond", "History", 10),
            Book(104, "The Diary of a Young Girl", "Anne Frank", "History", 10),
            Book(105, "The Silk Roads", "Peter Frankopan", "History", 10),
            Book(106, "Team of Rivals", "Doris Kearns Goodwin", "History", 10),
            Book(107, "The Wright Brothers", "David McCullough", "History", 10),
            Book(108, "The Rise and Fall of the Third Reich", "William L. Shirer", "History", 10),
            Book(109, "A People's History of the United States", "Howard Zinn", "History", 10),
            Book(110, "The History of the Ancient World", "Susan Wise Bauer", "History", 10)

        ]

       

        self.library["Sci-Fi"] = [

            Book(201, "Dune", "Frank Herbert", "Sci-Fi", 10),
            Book(202, "The Martian", "Andy Weir", "Sci-Fi", 10),
            Book(203, "Ender's Game", "Orson Scott Card", "Sci-Fi", 10),
            Book(204, "Foundation", "Isaac Asimov", "Sci-Fi", 10),
            Book(205, "Neuromancer", "William Gibson", "Sci-Fi", 10),
            Book(206, "The Time Machine", "H. G. Wells", "Sci-Fi", 10),
            Book(207, "Ready Player One", "Ernest Cline", "Sci-Fi", 10),
            Book(208, "Jurassic Park", "Michael Crichton", "Sci-Fi", 10),
            Book(209, "Fahrenheit 451", "Ray Bradbury", "Sci-Fi", 10),
            Book(210, "The War of the Worlds", "H. G. Wells", "Sci-Fi", 10)

        ]

        

        self.library["Comics"] = [

            Book(301, "Watchmen", "Alan Moore", "Comics", 10),
            Book(302, "Batman: The Killing Joke", "Alan Moore", "Comics", 10),
            Book(303, "Spider-Man: Blue", "Jeph Loeb", "Comics", 10),
            Book(304, "Batman: Year One", "Frank Miller", "Comics", 10),
            Book(305, "Maus", "Art Spiegelman", "Comics", 10),
            Book(306, "Tintin in Tibet", "Herge", "Comics", 10),
            Book(307, "Asterix the Gaul", "Rene Goscinny", "Comics", 10),
            Book(308, "The Blue Lotus", "Herge", "Comics", 10),
            Book(309, "Superman: Red Son", "Mark Millar", "Comics", 10),
            Book(310, "The Sandman", "Neil Gaiman", "Comics", 10)

        ]

        

        self.library["Mystery"] = [

            Book(401, "The Da Vinci Code", "Dan Brown", "Mystery", 10),
            Book(402, "Gone Girl", "Gillian Flynn", "Mystery", 10),
            Book(403, "The Girl with the Dragon Tattoo", "Stieg Larsson", "Mystery", 10),
            Book(404, "Murder on the Orient Express", "Agatha Christie", "Mystery", 10),
            Book(405, "The Hound of the Baskervilles", "Arthur Conan Doyle", "Mystery", 10),
            Book(406, "The Silent Patient", "Alex Michaelides", "Mystery", 10),
            Book(407, "Big Little Lies", "Liane Moriarty", "Mystery", 10),
            Book(408, "The Girl on the Train", "Paula Hawkins", "Mystery", 10),
            Book(409, "And Then There Were None", "Agatha Christie", "Mystery", 10),
            Book(410, "The Reversal", "Michael Connelly", "Mystery", 10)

        ]

        
        self.library["Fantasy"] = [

            Book(501, "Harry Potter and the Philosopher's Stone", "J. K. Rowling", "Fantasy", 10),
            Book(502, "The Hobbit", "J. R. R. Tolkien", "Fantasy", 10),
            Book(503, "The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 10),
            Book(504, "A Game of Thrones", "George R. R. Martin", "Fantasy", 10),
            Book(505, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", "Fantasy", 10),
            Book(506, "Percy Jackson", "Rick Riordan", "Fantasy", 10),
            Book(507, "The Name of the Wind", "Patrick Rothfuss", "Fantasy", 10),
            Book(508, "Eragon", "Christopher Paolini", "Fantasy", 10),
            Book(509, "The Eye of the World", "Robert Jordan", "Fantasy", 10),
            Book(510, "The Last Unicorn", "Peter S. Beagle", "Fantasy", 10)

        ]

        

        self.library["Biography"] = [

            Book(601, "Wings of Fire", "A. P. J. Abdul Kalam", "Biography", 10),
            Book(602, "Steve Jobs", "Walter Isaacson", "Biography", 10),
            Book(603, "Long Walk to Freedom", "Nelson Mandela", "Biography", 10),
            Book(604, "Becoming", "Michelle Obama", "Biography", 10),
            Book(605, "The Diary of a Young Girl", "Anne Frank", "Biography", 10),
            Book(606, "Elon Musk", "Walter Isaacson", "Biography", 10),
            Book(607, "Einstein: His Life and Universe", "Walter Isaacson", "Biography", 10),
            Book(608, "Shoe Dog", "Phil Knight", "Biography", 10),
            Book(609, "Gandhi: An Autobiography", "Mahatma Gandhi", "Biography", 10),
            Book(610, "Open", "Andre Agassi", "Biography", 10)

        ]
   



    def display_categories(self):

        print("\nBook Categories:\n")

        for category in self.library:
            print(category)


    def display_category(self, category):

        if category in self.library:

            for book in self.library[category]:
                book.display()

        else:
            print("Category not found.")


    def display_all_books(self):

        for category in self.library:

            print(f"\n===== {category} =====")

            for book in self.library[category]:
                book.display()


    def search_book_by_id(self, book_id):

        for category in self.library.values():

            for book in category:

                if book.book_id == book_id:
                    return book

        return None


    def search_book_by_title(self, title):

        for category in self.library.values():

            for book in category:

                if book.title.lower() == title.lower():
                    return book

        return None