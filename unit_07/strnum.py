#-----------------------------
# For demo purposes only - the StrNum class is superfluous in this
# case as plain strings would give the same result.
class StrNum:
    def __init__(self, value):
        self.value = value

    def __cmp__(self, other):  # both <=> and cmp
        # providing <=> gives us <, ==, etc. for free.
        # __lt__, __eq__, and __gt__ can also be individually specified
        return cmp(self.value, other.value)

    def __str__(self):  # ""
        return self.value

    def __nonzero__(self, other):   # bool
        return bool(self.value)

    def __int__(self, other):   # 0+
        return int(self.value)

    def __add__(self, other):   # +
        return StrNum(self.value + other.value)

    def __radd__(self, other):   # +, inverted
        return StrNum(other.value + self.value)

    def __mul__(self, other):   # *
        return StrNum(self.value * other)

    def __rmul__(self, other):   # *, inverted
        return StrNum(self.value * other)


def demo():
    # show_strnum - demo operator overloading
    x = StrNum("Red")
    y = StrNum("Black")
    z = x + y
    r = z * 3
    print "values are %s, %s, %s, and %s" % (x, y, z, r)
    if x < y:
        s = "LT"
    else:
        s = "GE"
    print x, "is", s, y

if __name__ == "__main__":
    demo()
# values are Red, Black, RedBlack, and RedBlackRedBlackRedBlack
# Red is GE Black
