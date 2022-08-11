#!/usr/bin/python
from regex import findall
import sys
from tiktok import ttdownloader
url=str(sys.argv[1])

#https://vm.tiktok.com/ZMNp33HPV/?k=1

d=ttdownloader(url)

mp3=str(findall(r'([a-zA-Z]\w+)', url)[4])+'.mp3'
d[2].download('./storage/shared/Tiktok/'+mp3)

print(mp3)

#print (str(sys.argv[1]))

