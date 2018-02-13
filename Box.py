class Box(object):
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
    def volume(self):
        vol = self.length * self.width * self.height
        print("The volume for your box: ", vol)
    def surfArea(self):
        sArea = 2*self.length * self.width + 2*self.length * self.height + 2*self.width * self.height
        print("The surface area for your box: ", sArea)
