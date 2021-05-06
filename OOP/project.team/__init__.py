from project_animals.player import Player
from project_animals.team import Team

t = Team("Best", 10)
p = Player("Pall", 3, 3, 3, 3, 3)
t.add_player(p)
print(t.remove_player("Pall"))
print(p)