# Zanti Carlos B. Antero
# 9 - Beryillium
# Oct/20/2026

# Sets Publications as the parent class.
class Publications:
    def __init__(self, title, author): # initializes itself with the title and author of the publication.
        self.Title = title
        self.Author = author

    def get_info(self):
        return f"{self.Title} by {self.Author}" # Method that returns the title and author of the publication.

# Class Book is set as a child class of Publications.
class Book(Publications):
    def __init__(self, title, author, numberofpages):
        super().__init__(title, author) # Inherits the title and author from the parent class.
        self.numberofpages = numberofpages
        
    def get_info(self):
        return f"{self.Title} by {self.Author}, {self.numberofpages} pages" # Again this is a method that returns the title, author, in addition to that it also returns a new attribute which is the number of pages of the book.

    def set_number_of_pages(self, numberofpages): # This method sets the number of pages of the book and checks if the number of pages is valid since logically no book could EVER have a negative number of pages.
        self.numberofpages = numberofpages
        if numberofpages < 0:
            raise ValueError("Number of pages is invalid.") # Prints an error message when the user trolls and adds a negative number of pages to the book.
        return self.numberofpages

    def get_number_of_pages(self): # This method just returns the number of pages of the book.
        return self.numberofpages

# We set another child class
class Magazine(Publications):
    def __init__(self, title, author, issuenumber):
        super().__init__(title, author) # Again here we just inherit the title and author from the Publications.
        self.issuenumber = issuenumber
        
    def get_info(self):
        return f"{self.Title} by {self.Author}, Issue: {self.issuenumber}" # This method basically just returns the title, author and also a new attribute which is the issue number.
    
    def set_issue_number(self, issuenumber): # This method sets the issue number of the magazine and just like the other line, checks if the set issue number is valid or not.
        if issuenumber < 0:
            raise ValueError("Issue number is invalid.") # Again, this prints an error message when the user sets a negative issue number.
        self.issuenumber = issuenumber

    def get_issue_number(self):
        return self.issuenumber
    
# I guess the following code is given for testing, and to show that the classes are working properly.
Publication1 = Publications("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") 
Book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
Magazine1 = Magazine("National Geographic", "Various Authors", 202)

# This prints the information of publications, by using the get_info() method.
print("Publication Information:")
print(Publication1.get_info())

# Prints the information of the book, by using the get_info() method in addition to that, it also prints the number of pages by using another method get_number_of_pages().
print(Book1.get_info())
print(f"Number of Pages: {Book1.get_number_of_pages()}")

# AGAIN it prints the information of the magazine by using the method get_info() in addition to that, it also prints the issue number by using another method get_issue_number() wow creative.
print("\nMagazine Information:")
print(Magazine1.get_info())
print(f"Issue Number: {Magazine1.get_issue_number()}")
