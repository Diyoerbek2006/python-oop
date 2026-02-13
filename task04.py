class movie:
    def __init__(self, title: str, genre: str, dration: float, rating: float) -> None:
        self.title = title
        self.genre = genre
        self.dration = dration
        self.rating = rating

    def info(self) -> str:
        return f'title: {self.title}, genre: {self.genre}, dration: {self.dration}, rating: {self.rating}'

S01 = movie()

print(S01.info())