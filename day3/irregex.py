import re

ip = '127.0.0.1'

octet = r'([0-9]{1,3})'
ipre = r'^{}\.{}\.{}\.{}$'.format(octet, octet, octet, octet)

compiled_ipre = re.compile(ipre)  # speeds things up when there's many many inputs

mo = compiled_ipre.search(ip)

if mo:
    print(mo)
    if all(0 <= int(group) <= 255 for group in mo.groups()):
        print('ok')

