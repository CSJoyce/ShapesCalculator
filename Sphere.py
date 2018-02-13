class Sphere(object):
    def __init__(self):
        self.radius = 0
    def volume(self):
        vol = 4/3 * 3.14 * self.radius**3
        print("The volume for your sphere: ", vol)
