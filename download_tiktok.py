#!/usr/bin/python
from regex import findall
import sys
from tiktok import ttdownloader
url=str(sys.argv[1])

d=ttdownloader(url)

iid = findall(r'([a-zA-Z]\w+)', url)[4]

print(iid)

d[2].download(str(iid)+'.mp3')

#print (str(sys.argv[1]))
