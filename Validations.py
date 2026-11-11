from data import *

def check_name(name):
    if name == "":
        print("The name must be full.") 
        return False
    return True

def check_year(year):
    try:
      num = int(year)
      if num <= 0:
        print("The year must be positive.")
        return False
      return True
    except:
        ValueError("Enter only a positive number")

def check_book(books,name,author):
    for book in books:
        if book["name"] == name and book["author"] == author:
            print("The book is already in the library.")
            return False
        return True

def check_id(num):
    if num == "":
      return False
    return True    