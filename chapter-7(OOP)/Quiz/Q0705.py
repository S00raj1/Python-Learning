
class Rectangle:
    length = 50
    width = 40
    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length*self.width


    def length_of_diagonal(self):
        return (self.length**2 + self.width**2)**(1/2)

class Circle:
    radius = 50
    pi = 3.14
    def circumferences(self):
        return self.radius*self.pi*2
    def area_of_circle(self):
        return self.pi*(self.radius**2)
    def diameter(self):
        return self.radius*2

class Box:
    length = 5
    breadth = 10
    height = 15
    def surface_area(self):
        return 2*self.length+2*self.height+2*self.breadth

    def volume(self):
        return self.height*self.length*self.breadth


r = Rectangle()
print('The perimeter of rectangle is',r.perimeter())
print('The area of rectangle is',r.area())
print('The length of diagonal is',r.length_of_diagonal())

c = Circle()
print('The area of circle is ',c.area_of_circle())
print('The circumference of circle is',c.circumferences())
print('The diameter of circle is ',c.diameter())

b = Box()
print('The surface area of box is ',b.surface_area())
print('The volume of box is',b.volume())