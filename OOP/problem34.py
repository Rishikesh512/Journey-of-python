class LibraryItem:
    def __init__(self, title):
        self.title = title

    def getInfo(self):
        print("Library item")


class Book(LibraryItem):
    def getInfo(self):
        print(f"Book: {self.title}")


class Magazine(LibraryItem):
    def getInfo(self):
        print(f"Magazine: {self.title}")


class DVD(LibraryItem):
    def getInfo(self):
        print(f"DVD: {self.title}")


# Usage
items = [Book("Python"), Magazine("Tech Today"), DVD("Inception")]

for item in items:
    item.getInfo()