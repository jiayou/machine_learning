import numpy as np
from numpy import vectorize 

f = lambda x : 1/(1+np.exp(-x))
df =lambda f: f*(1-f)

sigmoid = vectorize(f)

class Layer:
    
    name = ""
    W=[]
    b=[]
    x=[]
    y=[]
    err=[]
    lr = 0.01       # learning rate
    
    def __init__(self, in_dim ,out_dim, name=""):
        self.W = np.random.randn(out_dim, in_dim) * 0.01
        self.b = np.random.randn(1) *0.01
        self.name = name;
        
    def feed(self, x):
#        print("==================== Feed Through ================"+self.name)
        self.x = x
        z = np.dot(self.W, x)+self.b
        self.y = sigmoid(z)
        return self.y
        
    def bp(self, delta):
#        print("==================== Back Propagation ================"+self.name)
        out = self.y
        err  = out * (1-out) * delta
        delta = np.dot(self.W.T, err)
        
        db = np.sum(err)        
        dW = np.dot(err, self.x.T) 
        
        self.W += dW
        self.b += db
        
        return delta

    def gradient(self, delta):
        out = self.y
        err  = out * (1-out) * delta

        delta = np.dot(self.W.T, err)        
        db = np.sum(err)
        dW = np.dot(err, self.x.T) 
        
        return dW, db, delta
        