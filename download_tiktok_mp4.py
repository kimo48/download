#!/usr/bin/python
from regex import findall
import sys
from tiktok import ttdownloader
url=str(sys.argv[1])

#https://vm.tiktok.com/ZMNp33HPV/?k=1

d=ttdownloader(url)

mp4=str(findall(r'([a-zA-Z]\w+)', url)[4])+'.mp4'


d[2].download('C:/Users/ssd/Desktop/'+mp4)

print(mp4)

#print (str(sys.argv[1]))
