class Polynom:
    def __init__(self):
        self._coefs_dict = {}

    def get_power(self):
        return self._coefs_dict.keys()

    def get_coef(self, pwr):
        return self._coefs_dict.get(pwr, 0)

    def _process_line(self, line):
        line = line.strip()
        if not line:
            return True

        data = line.split()
        if len(data) != 2:
            print('Incorrect format:', line)
            return False

        try:
            pwr = int(data[0])
            coef = float(data[1])
        except (ValueError, TypeError):
            print('Incorrect data format:', line)
            return False

        self._coefs_dict[pwr] = coef
        return True

    def read_from_file(self, file_name):
        self._coefs_dict = {}
        try:
            with open(file_name) as f:
                for line in f:
                    self._process_line(line)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print("Error while reading from file:", e)

    def read_from_keyboard(self):
        self._coefs_dict = {}
        print("Input powers & coefficients, one pair per line, or empty line to stop")
        while True:
            s = input()
            if not s:
                break
            self._process_line(s)

    def set_coefs(self, poly):
        self._coefs_dict = poly

    def evaluate_at_point(self, x):
        result = 0
        for pwr, coef in self._coefs_dict.items():
            term = x ** pwr * coef
            result += term
        return result

    def show(self):
        print(self._coefs_dict)

    def add(self, poly1, poly2):
        powers1 = poly1.get_power()
        powers2 = poly2.get_power()
        poly = {}
        for pwr in set(powers1) | set(powers2):
            poly[pwr] = poly1.get_coef(pwr) + poly2.get_coef(pwr)
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom

    def subtract(self, poly1, poly2):
        powers1 = poly1.get_power()
        powers2 = poly2.get_power()
        poly = {}
        for pwr in set(powers1) | set(powers2):
            poly[pwr] = poly1.get_coef(pwr) - poly2.get_coef(pwr)
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom

    def multiply(self, poly1, poly2):
        poly = {}
        for pwr1, coef1 in poly1._coefs_dict.items():
            for pwr2, coef2 in poly2._coefs_dict.items():
                new_pwr = pwr1 + pwr2
                new_coef = coef1 * coef2
                if new_pwr in poly:
                    poly[new_pwr] += new_coef
                else:
                    poly[new_pwr] = new_coef
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom


if __name__ == "__main__":
    obj = Polynom()
    obj.read_from_file('input01.txt')

    obj2 = Polynom()
    obj2.read_from_file('input02.txt')

    print("Polynom 1:")
    obj.show()
    print("Polynom 2:")
    obj2.show()

    sum_poly = obj.add(obj, obj2)

    diff_poly = obj.subtract(obj, obj2)

    product_poly = obj.multiply(obj, obj2)

    x = float(input("Enter a value for x: "))

    q_value = sum_poly.evaluate_at_point(x)
    h_value = product_poly.evaluate_at_point(x)
    print("Value of q(x):", q_value)
    print("Value of h(x):", h_value)

    with open("output.txt", "w") as f:
        f.write(str(q_value) + "\n")
        f.write(str(h_value) + "\n")

    print("Sum of Polynomials:")
    sum_poly.show()

    print("Difference of Polynomials:")
    diff_poly.show()

    print("Product of Polynomials:")
    product_poly.show()
