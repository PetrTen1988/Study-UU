class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        print(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    __file_name = 'Products.txt'
    def get_products(self):
        file = file.pprint(name, 'r')





# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
# p1.__str__()
# p2.__str__()
# p3.__str__()