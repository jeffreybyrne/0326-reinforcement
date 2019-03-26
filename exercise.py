class Location:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Trip:

    def __init__(self):
        self.stops = []

    def addStop(self, location):
        self.stops.append(location)

    def listRoute(self):
        print("Began trip.")
        for num in range(1, len(self.stops)):
            print(f"Travelled from {self.stops[num-1]} to {self.stops[num]}.")
        print("Ended trip.")


tdot = Location('Toronto')
odot = Location('Ottawa')
mdot = Location('Montreal')
qdot = Location('Quebec City')
hdot = Location('Halifax')
sdot = Location("St. John's")
myTrip = Trip()
myTrip.addStop(tdot)
myTrip.addStop(odot)
myTrip.addStop(mdot)
myTrip.addStop(qdot)
myTrip.addStop(hdot)
myTrip.addStop(sdot)
myTrip.listRoute()
