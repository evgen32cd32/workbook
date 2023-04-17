import numpy as np
from math import factorial
import datetime
#import multiprocessing as mp

class Rent:
    def __init__(self) -> None:
        self.rng = np.random.default_rng()

        self.v = np.zeros((21,21))
        self.pie = np.zeros((21,21))
        self.gamma = 0.9
        self.theta = 0.1

        self.rent = 10
        self.move = -2
        self.park_fee = -4
        self.exp_rent = {1:3,2:4}
        self.exp_ret = {1:3,2:2}

        self.p = {}
        for l in range(2,5):
            self.p[l] = np.zeros(21)
            for i in range(21):
                self.p[l][i] = self.poisson(l,i)
    
    def poisson(self, l, n):
        return np.exp(-l)*np.power(l,n)/factorial(n)
    
    #def ev_mp():
    
    def evaluation(self):
        now = datetime.datetime.now()
        print(f'Start {now}')
        it = 0
        while True:
            it += 1
            delta = 0
            for pk1 in range(21):
                for pk2 in range(21):
                    v_cur = self.v[pk1,pk2]
                    park1 = int(pk1 - self.pie[pk1,pk2])
                    park2 = int(pk2 + self.pie[pk1,pk2])
                    if park1 > 20:
                        park1 = 20
                    if park2 > 20:
                        park2 = 20
                    if self.pie[pk1,pk2] > 0:
                        v_new = (self.pie[pk1,pk2] - 1) * self.move
                    else:
                        v_new = - self.pie[pk1,pk2] * self.move
                    for t1 in range(park1+1):
                        p1 = self.p[self.exp_rent[1]][t1] if t1 < park1 else 1 - sum(self.p[self.exp_rent[1]][:t1])
                        for t2 in range(park2+1):
                            p2 = self.p[self.exp_rent[2]][t2] if t2 < park2 else 1 - sum(self.p[self.exp_rent[2]][:t2])
                            v_new += p1*p2 * (t1+t2) * self.rent
                            for r1 in range(21+t1-park1):
                                pr1 = self.p[self.exp_ret[1]][r1] if r1 < 20+t1-park1 else 1 - sum(self.p[self.exp_ret[1]][:r1])
                                for r2 in range(21+t2-park2):
                                    pr2 = self.p[self.exp_ret[2]][r2] if r2 < 20+t2-park2 else 1 - sum(self.p[self.exp_ret[2]][:r2])
                                    v_new += p1*p2*pr1*pr2 * self.gamma * self.v[park1-t1+r1,park2-t2+r2]
                                    if park1-t1+r1 > 10:
                                        v_new += p1*p2*pr1*pr2 * self.park_fee
                                    if park2-t2+r2 > 10:
                                        v_new += p1*p2*pr1*pr2 * self.park_fee
                    delta = max(delta, np.abs(v_cur - v_new))
                    self.v[park1,park2] = v_new
            nt = datetime.datetime.now()
            print(f'{it} {nt-now} {delta}')
            now = nt
            if delta < self.theta:
                return
        


if __name__ == '__main__':
    task = Rent()
    task.evaluation()
    print(task.pie)
    print(task.v)