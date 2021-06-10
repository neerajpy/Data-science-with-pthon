def find(l,s):
    for pos,t in enumerate(l):
        if t==s:
            return (f'{pos},{t}')
    return -1

l1 = ['abc', 'abcdef', 'neeraj']
print(find(l1,'bcdef'))
