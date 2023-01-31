from core.UTGeneral import Vector3D, Vector2D

class ViewPort:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cords = Vector3D(0, 0, 0)
        self.rotation = Vector2D(0, 0)

    def set_cords(self, x: float, y: float, z: float):
        self.cords = Vector3D(x, y, z)

    def move_cords(self, dx: float, dy: float, dz: float):
        self.cords = self.cords + Vector3D(dx, dy, dz)

    def set_rotate(self, angle_horizontal: float, angle_vertical: float):
        self.rotation = Vector2D(angle_horizontal, angle_vertical)

    def rotate(self, d_horizontal: float, d_vertical: float):
        self.rotation = self.rotation + Vector2D(d_horizontal, d_vertical)
        self.__normalize_rotation()

    def __normalize_rotation(self):
        self.rotation = Vector2D(self.rotation.x % 360, self.rotation.y % 360)
