import sys
sys.path.append('../utils')
from utils import *
import numpy as np

class File:

    def __init__(self, idd, size):
        self.size = size
        self.id = idd

class Space:

    def __init__(self, size):
        self.size = size

    def setSize(self, size):
        self.size = size

class Filesystem:
    
    def __str__(self):
        infos = ''
        infos += f'Ordered Files: {[file.id for file in self.orderedfiles]}\n'
        infos += f'Positions: {self.positions}\n'
        infos += f'Spaces: {[space.size for space in self.spaces]}\n'
        return infos

    def __init__(self, line):
        line += '0'
        files = line[::2]
        spaces = line[1::2]
        self.orderedfiles = []
        self.positions = list(range(len(files)))
        self.spaces = []
        self.numfiles = len(files)
        for i, size in enumerate(files):
            size = int(size)
            file = File(i, size)
            self.orderedfiles.append(file)
        for size in spaces:
            size = int(size)
            self.spaces.append(Space(size))
    
    def fileInPosition(self, i):
        return self.orderedfiles[i]

    def fileById(self, idd):
        return self.orderedfiles[self.positions[idd]]

    def positionOfFiles(self, file):
        fileid = file.id
        return self.positions[fileid]

    def move(self, file):
        fileid = file.id
        fileposition = self.positions[fileid]
        for i, space in enumerate(self.spaces[:fileposition]):
            if space.size >= file.size:
                del self.orderedfiles[fileposition]
                self.orderedfiles.insert(i + 1, file)
                for j in range(i+1, fileposition + 1):
                    self.positions[self.fileInPosition(j).id] += 1
                self.positions[fileid] = i + 1
                self.spaces[fileposition - 1].setSize(self.spaces[fileposition - 1].size + self.spaces[fileposition].size + file.size)
                del self.spaces[fileposition]
                self.spaces.insert(i, Space(0))
                self.spaces[i+1].setSize(space.size - file.size)
                break

    def checksum(self):
        res = 0
        i = 0
        filepos = 0
        spaceIndex = 0
        isFile = True
        while True:
            if isFile:
                try:
                    file = self.orderedfiles[filepos] 
                except:
                    break
                res += file.id * ((i + file.size) * (i + file.size - 1) // 2 - i * (i-1) // 2) 
                i += file.size
                filepos += 1
                isFile = False
            else:
                i += self.spaces[spaceIndex].size
                spaceIndex += 1
                isFile = True
        return res

fs = Filesystem(read_data()[0])
for i in range(fs.numfiles - 1, -1, -1):
    fs.move(fs.fileById(i))
res = fs.checksum()
print(res)
copy_result(res)
