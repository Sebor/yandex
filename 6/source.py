__author__ = 'Sebor'
import tarfile

tar = tarfile.open('input.tgz', 'r:gz')
path = 'sys/fs/cgroup/cpuacct/lxc'
fileName = 'cpuacct.usage'

pathLength = path.count('')
fileNameLength = fileName.count('')

maxUsage = 0
maxUsageName = ''

for dirs in tar.getmembers():
    if ((dirs.isdir()) and (path in dirs.name) and (dirs.name != path)) :
        rab = dirs
        rab.name = rab.name + '/' + fileName

        usage = tar.extractfile(rab.name).read()
        usage = int(usage.decode('utf-8'))

        if usage > maxUsage :
            maxUsage = usage
            maxUsageName = rab.name[pathLength:-fileNameLength]

print(maxUsageName)