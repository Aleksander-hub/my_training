
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    __file_name = 'products.txt'

    def __init__(self):
        open(self.__file_name, 'a').close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = {}
        file_content = self.get_products()
        lines = []
        index = 0

        while index < len(file_content):
            line_end = file_content.find('\n', index)
            if line_end == -1:
                lines.append(file_content[index:])
                break
            lines.append(file_content[index:line_end])
            index = line_end + 1

        for line in lines:
            if line:
                existing_products[line[:line.find(',')]] = True

        for product in products:
            product_name = product.name
            if product_name in existing_products:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f"{product}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # str
s1.add(p1, p2, p3)
print(s1.get_products())
