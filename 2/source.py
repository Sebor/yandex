__author__ = 'Sebor'
import re
Output = open('output.xml', 'w')
data = open('input.xml').read()
pattern1 = re.compile(r'<kernel>.+?</kernel>\n?')
pattern2 = re.compile(r'<initrd>.+?</initrd>\n?')
pattern4 = re.compile(r'<init>.+?</init>\n?')
pattern3 = re.compile(r'/b<boot dev.+?/>\n?')
data = re.sub(pattern1, '', data)
data = re.sub(pattern2, '', data)
data = re.sub(pattern4, '', data)
data = re.sub(pattern3, '<boot dev="hd"/>', data)
Output.write(data)
Output.close()