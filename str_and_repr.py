class Person:
    @classmethod
    def class_method(cls):
        print(f"Called class method of the {cls}")
        
    @staticmethod
    def static_method():
        print("Called static method")
Person.static_method()

class Book:
    TYPES=("HARDCOVER", "SOFTCOVER")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighs {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, paper_weight):
        return cls(name, cls.TYPES[0], paper_weight + 100)
    
    @classmethod
    def paperback(cls, name, paper_weight):
        return cls(name, cls.TYPES[1], paper_weight + 100)
    
book = Book.hardcover("Cars", 1200)
book1 = Book.paperback("Cars", 600)
print(book)
print(book1)