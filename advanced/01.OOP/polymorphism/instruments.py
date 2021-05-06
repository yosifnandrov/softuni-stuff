from abc import ABC, abstractmethod


class Instruments(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument:Instruments):
    return instrument.play()


class Guitar(Instruments):
    def play(self):
        return "playing guitar"

guitar = Guitar()

print(play_instrument(guitar))