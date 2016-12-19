from __builtin__ import int

import prereq
from prereq import Correctness
from math import  *
def distance_points(x,y,x1,y1):
    t =((x-x1)^2 + (y-y1)^2 )
    try :
        return sqrt(t)
    except :
        return 0
def ktestmodel(k,data_train,data):
    distance = []
    for datat in data_train:
        temp= distance_points(datat[0],datat[1],data[0],data[1])

        if len(distance) < 3 :
            t = zip(temp,datat[2])
            distance.append(t)
        else:
            md=0.0
            mlabel=""
            for i in range(k):
                d,label = zip(*distanc[i])
                if








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
for data in data_test:
    ktestmodel(k,data_train,data)


