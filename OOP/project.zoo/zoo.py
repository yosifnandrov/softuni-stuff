from typing import List


class Zoo:
    animal_capacity : int
    workers_capacity : int
    budget :int
    name:str
    animals: List
    workers: List

    def __init__(self,name:str,budget:int,animal_capacity:int,workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self,animal,price:int):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self,worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if type(animal).__name__ == "Lion"]
        tigers = [animal for animal in self.animals if type(animal).__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if type(animal).__name__ == "Cheetah"]
        lions_info = '\n'.join([lions[i].__repr__() for i in range(len(lions))])
        tigers_info = '\n'.join([tigers[i].__repr__() for i in range(len(tigers))])
        cheetahs_info = '\n'.join([cheetahs[i].__repr__() for i in range(len(cheetahs))])
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{lions_info}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{tigers_info}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{cheetahs_info}"

    def workers_status(self):
        caretakers = [worker for worker in self.workers if type(worker).__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if type(worker).__name__ == "Vet"]
        keepers = [worker for worker in self.workers if type(worker).__name__ == "Keeper"]
        caretakers_info = '\n'.join([caretakers[i].__repr__() for i in range(len(caretakers))])
        vets_info = '\n'.join([vets[i].__repr__() for i in range(len(vets))])
        keepers_info = '\n'.join([keepers[i].__repr__() for i in range(len(keepers))])
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{keepers_info}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_info}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{vets_info}"

