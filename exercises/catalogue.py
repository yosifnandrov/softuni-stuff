class Catalogue:

    def __init__(self, name):
        self.name = name
        self.__products = []

    def add_product(self, product):
        self.product = product
        self.__products.append(product)

    def get_by_letter(self,first_letter):
        #sorted_products = []
        return [el for el in self.__products if el.startswith(first_letter)]

        # for prdct in self.__products:
        #     for i in prdct:
        #         if i == first_letter:
        #             sorted_products.append(prdct)
        # return sorted_products

    def __repr__(self):
        joined_list = "\n".join(sorted(self.__products))
        return f"Items in the {self.name} catalogue:\n{joined_list}"

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)



