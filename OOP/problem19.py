class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

obj = MyList([10, 20, 30])
print(obj[1])
