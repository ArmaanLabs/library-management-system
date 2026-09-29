from pathlib import Path
import json

class Book:


    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available



    def __str__(self):
        return f"Title of the book is {self.title} written by {self.author}, isbn number {self.isbn}"


class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.book_issued = []
        self.issue_date = None
        self.return_date = None



    def __str__(self):
        return f"Member  {self.name} with employ id :  {self.member_id} was successfully added !!"

       




class Library:
    def __init__(self):
        self.book = []
        self.member = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.book.append(new_book)


    def display_all_book(self):

        for book in self.book:
            print(book)



    def add_member(self,name,member_id):
        new_member = Member(name,member_id)
        self.member.append(new_member)



    def find_book(self,isbn):
        for book in self.book:
            if book.isbn == isbn:
                
                return book
        return None


    def book_ava(self,isbn):
        found_book = self.find_book(isbn)
        if found_book:
            status = "available" if found_book.available else "not available"
            return f"Book with isbn {found_book.isbn} and title '{found_book.title}' is {status}!"
        else:
            return f"Book with isbn {isbn} does not exist!"

    


    def borrow_book(self,isbn,member_id):
        found_member = None
        for mem in self.member:
            if mem.member_id == member_id:
                found_member = mem
                break

        if not found_member:
            return f"Member with member id {member_id} does not exist"
            
        found_book = self.find_book(isbn)
        if not found_book:
            return f"Book with isbn number {isbn} does not exist."

        if found_book:
            if found_book.available:
                        found_book.available = False
                        found_member.book_issued.append(found_book)
                        return f"Book '{found_book.title}' was successfully issued to {found_member.name}!"
            else:
                return f"Book with isbn code {isbn} is not available."    

    def return_book(self,isbn,member_id):
        found_book = self.find_book(isbn)
        if not found_book:
            return f"Book with isbn number {isbn} does not exist."
        found_member = None
        for mem in self.member:
            if mem.member_id == member_id:
                found_member = mem
                break
        if not found_member:
            return f"Member with member id {member_id} does not exist"
        
        if found_book in found_member.book_issued:
            found_book.available = True 
            found_member.book_issued.remove(found_book)
            return f"Book '{found_book.title}' was returned by {found_member.name}"
        else :
            return f"There is some error"




    def save_file(self,filename = "library.json"):
        data = { 
            "books" : [{"title" : b.title,
                        "author" : b.author,
                        "isbn" : b.isbn ,
                        "available" : b.available
                        } for b in self.book] , 
            "members" : [{"name" : m.name,
                          "member_id": m.member_id,
                            } for m in self.member]
            
        }
        with open(filename,"w") as f:
            json.dump(data,f)

    def load_from_file(self, filename="library.json"):
        try:
            with open(filename) as f:
                data = json.load(f)
            for b in data["books"]:
                book = Book(b["title"], b["author"], b["isbn"], b["available"])
                self.book.append(book)
            for m in data["members"]:
                self.member.append(Member(m["name"], m["member_id"]))
        except FileNotFoundError:
            pass  
                        







        


my_library = Library()
my_library.load_from_file()



while True:
    print('''Enter 1 to Add New Book
Enter 2 to Add new member
Enter 3 to check availability of book
Enter 4 to View all books
Enter 5 to borrow a book
Enter 6 to return book
Enter 7 to quit ''')


    try:
        a = input("Enter Your choice : ")
    except Exception as err:
        print(f"There was an error: {err}")
        continue


    if a == '1':
        title = input("Enter Book Title : ")
        author = input("Enter Book Author Name : ")
        isbn = input("Enter Book isbn number : ")


        my_library.add_book(title, author, isbn)
       

        print(f"Successfully added {my_library.book[-1]}")

       
    elif a == '2':
        name = input("Enter member Name : " )
        member_id = input("Enter member id : " )
        my_library.add_member(name,member_id)


        print(my_library.member[-1])


    elif a == '3':
        isbn_issue_book = input("Enter isbn of issueing book = ")
        print(my_library.book_ava(isbn_issue_book))




    elif a == '4':       

        my_library.display_all_book()



    elif a == "5":
           

        isbn_issue_book = input("Enter isbn of issueing book = ")
        member_id = input("Enter Member id of borrower = ")
        print(my_library.borrow_book(isbn_issue_book,member_id))

    elif a == '6':
        isbn_return = input("Enter isbn of book to return = ")
        member_id = input("Enter Member id = ")
        print(my_library.return_book(isbn_return, member_id))
    elif a == '7':
        my_library.save_file()
        break
