
import matplotlib.pyplot as plt
import json
from shared import *


def plot_data(mileage, price):
    plt.scatter(mileage, price)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price distribution based on mileage")
    plt.show()


def regression_line(mileage_data, price, estimatePrice):
    plt.scatter(mileage_data, price)
    plt.plot(mileage_data, estimatePrice, color="red")
    plt.title('linear regression line prediction')
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.show()


if __name__ == "__main__" : 
    mileage_data, price, mileage_norm, mileage_min, mileage_max = load_data()
    with open("model.json", "r") as f:
        model = json.load(f)
    theta0, theta1 = model["theta0"], model["theta1"]
    estimate_price = theta0 + theta1 * mileage_norm
    plot_data(mileage_data, price)
    regression_line(mileage_data, price, estimate_price)
    



