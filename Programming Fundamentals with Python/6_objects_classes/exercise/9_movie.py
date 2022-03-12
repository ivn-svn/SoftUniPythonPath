class Movie:
    def __init__(self, name, director, watched=False):
        self.name = name
        self.director = director
        self.watched = watched
        self._watched_movies = []
        self.num_watched = 0

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        self.watched = True
        self.num_watched += 1
        if self.name not in self._watched_movies:
            self._watched_movies.append(self.name)

    def __repr__(self):
        return "Movie name: {}; Movie director: {}. Total watched movies: {}".format(self.name, self.director,
                                                                                     self.num_watched)


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
