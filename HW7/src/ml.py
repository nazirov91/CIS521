'''
Created on Apr 4, 2012

@author: Naphy
'''

import numpy as np
import Dataset
import random

def naiveBayes(X, Y):   
    transposedY = Y.T[0]
    denom = np.sum(transposedY == 1)
    prod = 1
    for j in range(0, X[0].size):
        print j
        print np.sum(X[transposedY == 1, j]) 
        print denom
        prod *= np.sum(X[transposedY == 1,j]) / denom
        print prod
        print ''
    c = (denom / Y.size) * prod
    print c
    return c

def ridgeRegression(TrainX, TrainY, lam):
    tX = np.asmatrix(TrainX)
    tY = np.asmatrix(TrainY)
    size = tX.shape
    temp = lam*np.identity(len(TrainX[0]), float)
    w = np.linalg.inv(tX.T*tX + temp)*tX.T*tY
    return w

def streamwiseRegression(X, Y):
    cols = []
    error = 1
    m1 = np.asmatrix(X)
    m2 = np.asmatrix(Y)
    lamb=1
    I=np.identity(m1)
    
    for j in range(X[0].size):
        cols.append(j)
        
    
    for y in Y:
        w = np.linalg.inv(m1.T*m1*(lamb*I))*m1.T*y
        res = X*w
    return

def stepwiseRegression(X, Y):
    
    return

def perceptron(TrainX, TrainY, TestX, TestY):
    
    w = []
    for x in range(0, len(TrainX[0])):
        w.append(random.randint(-1,1))
    for j in range(0, 1000):
        for x in range(0,len(TrainX)):
            temp = np.dot(w, TrainX[x])
            yHat = 0
            
            if temp > 0:
                yHat = 1
            else:
                yHat = -1
            
            if yHat != TrainY[x]:
                w = np.add(w, TrainY[x]*TrainX[x])
    compY = []
    for x in range(0, len(TestX)):
        temp = np.dot(w, TestX[x])
        yHat = 0
            
        if temp > 0:
            yHat = 1.
        else:
            yHat = -1.
        compY.append(yHat)
    
    sum = 0.0
    for x in range(0, len(TestX)):
        if compY[x] == TestY[x][0]:
            sum = sum + 1
     
    return sum/float(len(TestX))



d = Dataset.Dataset("../rec.sport.baseball.txt", "../rec.sport.hockey.txt", cutoff=100)
labels=['baseball', 'hockey', 'PC', 'Mac']

test1 = d.getTrainAndTestSets(.8, 1)
test2 = d.getTrainAndTestSets(.8, 2)
test3 = d.getTrainAndTestSets(.8, 3)
test4 = d.getTrainAndTestSets(.8, 4)
test5 = d.getTrainAndTestSets(.8, 5)
print ridgeRegression(test1[0], test2[1], 3)
f = perceptron(test1[0], test1[1], test1[2], test1[3])
g = perceptron(test2[0], test2[1], test2[2], test2[3])
h = perceptron(test3[0], test3[1], test3[2], test3[3])
i = perceptron(test4[0], test4[1], test4[2], test4[3])
j = perceptron(test5[0], test5[1], test5[2], test5[3])
print f
print g
print h
print i
print j
#naiveBayes(test[0], test[1])
#streamwiseRegression(test[0], test[1])

'''
print 'X = ' + str(test[2])
print 'Y = ' + str(test[3].T[0])
print 'Y == 1 = ' + str(test[3].T[0] == 1)
print test[2].size
print test[2][0].size
print test[3].size
print 
'''

