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
