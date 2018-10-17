import os
import subprocess
from pprint import pprint

print(os.listdir('.'))
# rv = os.system('ls -l')
rv = subprocess.run('ls')
print(rv.returncode)

# rv = subprocess.run(['false'], check=True)
# rv.returncode

out = os.popen('ls -l', 'r')
print(list(out))

completed = subprocess.run(['ls', '-l'],
                           stdout=subprocess.PIPE)
print(completed.stdout.decode())

wit = os.walk('.')
dir_name, sub_dirs, files = next(wit)

pprint(dir_name)
pprint(sub_dirs)
pprint(files)
