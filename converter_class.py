#Convert kilometers to miles
class Converter:
    def __init__(self, km):
        self.km = km
    def to_miles(self):
        return self.km / 1.609

#convert 3 kilometers to miles
distance1 = Converter(3)
print(distance1.to_miles())