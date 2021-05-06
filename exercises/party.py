class Persona:
    def __init__(self, name):
        self.name = name



class PartyAnimal:
    def __init__(self):
        self.people = []

    def invite_to_party(self, person):
        self.people.append(person)

    def names_of_attendees(self):
        return ", ".join([person.name for person in self.people])

    def number_of_people(self):
        return len(self.people)

party = PartyAnimal()
name = input()
while not name == "End":
    person = Persona(name)
    party.invite_to_party(person)
    name = input()
print(f"Going: {party.names_of_attendees()}")
print(f"Total: {party.number_of_people()}")

