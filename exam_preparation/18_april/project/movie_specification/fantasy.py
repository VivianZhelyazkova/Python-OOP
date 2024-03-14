from project.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title: str, owner: object, year: int, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @Movie.age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self._age_restriction = value

    def details(self):
        return (f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction},"
                f" Likes:{self.likes}, Owned by:{self.owner.username}")
