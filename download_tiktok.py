#!/usr/bin/python
from regex import findall
import sys
from tiktok import ttdownloader
url=str(sys.argv[1])

d=ttdownloader(url)

iid = findall(r'[0-9]{19}', url)[0]
print(iid)

d[2].download(iid+'.mp3')

#print (str(sys.argv[1]))
