class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pohni(self):
        self.y += 25


bod = Bod(200, 50)
bod2 = Bod(300, 100)

print(bod.x, bod.y)
print(bod2.x, bod2.y)

bod.pohni()
print(bod.x, bod.y)
print(bod2.x, bod2.y)
