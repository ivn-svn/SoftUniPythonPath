class User:
    def __init__(self, username: str, age: int):
        self.username = []
        self.age = []
        self.movies_liked = []
        self.movies_owned = []


    def __str__(self):
        movies_liked_str = 'No movies liked.'
        if self.movies_liked:
            movies_liked_str = os.linesep.join(m.details() for m in self.movies_liked)
            movies_owned_str = 'No movies owned.'
        if self.movies_owned:
            movies_owned_str = os.linesep.join(m.details() for m in self.movies_owned)
        return f'Username: {self.username}, Age: {self.age}' \
            "Liked movies:" \
            f'{movies_liked_str}' \
            "Owned movies:" \
            f'{movies_owned_str}'
