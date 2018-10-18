import sys
import traceback as tb # see pymotw.com
import logging

class HappyLittleError(Exception):
    def __init__(self):
        self.message = "Bob Ross would be proud"

print(ZeroDivisionError.mro())

try:
    # open("whoops")
    # 10/0
    pass
except (ArithmeticError, IndexError):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    sys.stderr.write("{} {} {}: can you even count bruh\n".format(exc_type, str(exc_obj), exc_tb))
    sys.exit(1)
except Exception as e:
    sys.stderr.write("{}: I can't even\n".format(e))
    sys.exit(1)
finally:
    print("I'm with you till the end of the line")


class CtxMgr:
    def __init__(self, val):
        self.val = val

    def __enter__(self):
        print('enter')
        return 11

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("you're exceptional")
        print("you're exitional")


# from somewhere import CtxMgr

with CtxMgr(12) as val:
    print(val)
    print("in it to win it")
    print("in it to win it")
    # 10/0
    print("in it to win it")
    print("in it to win it")
print("that's it, I'm out")