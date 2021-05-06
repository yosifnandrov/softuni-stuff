from typing import List


class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.group = None

    def __str__(self):
        #if self.group is not None:
            #return f"Person {self.group.index(self)}: {self.name} {self.surname}"
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name,other.surname)


class Group:
    name:str
    people:List[Person]

    def __init__(self,name,people):
        self.name = name
        self.people = people
        # for p in self.people:
        #     p.group = self.people

    def __str__(self):
        members_info = ', '.join([f"{p.name} {p.surname}" for p in self.people])
        return f"Group {self.name} with members {members_info}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item].name} {self.people[item].surname}"

    def __add__(self, other):
        new_group_people = self.people + other.people
        return Group(self.name,new_group_people)

    def __len__(self):
        return len(self.people)

    # def people_in_group(self):
    #     for p in self.people:
    #         p.group = self.people


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(p4.group)
print(len(first_group))
print(second_group)
print(third_group[0])
print(len(third_group))
for person in third_group:
    print(person)