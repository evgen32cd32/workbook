import numpy as np
from math import factorial
import datetime
from multiprocessing import Pool

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
    
    def _ev_mp(park1, park2, r_move, p, exp_rent, rent, exp_ret, gamma, v, park_fee):
        v_new = r_move
        for t1 in range(park1+1):
            p1 = p[exp_rent[1]][t1] if t1 < park1 else 1 - sum(p[exp_rent[1]][:t1])
            for t2 in range(park2+1):
                p2 = p[exp_rent[2]][t2] if t2 < park2 else 1 - sum(p[exp_rent[2]][:t2])
                v_new += p1*p2 * (t1+t2) * rent
                for r1 in range(21+t1-park1):
                    pr1 = p[exp_ret[1]][r1] if r1 < 20+t1-park1 else 1 - sum(p[exp_ret[1]][:r1])
                    for r2 in range(21+t2-park2):
                        pr2 = p[exp_ret[2]][r2] if r2 < 20+t2-park2 else 1 - sum(p[exp_ret[2]][:r2])
                        v_new += p1*p2*pr1*pr2 * gamma * v[park1-t1+r1,park2-t2+r2]
                        if park1-t1+r1 > 10:
                            v_new += p1*p2*pr1*pr2 * park_fee
                        if park2-t2+r2 > 10:
                            v_new += p1*p2*pr1*pr2 * park_fee
        return v_new

    def evaluation(self):
        now = datetime.datetime.now()
        print(f'Start evaluation {now}')
        with Pool() as pool:
            it = 0
            while True:
                it += 1
                data_input = []
                for pk1 in range(21):
                    for pk2 in range(21):
                        park1 = int(pk1 - self.pie[pk1,pk2])
                        park2 = int(pk2 + self.pie[pk1,pk2])
                        if park1 > 20:
                            park1 = 20
                        if park2 > 20:
                            park2 = 20
                        if self.pie[pk1,pk2] > 0:
                            r_move = (self.pie[pk1,pk2] - 1) * self.move
                        else:
                            r_move = - self.pie[pk1,pk2] * self.move
                        data_input.append((park1, park2, r_move, self.p, self.exp_rent, self.rent, self.exp_ret, self.gamma, self.v, self.park_fee))
                v_new = np.reshape(np.asarray(pool.starmap(Rent._ev_mp, data_input)),(-1,21))
                delta = np.max(np.abs(self.v - v_new))
                self.v = v_new
                nt = datetime.datetime.now()
                print(f'{it} {nt-now} {delta}')
                now = nt
                if delta < self.theta:
                    return it > 1
    
    def improvement(self):
        now = datetime.datetime.now()
        print(f'Start improvement {now}')
        with Pool() as pool:
            data_input = []
            di = []
            for pk1 in range(21):
                for pk2 in range(21):
                    for pie in range(max(-5,-pk2),min(7,pk1+1)):
                        park1 = int(pk1 - pie)
                        park2 = int(pk2 + pie)
                        if park1 < 0 or park2 < 0:
                            continue
                        if park1 > 20:
                            park1 = 20
                        if park2 > 20:
                            park2 = 20
                        if pie > 0:
                            r_move = (pie - 1) * self.move
                        else:
                            r_move = - pie * self.move
                        di.append((pk1,pk2,pie))
                        data_input.append((park1, park2, r_move, self.p, self.exp_rent, self.rent, self.exp_ret, self.gamma, self.v, self.park_fee))
            v_new = pool.starmap(Rent._ev_mp, data_input)
            pk1, pk2, pie_max = di[0]
            v_max = v_new[0]
            changed = False
            for i in range(1, len(di)):
                park1, park2, pie = di[i]
                if park2 != pk2:
                    if int(self.pie[pk1,pk2]) != pie_max:
                        changed = True
                        self.pie[pk1,pk2] = pie_max
                    pk1 = park1
                    pk2 = park2
                    v_max = v_new[i]
                    pie_max = pie
                    continue
                if v_new[i] > v_max:
                    v_max = v_new[i]
                    pie_max = pie
            nt = datetime.datetime.now()
            print(f'{nt-now} {changed}')
            return changed

        


if __name__ == '__main__':
    task = Rent()
    while(task.evaluation() and task.improvement()):
        pass
    print(task.pie)
    print(task.v)
