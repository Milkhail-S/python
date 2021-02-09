f_name = 't6.txt'

dial = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
}

new = {}
with open(f_name, 'r', encoding='utf-8') as fi:
    for line in fi:
        letters = list(line)
        cifry = str()
        for d in letters:
            if dial.get(d) is not None:
                cifry += str(dial.get(d))
            else:
                cifry += ' '
                continue
        dgt = cifry.split()
        dgts = [int(i) for i in dgt]
        print(dgts)
        new.update({line[:line.index(':')]: sum(dgts)})
    print(new)
