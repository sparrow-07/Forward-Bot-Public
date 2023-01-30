class Message:
    def __init__(self, id=None, text=None, photo=None):
        self.__id = id
        self.__text = text
        self.__photo = photo

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @property
    def photo(self):
        return self.__photo
