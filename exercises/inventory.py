class Inventory:
    __capacity = 0
    items = []
    capacity_left = __capacity - len(items)
    def __init__(self, capacity):
        self.__capacity = capacity

    def add_item(self, item):
        if len(self.items) < self.__capacity:
         self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity_left}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)