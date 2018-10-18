class Tracer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # return 2
        try:
            (instance.__dict__[self.name])
        except KeyError:
            self.__set__(instance, 2)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("delete")

class A:
    # x = 4
    x = Tracer('x')

    def __init__(self):
        # self.__dict__['x'] = 3
        # self.x = 3
        pass

    def __getattr__(self, name):
        return 5

    # def __getattribute__(self, name):
    #     return 1


# # # # #

a = A()

print("a.__dict__ => {}".format(a.__dict__))
print("a.__class__.__dict__ => {}".format(a.__class__.__dict__))

print("a.x is {}".format(a.x))


A.x = 4  # A.__dict__['x'] = 4 / a.__class__.__dict__['x'] = 4
print("a.x is {}".format(a.x))
del(A.x)
print("a.x is {}".format(a.x))

a.x = 3  # a.__dict__['x'] = 3
print("a.x is {}".format(a.x))

print("a.__dict__ => {}".format(a.__dict__))
print("a.__class__.__dict__ => {}".format(a.__class__.__dict__))