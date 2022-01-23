class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes