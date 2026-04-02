class DataPack:
    def __init__(self):
        self.data = 0   # in MB

    def recharge_data(self, mb):
        self.data += mb
        print("Data added:", mb)

    def use_data(self, mb):
        if mb > self.data:
            print("Not enough data")
        else:
            self.data -= mb
            print("Data used:", mb)

    def check_data(self):
        return self.data


d = DataPack()
d.recharge_data(1000)
d.use_data(300)
print("Remaining Data:", d.check_data())
