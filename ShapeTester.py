import Box
import Pyramid
import Sphere
shape = input("Enter which shape you would like to calculate (b = box, s = sphere, or p = pyramid) : ")

if shape == "b":
    b1 = Box.Box()
    b1.length = int(input("Enter box length: "))
    b1.width = int(input("Enter box width: "))
    b1.length = int(input("Enter box length: "))
    b1.volume()
    b1.surfArea()
elif shape == "p":
    p1 = Pyramid.Pyramid()
    p1.length = int(input("Enter pyramid length: "))
    p1.width = int(input("Enter pyramid width: "))
    p1.height = int(input("Enter pyramid height: "))
    p1.volume()
elif shape == "s":
    s1 = Sphere.Sphere()
    s1.radius = int(input("Enter sphere radius: "))
    s1.volume()
    
    
