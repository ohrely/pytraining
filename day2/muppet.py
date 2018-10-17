class Muppet:
    population = 0

    def __init__(boop, name):
        boop.__dict__['name'] = name
        boop.is_puppet = True
        boop._past_loves = [100]
        Muppet.population += 1

    def __gt__(self, other):
        return self.love > other.love

    @staticmethod
    def get_population():
        return Muppet.population

    def seek_affection(beep):
        print("You: Do you love me?")
        if beep.love < 50:
            print("{}: noooOOOooOOooOOOOooooo".format(beep.name))
            return False
        else:
            print("{}: Yeah".format(beep.name))
            return True

    def sway(bump, sway):
        bump._past_loves.append(sway)

    def introspect(bruh, time):
        return bruh._past_loves[time]

    @property
    def love(blog):
        return sum(blog._past_loves)

    @love.setter
    def love(blip, sway):
        print("{}: Nice try, I now love you {} less".format(blip.name, sway))
        blip.sway(-abs(sway))

    @love.deleter
    def love(blah):
        raise Exception("Love never dies")

kermit = Muppet("Kermit")

print("\n{}: Hello, I am {}".format(kermit.name, kermit.name))
print("{}: You say I am a puppet - this is {}\n".format(kermit.name, kermit.is_puppet))

assert kermit.name == "Kermit"
assert kermit.is_puppet

assert kermit.seek_affection()
kermit.sway(20)
assert kermit.seek_affection()
kermit.sway(-80)
assert not kermit.seek_affection()
kermit.sway(200)
assert kermit.seek_affection()

assert kermit.introspect(0) == 100
assert kermit.introspect(2) == -80
assert kermit.introspect(-1) == 200

assert Muppet.get_population() == 1

ernie = Muppet("Ernie")
bert = Muppet("Bert")

print("\n{} + {}: Hello, we are {} and {}".format(ernie.name, bert.name, ernie.name, bert.name))
assert Muppet.get_population() == 3

assert kermit > ernie


