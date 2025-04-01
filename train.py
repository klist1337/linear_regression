import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bonus import p

def load_data() :
    data = pd.read_csv("data.csv")
    mileage = data['km'].values
    price = data['price'].values
    return mileage, price


def plot_convergence(cost_history) :
    plt.plot(range(len(cost_history)), cost_history)
    plt.xlabel("iterations")
    plt.ylabel("cost")
    plt.title("cost function convergence")
    plt.show()

def estimate_price(mileage, theta0, theta1) :
    error = theta0 + theta1 * mileage
    return error

def compute_gradient(learning_rate, iterations, theta0, theta1, mileage, price):
    m = len(price)
    cost_history = []
    for _ in range(iterations):
        error = estimate_price(mileage, theta0, theta1) - price
        tmp_theta0 = learning_rate * (1 / m) * np.sum(error)
        tmp_theta1 = learning_rate * (1 / m) * np.sum(error * mileage)
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
        cost = (1 /  m) * np.sum(error ** 2)
        cost_history.append(cost)
    return theta0, theta1, cost_history

if __name__ == "__main__" :
    mileage, price = load_data()
    theta0, theta1 = 0, 0
    learning_rate = 1e-10
    iterations = 100
    theta0, theta1, cost_history = compute_gradient(learning_rate, iterations, theta0, theta1, mileage, price)
    # print(cost_history
    # plot_convergence(cost_history)
    estimatePrice = theta0 + theta1 * price
    
    