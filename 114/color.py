import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        try:
            self.color = color
            self.rgb = COLOR_NAMES[self.color.upper()]
        except KeyError:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        if len(hex) < 6:
            raise ValueError

        hex = hex.lstrip("#")
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)

        return tuple(rgb)

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        for element in rgb:
            if not isinstance(element, int) or element < 0 or element > 255:
                raise ValueError

        return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2]).lower()

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb:
            return f"({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"
        else:
            return "Unknown"


if __name__ == "__main__":

    c = Color("white")
    print(c.rgb)