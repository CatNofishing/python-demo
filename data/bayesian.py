from blitz.modules import BayesianLinear
from blitz.utils import variational_estimator
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import os


os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'


@variational_estimator
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            BayesianLinear(30, 10),
            nn.ReLU(),
            BayesianLinear(10, 5),
            nn.ReLU(),
            BayesianLinear(5, 1)
        )

    def forward(self, x_train):
        x = self.layer(x_train)
        return x


if __name__ == '__main__':

    train_x = torch.tensor(np.load('./train_x.npy'),
                           dtype=torch.float)  # size(746,30)
    train_y = torch.tensor(np.load('./train_y.npy'),
                           dtype=torch.float).reshape(-1, 1)  # size(746,1)
    test_x = torch.tensor(np.load('./test_x.npy'),
                          dtype=torch.float)  # size(320,30)
    test_y = torch.tensor(np.load('./test_y.npy'),
                          dtype=torch.float).reshape(-1, 1)  # size(320,1)

    model = Model()
    criterio = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-2)

    for epoch in range(1000):
        predict_y = model(train_x)
        #loss = criterio(y_train.reshape(-1,1), predict_y)
        loss = model.sample_elbo(inputs=train_x,
                                 labels=train_y,
                                 criterion=criterio,
                                 sample_nbr=3)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if epoch % 1000 == 0:
            print(loss)

    plt.plot(test_y.numpy().reshape(-1), label='actual')
    plt.plot(model(test_x).detach().clone().reshape(-1), label='predict')
    plt.legend()
    plt.show()
