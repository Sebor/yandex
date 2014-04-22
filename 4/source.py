__author__ = 'Sebor'
import re
Output = open('output.txt', 'w')
lst =[]
k = 0
pattern = re.compile(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$')
for i in open('access.log'):
    column = i.split()
    lst.append(column[0])
for elem in range(len(lst)):
    if re.search(pattern, lst[elem]):
        k = k + 1
Output.write(str(k))
Output.close()