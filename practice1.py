class Plant:
    def __init__(self, spec):
        self.spec = spec


class Cactus(Plant):
    pass


basil = Plant("Ocimum basilicum")

opuntia = Cactus("Opuntia vulgaris")


print(type(basil) == object)
print(type(basil) == Cactus)
print(isinstance(opuntia, Plant))
print(isinstance(opuntia, object))
print(isinstance(basil, Plant))
print(type(opuntia) == Cactus)
print(type(opuntia) == Plant)
