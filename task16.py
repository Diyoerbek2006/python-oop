class Book:
    def __init__(self, title:str, auther: str, is_read:bool) -> None:
        self.title = title 
        self.auther = auther
        self.is_read = is_read
    
    def mark_is_read(self,is_read:bool) -> None:
        if self.is_read == True:
            self.is_read = False
        else:
            self.is_read = True
    
    def status():
        print(f'holat-{self.is_read}, muallif-{self.auther}, kitob nomi{self.title}')

book1 = Book("Python Basics", "Ali")
book2 = Book("C++ Guide", "Vali")
book3 = Book("Algorithms", "Hasan")
book4 = Book("Data Science", "Husan")
book5 = Book("AI Fundamentals", "Olim")

books = [book1, book2, book3, book4, book5]

book2.mark_as_read()
book4.mark_as_read()

for book in books:
    book.status()