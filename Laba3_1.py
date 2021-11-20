import math

class Sphere:

    def __init__(self, rad=1, x_sph=0, y_sph=0, z_sph=0):  # конструктор
        self.rad = rad
        self.x_sph = x_sph
        self.y_sph = y_sph
        self.z_sph = z_sph
        print("radius =", rad, "  x =", x_sph, "  y =", y_sph, "  z =", z_sph)

    def get_volume(self):
        return round(4/3*math.pi*(self.rad**3), 3)

    def get_square_(self):
        return round(4*math.pi*(self.rad**2), 3)

    def get_radius_(self):
        return self.rad

    def get_center_(self):
        center = (self.x_sph, self.y_sph, self.z_sph)
        return center

    def set_radius_(self, rad_new):
        self.rad = rad_new

    def set_center(self, x_new, y_new, z_new):
        self.x_sph = x_new
        self.y_sph = y_new
        self.z_sph = z_new

    def is_point_inside(self, x, y, z):
        if (self.x_sph - x)**2 + (self.y_sph - y)**2 + (self.z_sph - z)**2 < self.rad**2: return True
        else: return False

# Main Начало
radius = 10
x_sphere = 1
y_sphere = 1
z_sphere = 1
Object_1 = Sphere(radius, x_sphere, y_sphere, z_sphere)
Object_2 = Sphere()
print("")
print("Volume =", Object_1.get_volume())
print("Square =", Object_1.get_square_())
print("Radius =", Object_1.get_radius_())
print("Center =", Object_1.get_center_())
radius_new = int(input("Enter radius: "))
Object_1.set_radius_(radius_new)
print("Radius =", Object_1.get_radius_())
x_new = int(input("Enter x: "))
y_new = int(input("Enter y: "))
z_new = int(input("Enter z: "))
Object_1.set_center(x_new, y_new, z_new)
print("Center =", Object_1.get_center_())
x_point = int(input("Enter point x: "))
y_point = int(input("Enter point y: "))
z_point = int(input("Enter point z: "))
print(Object_1.is_point_inside(x_point, y_point, z_point))
# Main Конец