import math


class PhotoAlbum:
    PAGE_SIZE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        '''Mathematical rounding when dividing by 4.
            Takes the upper integer.'''
        pages = math.ceil(photos_count / cls.PAGE_SIZE)
        return cls(pages)

    def add_photo(self, label: str):
        for photo in range(len(self.photos)):
            page = self.photos[photo]
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {photo + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = [11 * '-']
        for page in self.photos:
            photo = ' '.join(["[]"] * len(page))

            result.append(photo)
            result.append(11 * '-')
        result = '\n'.join(result)
        return result
