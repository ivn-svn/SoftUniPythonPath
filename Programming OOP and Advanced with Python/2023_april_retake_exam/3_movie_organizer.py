def movie_organizer(*movies):
    genres = {}
    for movie in movies:
        name, genre = movie
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(name)

    output = []
    for genre, movies in sorted(genres.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{genre} - {len(movies)}")
        for movie in sorted(movies):
            output.append(f"* {movie}")

    return "\n".join(output)
