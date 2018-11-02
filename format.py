out = open(r'H:\Documents\league\output.txt', 'w')

with open(r'H:\Documents\league\t.txt', encoding='utf-8') as f:
    while(True):
        line = f.readline()
        if line == '':
            break

        print(line, file = out)