import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Gambler:
    def __init__(self, ph) -> None:
        self.ph = ph
        self.v = [0.]*100 + [1]
        self.pie = None
        self.q = pd.DataFrame()
    
    def value_iter(self, theta):
        while True:
            delta = 0
            for cap in range(1,100):
                v_max = 0
                for a in range(1,min(cap,100-cap)+1):
                    v_new = self.ph*self.v[cap+a] + (1-self.ph)*self.v[cap-a]
                    if v_new > v_max:
                        v_max = v_new
                d = np.abs(self.v[cap] - v_max)
                if d > delta:
                    delta = d
                self.v[cap] = v_max
            if delta < theta:
                self.evaluation()
                return
    
    def evaluation(self):
        actions = range(1,51)
        #self.q.index = list(actions)
        for cap in range(1,100):
            d = {}
            for a in actions:
                if a <= min(cap,100-cap):
                    self.q.loc[a,cap] = self.ph*self.v[cap+a] + (1-self.ph)*self.v[cap-a]
        self.pie = self.q.idxmax()


if __name__ == '__main__':
    ph = [0.4, 0.25, 0.55]
    theta = 0.01
    for p in ph:
        g = Gambler(p)
        g.value_iter(theta)
        g.q.to_csv(f'./rl2020/4.9_q_{p}.csv')
        g.pie.plot()
    plt.show()