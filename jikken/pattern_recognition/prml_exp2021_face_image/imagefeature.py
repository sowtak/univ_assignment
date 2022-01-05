import os
from PIL import Image
from numpy import *
from operator import *

def get_matrix(dir_name):
    command='ls '+dir_name
    p=os.popen(command,"r")
    file_names=[]
    while 1:
        line = p.readline()
        if not line: break
        file_names.append(line.rstrip())
    vecs=[]
    for file_name in file_names:
        img=Image.open(dir_name + '/' + file_name)
        vec=[]
        image_vecs=array(img)
        for i in range(shape(image_vecs)[0]):
            vec.extend(image_vecs[i])
        vecs.append(vec)    
    return file_names,matrix(vecs)

def matrix_sum(A):
    sum=0.0
    for i in range(shape(A)[0]):
        for j in range(shape(A)[1]):
            sum+=A[i,j]
    return sum

def analyze_nmf_result(U,V,file_names,dir_name,example_num=10,result_dir='result'):
    command='mkdir -p ' + result_dir
    ret_val=os.system(command)
    if ret_val!=0:
        print "error:",command
        
    dim,column_dim=shape(V)
    row_dim=len(file_names)
    img_size=int(sqrt(column_dim))

    out_file=file(result_dir+'/result.txt','w')

    rate_of_magnification=matrix_sum(U)/row_dim
    V*=rate_of_magnification
    U/=rate_of_magnification

    img_all=Image.new("RGB",(img_size*(example_num+1),img_size*dim), "white")
    
    for i in range(dim):
        file_prefix=result_dir+'/pat'+str(i)
        img_array=array(V[i,0:img_size])
        for j in range(1,img_size):
            img_array=r_[img_array,V[i,j*img_size:(j+1)*img_size]]
        img=Image.fromarray(uint8(img_array))
        img.save(file_prefix+'.pgm')
        img_all.paste(img,(0,img_size*i))
        
        out_file.write(str(i)+':')
        
        faces=[]
        for j in range(row_dim):
            faces.append((file_names[j],U[j,i]))
        for face in sorted(faces,key=itemgetter(1),reverse=True)[0:example_num]:
            out_file.write(str(face)+'\n')
        out_file.write('\n')

        img_list=[]
        for face in sorted(faces,key=itemgetter(1),reverse=True)[0:example_num]:
            img_list.append(Image.open(dir_name + '/' + face[0]))
        for j in range(len(img_list)):
            img_all.paste(img_list[j],(img_size*(j+1),img_size*i))
    out_file.close()
    img_all.save(result_dir+'/all.pgm')
    return
