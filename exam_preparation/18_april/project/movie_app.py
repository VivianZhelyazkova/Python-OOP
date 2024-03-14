from project.user import User
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        new_user = User(username, age)
        found_user = next((user for user in self.users_collection if user.username == username), None)
        if found_user:
            raise Exception("User already exists!")
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def validate_movie_owner(self, username: str, movie: Movie):
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def upload_movie(self, username: str, movie: Movie):
        user_found = next((user for user in self.users_collection if user.username == username), None)
        if not user_found:
            raise Exception("This user does not exist!")
        self.validate_movie_owner(username, movie)
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        self.validate_movie_owner(username, movie)
        movie.update(kwargs)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        self.validate_movie_owner(username, movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        current_user = next(user for user in self.users_collection if user.username == username)
        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = next(user for user in self.users_collection if user.username == username)
        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        current_user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = list(sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title)))
        result = ""
        for movie in sorted_movies:
            result += movie.details() + "\n"
        return result.rstrip()

    def __str__(self):
        if not self.users_collection:
            result = "All users: No users.\n"
        else:
            usernames = ", ".join(user.username for user in self.users_collection)
            result = f"All users: {usernames}\n"
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            titles = ", ".join(movie.title for movie in self.movies_collection)
            result += f"All movies: {titles}"
        return result
