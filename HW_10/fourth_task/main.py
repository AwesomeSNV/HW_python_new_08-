# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def type_check(self):

        if self.side_a >= self.side_b+self.side_c or self.side_b >= self.side_a+side_c or self.side_c >= self.side_b+self.side_a:
            result = "Треугольник не существует"

        else:
            result = "Треугольник существует"
            if self.side_a == self.side_b == self.side_c:
                result = "Треугольник равносторонний"
            elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_c == self.side_b:
                result = "Треугольник равнобедренный"

        return result


def input_parametr(str_param):
    while True:
        param = input("Введите длину стороны  {} : ".format(str_param))
        try:
            param = float(param)
        except:
            print("{} должно быть числом".format(str_param))
        else:
            if param > 0:
                return param
            else:
                print("{} должно быть положительным числом".format(str_param))

print("Введите стороны треугольника а, b, c")

side_a = input_parametr("а")
side_b = input_parametr("b")
side_c = input_parametr("c")

print(Triangle(side_a, side_b, side_c).type_check())