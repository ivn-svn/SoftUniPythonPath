from movie_world.project import Hero


class Wizard(Hero):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
