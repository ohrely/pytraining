"""
hi - loves you
bye - leaves you
"""

version = '0.1'


def hi():
    print('heya')
hi.__doc__ = 'says hello; brooks no arguments; never returns'


def how_hi():
    import dis
    dis.dis(hi)


def is_speech(word):
    if isinstance(word, str):
        print('sounds good')
    else:
        print('say wut?')


def bye():
    'says goodbye; brooks no arguments; never returns'
    print('bye')
    if version == '0.1': # check version number before going too far
        print('forever')


# So many ways to get classy

class C(object):
    pass

class D: # python 3 only!
    pass

E = type('E', (object,), {})


# Globalist monkeys jumping on the bed

monkeys = 7

def fall_off_bed():
    global monkeys
    monkeys -= 1

# Splat

def showoff(*nums):
    return sum(nums), max(nums), min(nums)

def show():
    print(showoff(list(range(1, 4))))
    print(showoff(1, 2, 3))


# Input

def dismiss():
    feedback = input("What do you think?")
    print("You may think " + feedback + ", but you're wrong.")
