# Photo Album
# 100%
# https://docs.google.com/document/d/1-tatQyAyZFcvR50r8NVYFpkZfCIyXGz2/edit?usp=sharing&ouid=105748105946982460404&rtpof=true&sd=true
# Judge link:
# https://judge.softuni.org/Contests/Practice/Index/2431#0
# Submission link:
# https://judge.softuni.org/Contests/Submissions/View/31773540


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = abs(pages)
        self.photos_original = [[None for j in range(4)] for y in range(pages)]
        self.photos = [[i for i in k if i is not None] for k in self.photos_original]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # - creates a new instance of PhotoAlbum. Note:
        # Each page can contain 4 photos.
        pages = photos_count // 4 + (photos_count % 4 != 0)
        return cls(pages)

    def add_photo(self, label: str):  # - adds the photo in the first possible page and slot and
        success = False
        row_ctr = 0
        col_ctr = 0
        for row_ctr, row in enumerate(self.photos_original):
            for col_ctr, col in enumerate(row):
                if col == None:
                    self.photos_original[row_ctr][col_ctr] = label
                    success = True
                    self.photos = [[k for k in i if k is not None] for i in self.photos_original]
                    break
            if success:
                break
        page_number = row_ctr + 1
        slot_number = col_ctr + 1
        if success:
            return f"{label} photo added successfully on page {page_number} slot {slot_number}"
        else:
            # If there are no free slots left
            return "No more free slots"

    def display(self):
        # - returns a string representation of each page and the photos in it. Each photo is marked with "[]", and the page separation is made using 11 dashes (-).
        return self.__repr__()

    def __repr__(self):
        dashes = 11 * "-"
        str_repr = dashes + "\n"
        for row_ctr, row in enumerate(self.photos):
            for col_ctr, col in enumerate(row):
                str_repr += "[]"
                if col_ctr + 1 != len(row):
                    str_repr += " "
            if row_ctr + 1 != len(self.photos):
                str_repr += "\n" + dashes + "\n"
            else:
                str_repr += "\n" + dashes
        return str_repr


album = PhotoAlbum(2)

#
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.photos)
print(album.add_photo("wedding"))
print(album.photos)
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.display())

# Code keeps giving only 71% in the automated Judge test system.