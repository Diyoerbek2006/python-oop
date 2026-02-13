class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def info(self) -> str:
        return f'brend: {self.brand}\nmodel: {self.model}\nyear: {self.year}'

c01 = Car('GM', 'Cobalt', 2020)

print(c01.info())