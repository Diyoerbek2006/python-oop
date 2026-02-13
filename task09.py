class user:
    def __init__(self, username: str, email: str, is_active: bool) -> None:
        self.username = username
        self.email = email
        self.is_active = is_active

    def info(self) -> str:
        if is_active == True:
            return f'{self.username} foydalanuvchi faol:'
        else:
            return f'{self.username} foydalanuvchi no faol:'

            
S01 = user('ali', 'dgfs', True)
print(S01.info())