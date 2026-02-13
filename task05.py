class Praduct:
    def __init__(self, name: str, price: float, category: str,  is_active: bool) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.is_active = is_active

    def info(self) -> str:
        return f'name: {self.name} \nprice: {self.price} \ncategory: {self.category} \nis_active: {self.is_active}'

S01 = Praduct()
print(S01.info())