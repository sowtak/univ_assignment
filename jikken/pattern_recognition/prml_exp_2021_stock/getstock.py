#coding:utf-8
import urllib2
import urllib
import os
import sys
import time

stock_list=urllib2.urlopen('http://k-db.com/stocks/2015-10-02?download=csv').readlines()

tosho_ichibu=[]
for stock in stock_list:
    l=stock.decode('shift-jis').split(',')
    if len(l)<4: continue
    if l[1] == u"東証1部":
        tosho_ichibu.append((l[0],l[2],l[3]))

command='mkdir -p stock_data'
ret_val=os.system(command)
if ret_val!=0:
    print "error:",command

if len(sys.argv)<2:
    first_data_no=0
else:
    first_data_no=int(sys.argv[1])
for i in range(first_data_no,len(tosho_ichibu)):
    urllib.urlretrieve('http://k-db.com/stocks/'+tosho_ichibu[i][0]+'?download=csv','stock_data/'+tosho_ichibu[i][0]+'.csv')
    time.sleep(1)
