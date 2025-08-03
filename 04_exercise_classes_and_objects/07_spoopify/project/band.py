from typing import List
from project.song import Song
from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):

        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):

        band_info = '\n'.join(b.details() for b in self.albums)
        return (f"Band {self.name}\n"
                f"{band_info}")

