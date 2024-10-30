class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

c = Product('codetree', 50)
name, code = tuple(input().split())
b = Product(name, code)

print('product {} is {}'.format(c.code, c.name))
print('product {} is {}'.format(b.code, b.name))