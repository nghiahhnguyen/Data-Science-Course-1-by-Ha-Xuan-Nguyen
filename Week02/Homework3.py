def uppercase(l):
    for i in range(len(l)):
        l[i] = l[i][0].upper() + l[i][1:]


s = 'the output that tells you if the object is the type you think or not'
l = s.split(' ')
l.sort()
print(' '.join(l))
l = s.split(' ')
uppercase(l)
print(' '.join(l))
