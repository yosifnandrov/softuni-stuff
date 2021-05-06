class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "birds":
            self.birds.append(name)
        self.__animals += 1


    def get_info(self, species):
        zoo_name = self.name
        if species == "mammal":
            names = ", ".join(self.mammals)
            print(f"{species.capitalize()}s in {zoo_name}: {names}")
        elif species == "fish":
            names = ", ".join(self.fish)
            print(f"{species.capitalize()}es in {zoo_name}: {names}")
        elif species == "birds":
            names = ", ".join(self.fish)
            print(f"{species.capitalize()}s in {zoo_name}: {names}")

    def get_total_animals(self):
        return f'Total animals: {self.__animals}'

zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, name = input().split(" ")
    zoo.add_animal(species, name)

species = input()
zoo.get_info(species)
print(zoo.get_total_animals())
