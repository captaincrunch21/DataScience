from __builtin__ import int
from operator import itemgetter


import prereq
from prereq import Correctness
from math import  *

def distance_points(x,y,x1,y1):
    t =((x-x1)^2 + (y-y1)^2 )
    try :
        return sqrt(t)
    except :
        return 0

def sorter(list):
    for i  in range(len(list)):
        for j in range(len(list)):
            if list[i][0] < list[j][0]:
                t=list[j]
                list[j]=list[i]
                list[i]=t

    return list





def answer(list):
    dict={}
    for data in list:
        try:
            dict[data[1]]
            dict[data[1]]=dict[data[1]] + 1
        except:
            dict[data[1]] = 0
    data=[0,'']

    for label,count in dict.iteritems():

        if count > data[0] :
            data[0] = count
            data[1] = label



    return data[1]



def ktestmodel(k,data_train,data):
    distance = []

    for datat in data_train:
        temp= distance_points(datat[0],datat[1],data[0],data[1])

        distance.append([temp,datat[2]])
    distance=sorter(distance)



    distance=distance[0:k]
    return answer(distance)








n= int(raw_input("Length of data"))

raw_data = [[data for data in raw_input().strip().split(" ")] for index in range(n)]

x=[]
y=[]

label=[]

for data in raw_data:
    x.append(int(data[0]))
    y.append(int(data[1]))
    label.append(data[2])

data = zip(x,y,label)

x_train,y_train,label_train,x_test,y_test,label_test = prereq.train_the_data(data,0.75)

k = int(raw_input("Number of nearest nodes"))

data_train=zip(x_train,y_train,label_train)
data_test=zip(x_test,y_test,label_test)
t=0
f=0


for data in data_test:
    label=ktestmodel(k,data_train,data)
    print label,data[2]
    if label is data[2]:
        t= t + 1
    else:
        f =f +1

print t
print f

