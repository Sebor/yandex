__author__ = 'Sebor'
import tarfile
tar = tarfile.open('etc.tar.gz', 'r:gz')
Output = open('output.txt', 'w')
try:
    if tar.getmember('etc/inittab') and tar.getmember('etc/inittab').isfile():
        inittab = tar.extractfile('etc/inittab').readlines()
        for elem in range(len(inittab)):
            inittab[elem] = inittab[elem].decode('utf-8')
        for line in inittab:
            if line.startswith('id'):
                line = line.split(':')
                Output.write(line[1])
                Output.close()
except KeyError:
    rc_sysinit = tar.extractfile('etc/init/rc-sysinit.conf').readlines()
    for elem in range(len(rc_sysinit)):
        rc_sysinit[elem] = rc_sysinit[elem].decode('utf-8')
    for line in rc_sysinit:
        if line.startswith('env DEFAULT_RUNLEVEL'):
            line = line.split('=')
            Output.write(line[1])
            Output.close()