# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import numpy as np
from IPython import get_ipython

# %%

get_ipython().run_line_magic('matplotlib', 'qt5')


def fun(x):
    return x+10*np.sin(x)+7*np.cos(4*x)


x = np.arange(0, 10, 0.01)
y = fun(x)
np.random.seed(10)
t = 100
x_old = np.random.uniform(0, 10, 1)[0]
y_old = fun(x_old)
theta = 0.9
iter = 1000
x_best = x_old
y_best = y_old
record = []
while t >= 10:
    for i in range(iter):
        x_new = x_old+(np.random.rand()-0.5)
        if (x_new >= 0) and (x_new <= 10):
            y_new = fun(x_new)
            if (y_new < y_old) or (np.exp(-(y_new-y_old)/t) > np.random.rand()):
                x_old = x_new
                y_old = y_new
                record.append([x_old, y_old])
                if y_old < y_best:
                    y_best = y_old
                    x_best = x_old
    t *= theta
print(x_best)
plt.ion()
plt.plot(x, y)
for i in range(0, len(record), 10):
    plt.scatter(record[i][0], record[i][1], c='r')
    plt.pause(1)
plt.ioff()


# %%

