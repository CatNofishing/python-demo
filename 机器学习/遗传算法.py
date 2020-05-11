import numpy as np
import matplotlib.pyplot as plt

class Genetic_algorithm:
    def __init__(self, group_number=5, chro_length=4, mat_pro=0.8, muta_pro=0.2, iter=1000):
        self.iter = iter
        self.chro_length = chro_length
        self.group_number = group_number
        self.mat_pro = mat_pro
        self.muta_pro = muta_pro
        self.group_init = np.random.uniform(
            0, 100, (group_number, chro_length))
        self.group_fitnees = self.cal_fitness(self.group_init)
        self.best_ind=self.group_init[np.argmax(self.group_fitnees)]
        self.best_fitnees=self.cal_fitness(self.best_ind)
        self.itearation()

    def fun(self, ind):
        if ind.ndim == 1:
            return 1/(np.sum(ind**2)+1)
        else:
            return 1/(np.sum(ind**2, axis=1)+1)

    def cal_fitness(self, ind):
        if ind.ndim == 1:
            return 1/(np.sum(ind**2)+1)
        else:
            return 1/(np.sum(ind**2, axis=1)+1)

    def cal_choice_pro(self):
        return self.group_fitnees/np.sum(self.group_fitnees)

    def group_choice(self):
        index = []
        group_ind_pro = self.cal_choice_pro()
        pro_sum = np.cumsum(group_ind_pro)
        rand_value = np.random.rand(self.group_number)
        for i in range(len(rand_value)):
            index.append(np.argwhere(pro_sum >= rand_value[i]).ravel()[0])
        if len(index)==0:
            return
        self.group_init = self.group_init[index]

    def group_mat(self):
        pro = np.random.rand(self.group_number)
        index = np.argwhere(pro > self.mat_pro).ravel()
        if len(index)==0:
            return
        for i in range(0, len(index)-1):
            rand_num = np.random.randint(0, self.chro_length)
            value = self.group_init[index[i]][rand_num]
            self.group_init[index[i]
                            ][rand_num] = self.group_init[index[i]+1][rand_num]
            self.group_init[index[i+1]][rand_num] = value

    def group_mut(self):
        pro = np.random.rand(self.group_number)
        index = np.argwhere(pro <= self.muta_pro).ravel()
        if len(index)==0:
            return
        for i in index:
            self.group_init[i][np.random.randint(
                0, self.chro_length)] = np.random.randint(-100, 100)

    def itearation(self):
        for i in range(self.iter):
            self.group_choice()
            self.group_mat()
            self.group_mut()
            self.group_fitnees = self.cal_fitness(self.group_init)
            best_ind=self.group_init[np.argmax(self.group_fitnees)]
            best_fitnees=self.cal_fitness(best_ind)
            if best_fitnees>self.best_fitnees:
                self.best_fitnees=best_fitnees
                self.best_ind=best_ind
            if i%100==0:
                print(f'第{i}次',self.best_ind,self.best_fitnees,sep='  ')
        print(self.best_ind,self.best_fitnees) 

if  __name__=='__main__':
    np.random.seed(100)
    gen=Genetic_algorithm()

