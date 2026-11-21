from library_classes.member import Member


class MemberService:

    def __init__(self):

        self.members = []

        self.load_members()



    def load_members(self):

        self.members = [

            Member(1, "Kuldeep", 20, "Male", "9876543210", "Premium", 5),
            Member(2, "Deepu", 21, "Male", "9876541234", "Regular", 2),
            Member(3, "Deepika", 19, "Female", "9123456789", "Premium", 5),
            Member(4, "Rashmika", 20, "Female", "9988776655", "Regular", 2),
            Member(5, "Virat", 22, "Male", "9876509876", "Premium", 5),
            Member(6, "Hardik", 18, "Male", "9876123456", "Regular", 2),
            Member(7, "Ashish", 23, "Male", "9988001122", "Premium", 5),
            Member(8, "Priya", 21, "Female", "9877001122", "Regular", 2),
            Member(9, "Gill", 24, "Male", "9999112233", "Premium", 5),
            Member(10, "Pooja", 20, "Female", "9877889900", "Regular", 2)

        ]



    def display_members(self):

        for member in self.members:
            member.display()



    def search_member_by_id(self, member_id):

        for member in self.members:

            if member.member_id == member_id:
                return member

        return None



    def search_member_by_name(self, name):

        for member in self.members:

            if member.name.lower() == name.lower():
                return member

        return None



    def add_member(self):

        member_id = int(input("Enter Member ID : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        gender = input("Enter Gender : ")
        phone = input("Enter Phone Number : ")

        print("\nMember Types")
        print("1. Premium (5 Books)")
        print("2. Regular (2 Books)")

        choice = input("Enter Choice : ")

        if choice == "1":
            member_type = "Premium"
            max_books = 5
        else:
            member_type = "Regular"
            max_books = 2

        member = Member(
            member_id,
            name,
            age,
            gender,
            phone,
            member_type,
            max_books
        )

        self.members.append(member)

        print("\nMember Added Successfully.")



    def remove_member(self, member_id):

        member = self.search_member_by_id(member_id)

        if member:

            self.members.remove(member)
            print("Member Removed Successfully.")

        else:

            print("Member Not Found.")




    def display_member(self, member_id):

        member = self.search_member_by_id(member_id)

        if member:

            member.display()

        else:

            print("Member Not Found.")



    def total_members(self):

        return len(self.members)
