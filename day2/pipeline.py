while True:
    line = input()
    if 'BB' in line:
        val = line.split('.')[-1]
        if '0' in val:
            print(val)