class Praduct:
    def __init__(self, name: str, price: float, category: str,  is_active: bool) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.is_active = is_active

    def info(self) -> str:
        if is_active == True:
            return f'{self.name} omborda mavjud'
        else:
            return f'{self.name} mahsulot tugagan'


S01 = Praduct()
print(S01.info())