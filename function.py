from data import *
from Validations import *

def menu():
     print("================================")
     print("           LIBRARY MANAGEMENT   ")
     print("================================")         
     print("   1. Display all books")
     print("   2. Search book by name")
     print("   3. Add new book")
     print("   4. Borrow a book")
     print("   5. Return a book")
     print("   6. Display available books")
     print("   7. Display books by author")
     print("   8.  Exit")
     
          

def display_books(books): #1
     for book in books:
          print(book)


def search_book(books,name): #2
    if check_name(name):
      list_books = []
      for book in books:
         if name in book["name"]:
            list_books.append(book)
      if list_books == []:
          return None
      else:
         return list_books
    else:
        return

    
def get_next_book_id(books): #3
    return (len(books)+ 1)

def add_book(bookse, name, author, year): #3
    if check_name(name) and check_name(author) and check_year(year) and check_book(books,name,author) == True:
      new_book = {  "id": 0, "name": "0","author": "0",    "year": 1,"available": True }
      new_book["id"] = get_next_book_id(bookse)
      new_book["name"] = name
      new_book["author"] = author
      new_book["year"] = year
      books.append(new_book)
      return
    else:
        return   

def borrow_book(books,book_id): #4
    if not check_id(book_id):
        print("enter a number")
        return
    num = int(book_id) 
    for book in books:
        if book["id"] == num:
            if book["available"] == False:
                print("This book is already checked out.") 
                return
            book["available"] = False  
            print("The book was successfully borrowed.")
            return
    print("ID number not found")
    return    

def return_book(books, book_id): #5
    if not check_id(book_id):
        print("enter a number")
        return
    num = int(book_id) 
    for book in books:
        if book["id"] == num:
            if book["available"] == True:
                print("This book is already in the library.") 
                return
            book["available"] = True  
            print("The book was returned successfully.")
            return
    print("ID number not found")
    return 

def get_available_books(books):  #6
    available_books = []
    for book in books:
        if book["available"] == True:
            available_books.append(book)
    for book in available_books:
        print(book)        

def get_books_by_author(books, author): #7
     author_books = []
     for book in books:
       if book["author"] == author:
           author_books.append(book)
     if author_books == []:
         print("No books by this author were found.")

     else: 
         for book in author_books:
             print(book)
            
def main():
    while True:
        menu()
        choice = input("   Choose an option:")
        if choice == "1":
            display_books(books)
        elif choice == "2":
            name = input("Enter the book name: ")
            print(search_book(books,name))
        elif choice == "3":
            name = input("Enter the book name: ")
            author = input("Enter the author name: ")
            year = input("Enter the year of publication: ")
            add_book(books, name, author, year)
        elif choice == "4":
            book_id = input("Enter the book id: ")
            borrow_book(books,book_id) 
        elif choice == "5":
            book_id = input("Enter the book id: ")
            return_book(books,book_id)
        elif choice == "6":
            get_available_books(books)
        elif choice == "7":
             author = input("Enter the author name: ")
             get_books_by_author(books, author)
        elif choice == "8":
           exit()
        else:
            print("Enter a number between 1 and 8 only!")