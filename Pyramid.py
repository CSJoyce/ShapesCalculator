class Pyramid(object):
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
    def volume(self):
        vol = self.length * self.width * self.height * 1/3
        print("The volume for your pyramid: ", vol)
