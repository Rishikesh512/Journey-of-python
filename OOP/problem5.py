class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zip = zips
        self.pockets = pockets

    def show(self):
        print("Your object details are :-{self.material},{self.zips},{self.pockets}")


reebok = Factory("Lather",3,4)
campus = Factory("Nylon",5,6)
skybags = Factory("Jeans",3,6)

reebok.show()
campus.show()


