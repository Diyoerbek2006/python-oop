class Students:
    def __init__(self, ism: str, yosh: int, great: int) -> None:
        self.ism = ism
        self.yosh = yosh
        self.great = great

    def info(self) -> str:
        return f'{self.ism}: {self.yosh} yoshda, {self.great}-sinf uquvchisi'

S01 = Students('ali', 16, 5)

print(S01.info())