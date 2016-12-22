
import prereq

from prereq import Correctness
spam={}

not_spam={}

mail_spam={}
mail_notspam={}
checker=[]

general= []
with open('general.txt','r') as f:
    for line in f:
        for word in line.split():
           general.append(word)



def tokkenize(file,flag):
    global spam
    global not_spam
    for line in file:
        for word in line.split():
            if word not in general:
                if flag is 's':
                    print "111111111111111"

                    try:
                        spam[word] = spam[word] + 1
                    except:
                        spam[word]=1
                elif flag is 'ns':
                    print "111111111111"
                    try:
                        not_spam[word] = not_spam[word] + 1
                    except:
                        not_spam[word]=1


def mailspammer(file):
    global spam
    global not_spam
    global checker
    for line in file:
        for word in line.split():
            if word not in general:
                try:
                    k=spam[word]
                    s=not_spam[word]
                    t=0.0
                    t= k / k + s
                    checker.append(t)

                except:
                    pass



file = open("test.txt", "r")

tokkenize(file,'s')

file1 = open("test2.txt","r")


tokkenize(file1,'ns')

file2 = open("check.txt","r")

mailspammer(file2)
sum =0.0
for i in checker:
    sum = sum + i

sum = sum /len(checker)

if sum> 0.5:
    print  "spam"
else:
    print "not spam"