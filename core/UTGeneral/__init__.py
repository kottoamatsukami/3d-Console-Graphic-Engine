import math


class Vector3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_cords(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def set_cords(self, new_x: float, new_y: float, new_z: float) -> None:
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def get_unit_vector(self) -> tuple[float, float, float]:
        return self / math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise ValueError("Unsupported mult operation for Vector3D and {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x / other, self.y / other, self.z / other)
        else:
            raise ValueError("Unsupported div operation for Vector3D and {}".format(type(other)))

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Unsupported add operation for Vector3D and {}".format(type(other)))

    def __repr__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def get_cords(self) -> tuple[float, float]:
        return (self.x, self.y)

    def set_cords(self, new_x: float, new_y: float) -> None:
        self.x = new_x
        self.y = new_y

    def get_unit_vector(self) -> tuple[float, float]:
        return self / math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise ValueError("Unsupported mult operation for Vector2D and {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x / other, self.y / other)
        else:
            raise ValueError("Unsupported div operation for Vector2D and {}".format(type(other)))

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Unsupported add operation for Vector2D and {}".format(type(other)))

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"
