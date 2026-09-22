class Animals: 
    pass
class Pets(Animals):
    pass
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow Bow !!")

d = Dogs()
d.bark()