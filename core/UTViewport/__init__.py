from core.UTGeneral import Vector3D, Vector2D
import math

class ViewPort:
    def __init__(self, width, height, view_angle):
        self.width = width
        self.height = height
        self.view_angle = view_angle
        self.cords = Vector3D(0, 0, 0)
        self.rotation = Vector2D(0, 0)
        self.charset = {
            "circles_and_squares": { # Test Set
                "0" : " ",
                "1" : "◦",
                "2" : "▫",
                "3" : "▪",
                "4" : "⦿",
                "5" : "●",
                "6" : "■",
            },
            "vertical_boxes":{ # Test Set
                "0": " ",
                "1": "░",
                "2": "▒",
                "3": "▓",
                "4": "█",
            }
        }

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

    def get_unit_rotate(self):
        return Vector3D(
            x=math.cos(math.radians(self.rotation.x))*math.cos(math.radians(self.rotation.y)),
            y=math.sin(math.radians(self.rotation.x))*math.cos(math.radians(self.rotation.y)),
            z=math.sin(math.radians(self.rotation.y)),
        )

    def render(self, objects):
        # Make surface
        direction = self.get_unit_rotate()
        A = direction.x
        B = direction.y
        C = direction.z
        D = min(
            -(
                    (self.width/2)*math.tan(math.radians(self.view_angle/2)) + A*self.cords.x+B*self.cords.y+C*self.cords.z
            ),
            (
                    (self.width/2)*math.tan(math.radians(self.view_angle/2)) + A*self.cords.x+B*self.cords.y+C*self.cords.z
            ),
        ),
        p = (A*self.cords.x+B*self.cords.y+C*self.cords.z + D)/(A**2 + B**2 + C**2)
        projection = Vector3D(
            x=self.cords.x - p*A,
            y=self.cords.y - p*B,
            z=self.cords.z - p*C,
        )
