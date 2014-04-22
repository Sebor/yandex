__author__ = 'Sebor'
import re
def Hosts(file):
    try:
        pattern1 = re.compile(r'\bbar\b')
        pattern2 = re.compile(r'\bbar.domain\b')
        Output = open('output.txt', 'w')
        with open(file) as f:
             for line in f:
                  line = re.sub(pattern2, 'baz.donemain', line)
                  line = re.sub(pattern1, 'baz', line)
                  Output.write(line)
             Output.close()
    except IOError:
        print('File does not exist')
Hosts('input.txt')