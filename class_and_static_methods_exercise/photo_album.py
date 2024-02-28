from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for row in range(self.pages):
            if len(self.photos[row]) < 4:
                slot = len(self.photos[row]) + 1
                page = row + 1
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {page} slot {slot}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += ("[] " * len(page)).rstrip() + "\n"
            result += "-----------\n"
        return result.rstrip()


