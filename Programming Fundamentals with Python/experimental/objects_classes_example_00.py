class User:
    pass
user1 = User()
user1.first_name = 'User' # If there are more than 1 words within a field name, put them between underscores.
user1.last_name = 'Userov'
print(user1.last_name, user1.first_name)

class SelfUser:
    def __int__(self, full_name, birthday): # using the constructor class
        self.name = full_name
        self.birthday = birthday #yyyymmdd

user = User("Dave Bowman", "19710315")