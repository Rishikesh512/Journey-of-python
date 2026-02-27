class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class MahurFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(MahurFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        
obj = PuneFactory("Leather",2,"Black",4)

print(obj.material)
print(obj.zips)
print(obj.color)
print(obj.pockets)
