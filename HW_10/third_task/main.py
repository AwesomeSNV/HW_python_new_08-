# Решите квадратное уравнение
# 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.

class SquareEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = None
        self.x2 = None
        self.discriminant = None
        self.text = ""

    def roots(self):
        self.x1 = None
        self.x2 = None

        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    self.text = "Уравнение имеет бесконечное число корней"
                else:
                    self.text = "Ошибка записи уравнения"
            else:
                self.x1 = self.x2 = -self.c / self.b
                self.text = f"Уравнение имеет только один корень x1= {self.x1}"
        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c
            if self.discriminant < 0:
                self.text = f"Уравнение не имеет вещественных корней"
            elif self.discriminant == 0:
                self.x1 = -b / (2 * a)
                self.text = f"Уравнение имеет только один корень x1 = {self.x1}"
            else:
                self.x1 = (-self.b + self.discriminant ** 0.5) / (2 * self.a)
                self.x2 = (-self.b - self.discriminant ** 0.5) / (2 * self.a)
                self.text = f"Первый корень уравнения x1= {self.x1}, второй корень уравнения x2= ,{self.x2}"

        return self.text, self.x1, self.x2


print("Квадратное уравнение ax^2+bx+c = 0")
a = float(input("a: "))
print("Вы ввели a=", a)
b = float(input("b: "))
print("Вы ввели b= ", b)
c = float(input("c: "))
print("Вы ввели c=", c)

print("Решаем квадратное уравнение {}x^2 + {}x + {} = 0".format(a, b, c))

text, x1, x2 = SquareEquation(a, b, c).roots()

print(text)
if x1 is None and x2 is None:
    pass
elif x2 == None:
    print(f"x1 = {x1}")
else:
    print(f"x1 = {x1}, x2 = {x2}")