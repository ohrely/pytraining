import json

class AutoSave:
    def __init__(self, data):
        self.data = data
        self.path = "data.sav"

    def __enter__(self):
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        fo = open(self.path, "wt")
        json.dump(self.data, fo)
        fo.close()


##==== from lib import AutoSave
dict = {}

with AutoSave(dict) as team:
    dict['arthur']  = 'die'
    dict['eames']   = 'chip'
    dict['ariadne'] = 'bishop'

fo = open(team)
print(json.load(fo))



# --------

from contextlib import contextmanager
import sys

@contextmanager
def stdout_redirected(new_stdout):
    save_stdout = sys.stdout
    sys.stout = new_stdout
    yield
    sys.stdout = save_stdout

with open("temp.txt", "w") as fobj:
    with stdout_redirected(fobj):
        print("helloooo")
    print("back again")

