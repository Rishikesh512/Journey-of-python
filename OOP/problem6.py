class Annimal :
    name ="Lion"

    def __init__(self,age):
        self.age = age
    def show(self):
        print("how are you")
    
    @classmethod
    def hello(cls):
        print("How are you brother")

    @staticmethod
    def static():
        print("how are you")





obj = Annimal(12)

obj.hello()

obj.static()