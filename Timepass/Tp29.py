class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def make_call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    pass

s = SmartPhone()
s.take_photo()
s.make_call()
