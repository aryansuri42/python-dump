class BookShelf:
    
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"Book shelf with {len(self.books)} books"
    
class Book:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"{self.name}"
    
book = Book("Harry Potter")
book2 = Book("Cars")
print(BookShelf(book, book2))