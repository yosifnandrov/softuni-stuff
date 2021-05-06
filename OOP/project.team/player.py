class Player:

    def __init__(self,name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self,new_value):
        self.__endurance = new_value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self,new_value):
        self.__sprint = new_value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self,new_value):
        self.__dribble = new_value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self,new_value):
        self.__passing = new_value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self,new_value):
        self.__shooting = new_value

    def __str__(self):
        return f"Player: {self.__name}\n" \
               f"Endurance: {self.__endurance}\n" \
               f"Sprint: {self.__sprint}\n" \
               f"Dribble: {self.__dribble}\n" \
               f"Passing: {self.__passing}\n" \
               f"Shooting: {self.__shooting}\n" \
