import numpy as np
from math import sqrt


def cutoff(X):
    x1,x2 = X[0], X[1]
    Y = [max(x1,0),max(x2,0)]
    return Y


def mlca (M, S_cue, S_motion, S_color, A, total_time=100, dt=.1, tau=1, th=10, std=.25) :
    
    time = np.arange(0,total_time,dt)
    X = np.zeros([int(total_time / dt)+1,2])

    for idx in range(len(time)-1):
        chi = np.random.normal(size=2, scale=std)
        mu  = np.dot(M, np.kron(S_cue.T, np.kron(S_motion.T, S_color.T))).squeeze()
        
        dX = (mu + np.dot(A,X[idx,:]))*dt/tau + chi*sqrt(dt/tau)
        X[idx+1,:] = cutoff(X[idx,:] + dX)
        
        if (X[idx+1,0]>=th) or (X[idx+1,1]>=th):
            time = time[:idx+1]
            X = X[:idx+1, :]
            return time, X

        if (idx==len(time)-2) :
            return time[:-1], X[:-2,:]