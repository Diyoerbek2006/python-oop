class user:
    def __init__(self, username: str, email: str, is_active: bool) -> None:
        self.username = username
        self.email = email
        self.is_active = is_active

    def info(self) -> str:
        return f'username: {self.username} \nemail: {self.email} \nis_active: {self.is_active}'

S01 = user('ali', 'dgfs', True)
print(S01.info())