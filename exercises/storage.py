class StoreBg:

    def __init__(self, capacity):
        self.capacity = capacity
        self.__storage = []


    def add_product(self,product):
        self.product = product
        if len(self.__storage) < self.capacity:
            self.__storage.append(self.product)


    def get_products(self):
         return f"{self.__storage}"

storage = StoreBg(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())