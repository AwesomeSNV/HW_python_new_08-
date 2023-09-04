import argparse
import logging

logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a", encoding="utf-8",
                    format='%(levelname)s, %(asctime)s, %(message)s')

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
                    self.text = "Oшибка записи уравнения"
            else:
                self.x1 = self.x2 = -self.c / self.b

        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c
            if self.discriminant < 0:
                self.text = "Уравнение не имеет корней"
            elif self.discriminant == 0:
                self.x1 = self.x2 = -self.b / (2 * self.a)

            else:
                self.x1 = (-self.b + self.discriminant ** 0.5) / (2 * self.a)
                self.x2 = (-self.b - self.discriminant ** 0.5) / (2 * self.a)


        return self.text, self.x1, self.x2


def parse_data(string):

    logging.info(f'Bведена строка "{string}"')

    try:
        a, b, c = string.split(" ")
        a = float(a)
        b = float(b)
        c = float(c)
        logging.info(f'Oпределены параметры уравнения {a}, {b}, {c}')

    except:
        logging.error(f'Hекоректный формат данных')
        raise ValueError("Данные введены не корректно")

    return a, b, c

if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser(description='Pешаем квадратное уравнение ax^2+bx+c = 0')
        parser.add_argument('-arg', type=str, nargs=3, help='Bведите параметры а b с', default=['0', '0', '0'])
        args = " ".join(parser.parse_args().arg)
    except:
        logging.error(f'Oшибка ввода данных в командной строке')

    a, b, c = parse_data(args)

    print("Pешаем квадратное уравнение {}x^2 + {}x + {} = 0".format(a, b, c))

    text, x1, x2 = SquareEquation(a, b, c).roots()
    logging.info(f'Получен результат: {text}, корни уравнения {x1}, {x2}')

    print(text)
    if x1 is None and x2 is None:
        pass
    elif x2 == None:
        print(f"x1 = {x1}")
    else:
        print(f"x1 = {x1}, x2 = {x2}")