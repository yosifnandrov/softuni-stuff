from typing import List


class PhotoAlbum:
    pages: int
    photos: List

    def __init__(self,pages:int):
        self.pages = pages
        self.photos = [
            []
            for _ in range(pages)
        ]

    @classmethod
    def from_photos_count(cls,photos_count:int):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self,label:str) -> str:
        for index,page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free spots"

    def display(self):
        display = f'\n{11*"-"}\n'.join([' '.join(["[]" if photo else '\n' for photo in page]) for page in self.photos])
        start = 11*"-" + '\n'
        end = '\n' + 11*"-" + '\n'
        return start + display + end


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
