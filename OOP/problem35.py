class Ride:
    def fare(self, distance):
        print("Calculating fare")


class BikeRide(Ride):
    def fare(self, distance):
        print("Bike Fare:", distance * 5)


class CarRide(Ride):
    def fare(self, distance):
        print("Car Fare:", distance * 10)


class AutoRide(Ride):
    def fare(self, distance):
        print("Auto Fare:", distance * 7)


# Usage
rides = [BikeRide(), CarRide(), AutoRide()]

for r in rides:
    r.fare(10)