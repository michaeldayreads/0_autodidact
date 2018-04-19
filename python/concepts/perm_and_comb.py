# from https://www.youtube.com/watch?v=hqijNdQTBH8

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x] +p)
        return l


def perm2(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm2(xs):
                yield [x] + p


data = list('abcdefghi')
print('perm1')
for p in perm1(data):
    print(p)

input('type enter to continue...')

print('perm2')
for p in perm2(data):
    print(p)
