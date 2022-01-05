#coding:utf-8
#日本語UTF8でエンコード
import os
from numpy import *
import codecs
from operator import *

def get_matrix(dir_name,date_from='2014-09-25',date_to='2015-10-02',column_no=5):
    command='ls '+dir_name
    p=os.popen(command,"r")
    file_names=[]
    while 1:
        line = p.readline()
        if not line: break
        file_names.append(line.rstrip())
    vecs=[]
    stock_info=[]
    date=[]
    for file_name in file_names:
        f = codecs.open(dir_name + "/" + file_name, 'r', 'shift-jis')
        lines=f.readlines()
        if len(lines)<2:
            print "skip ",file_name,"(",len(lines),")"
            continue
        if lines[2].split(',')[0]!=date_to or lines[len(lines)-1].split(',')[0]!=date_from:
            print "skip ",file_name,"(",len(lines),")"
            continue
        if len(date)==0:
            for i in range(2,len(lines)):
                date.append(lines[i].split(',')[0])
        stock_info.append((lines[0].split(',')[0],lines[0].split(',')[2]))
        vecs.append([float(lines[i].split(',')[column_no]) for i in range(2,len(lines))])
    return stock_info,date,matrix(vecs)

def analyze_nmf_result(U,V,stock_info,date,result_file='result_stock.txt'):
    out_file=codecs.open(result_file, 'w', 'utf-8')
    dim,column_dim=shape(V)
    row_dim=len(stock_info)

    for i in range(dim):
        dates=[]
        for j in range(column_dim):
            dates.append((date[j],V[i,j]))
        out_file.write('[')
        for s in sorted(dates,key=itemgetter(1),reverse=True)[0:10]:
            out_file.write(s[0]+' ')
        out_file.write(']\n')

        stocks=[]
        for j in range(row_dim):
            stocks.append((stock_info[j][0],stock_info[j][1],U[j,i]))
        for stock in sorted(stocks,key=itemgetter(2),reverse=True)[0:10]:
            out_file.write(stock[0]+' '+stock[1]+' '+str(stock[2])+'\n')
        out_file.write('\n')

    out_file.close()
    return
