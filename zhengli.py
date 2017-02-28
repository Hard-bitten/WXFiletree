import re
import sys
import string
import os,glob

filename = './string.txt'

fout = open("res.txt",'w')
searchtext = "/Users/ioscmechine/Desktop/hudson/workspace/"

fs = open(filename,'r+')
for line in fs.readlines():
    data = line.split("\"")
    if len(data) <= 2:
        continue
    if searchtext in data[1]:
        fout.write(data[1]+'\n')
fout.close()

fs = open('./res.txt','r+')
for line in fs.readlines():
    (basename,filename) = os.path.split(line)
    if not os.path.exists(basename):
        os.makedirs(basename)
    fout = open(line,'w')
    fout.write('')
    fout.close()