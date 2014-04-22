__author__ = 'Sebor'
def func(file):
    from collections import Counter
    lst = []
    k = 0
    f = open(file)
    for i in f :
        while i[k] != ' ':
            j = i[0:k+1]
            k+=1
        lst.append(j)
        k = 0
    t = tuple(lst)
    c = Counter(t).most_common(1)[0][1]
    print(c)
    return 0
func('input.txt')