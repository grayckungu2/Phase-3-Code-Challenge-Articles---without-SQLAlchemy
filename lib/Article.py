

# Object oriented program 

class Article:
    _all = []
#set an attributes  of the class
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all.append(self)
#
    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls._all

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
    


