__author__ = 'Sebor'
def CountR(file):
    from collections import Counter
    lst = []
    with open(file) as f:
        for i in f:
            j = i[0:i.find(' ')]
            lst.append(j)
    c = Counter(lst).most_common(1)[0][1]
    print(c)
    return 0
CountR('input.txt')