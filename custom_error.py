class TooManyPagesReadError(Exception):
    pass

class Book:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
        
    def __repr__(self):
        return f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
    
    def read(self, number_pages):
        if self.pages_read + number_pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read more number of pages than there are in the book."
            )
        self.pages_read += number_pages
        print(f"You have now read {self.pages_read} pages out {self.page_count}.") 
        
book1 = Book("Python 101", 50)
try:
    book1.read(40)
    book1.read(20)
except TooManyPagesReadError as e:
    print(e)