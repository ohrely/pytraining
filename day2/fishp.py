"""
Functional-ish programming in python
"""

gen = (n * 3 for n in [1,2,4,8] if n > 3)

for item in gen:
    print(item)


def salt():
    def pepper(): # inner function can't be accessed outside of this scope!
        print('pepper')
    pepper()

def xch_gen(rate):
    def calc(amt):
        return rate * amt
    return calc

usd = xch_gen(1)
eur = xch_gen(1.5)
mga = xch_gen(2000)

print(usd(20), eur(20), mga(20))