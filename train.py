import numpy as np
import matplotlib.pyplot as plt
import json
from shared import *



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
    mileage_data, price, mileage_normaliser, mileage_min, mileage_max = load_data()
    # mileage_data, price, mileage_standardiser, mileage_mean, mileage_std = load_data()
    theta0, theta1 = 0, 0
    learning_rate = 0.01
    iterations = 10000
    theta0, theta1, cost_history = compute_gradient(learning_rate, iterations, theta0, theta1, mileage_normaliser, price)
    # theta0, theta1, cost_history = compute_gradient(learning_rate, iterations, theta0, theta1, mileage_standardiser, price)
    # plot_convergence(cost_history)
    with open("model.json", "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f)
    print(f"Training completed. Model saved with theta0: {theta0:.2f} and theta1: {theta1:.2f}")

    # estimatePrice = theta0 + theta1 * mileage_normaliser
    # estimatePrice = theta0 + theta1 * mileage_standardiser
    # regression_line(mileage_data, price, estimatePrice)
    