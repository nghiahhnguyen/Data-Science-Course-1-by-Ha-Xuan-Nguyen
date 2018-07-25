def sum(l):
    cnt = 0
    for x in l:
        if type(x) == int or type(x) == float:
            cnt += x
    return cnt


l = [(1, 4, 'ewe', '5'), ('21', 0.4, 4, [31, 3, 5]), [7, 3, 's', 2], [4, 2, 6, 'dad'], {3, 5}]
l.sort(key=lambda x: sum(x))
print(l)
