import random


def split_data(data,ratio):
    results_t=[]
    results_p=[]
    for row in data:
        if random.random()< ratio:
            results_t.append(row)
        else:
            results_p.append(row)
    results=[]
    results.append(results_t)
    results.append(results_p)


    return results

def train_the_data(data,ratio):

    train , test = split_data(data,ratio)
    x_train,y_train,label_train=zip(*train)
    x_test,y_test,label_test=zip(*test)

    return x_train,y_train,label_train,x_test,y_test,label_test

class Correctness:
    def accuracy(self,tp,fp,tn,fn):
        correct = tp + tn
        total = tp+tn+fp+fn

        return correct/total

    def precision(self,tp,fp,tn,fn):
        return tp/ (tp + fp)

    def recall(self,tp,fp,tn,fn):

        return tp / (tp + fn)

    def f1_score(self, tp, fp, tn, fn):

        p = self.precision(self,tp,fp,tn,fn)

        r = self.recall(self,tp,fp,tn,fn)

        return 2 * p * r /( p * r)

