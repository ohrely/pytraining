from day2.muppet import Muppet

class Monster(Muppet):
    def __init__(self, name, obsession):
        super().__init__(name)
        super().sway(-130)
        self._obsession = obsession

    def sway(self, offering):
        if offering == self._obsession:
            print("{}: Thank you for the {}!".format(self.name, offering))
            super().sway(200)
        else:
            print("{}: I hate {}!  Bring me {}!".format(self.name, offering, self._obsession))
            super().sway(-20)


print("")
cookie = Monster("Cookie Monster", "cookies")

cookie.sway("love")
cookie.sway("cookies")