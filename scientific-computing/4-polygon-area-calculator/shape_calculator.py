class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_str_title(self):
        return __class__.__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def get_picture(self):
        ret = ""
        ret = ret + self.get_str_title() + "\n"
        for i in range(0, self.height):
            is_last = i == self.height - 1
            for j in range(0, self.width):
                ret += "*"
            if not is_last:
                ret += "\n"
        return ret

    def get_amount_inside(self, rect):
        return int(self.get_width()/rect.get_width()) * int(self.get_height()/rect.get_height())


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)

    def get_str_title(self):
        return __class__.__name__ + "(side=" + str(self.height) + ")"

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

