

import pandas as pd
import numpy as np
from shared import *
import json

def get_price_mean():
    data = pd.read_csv("data.csv")
    price = data["price"]
    price_mean = price.mean()
    return price_mean

# this function calculate the score or Rsquare 
def calculate_score_prediction(price, estimate_price, price_mean):
    r_square = 1 - np.sum((price - estimate_price) ** 2) / np.sum((price - price_mean) ** 2)
    return r_square


if __name__ == "__main__":
    mileage_data, price, mileage_norm, mileage_min, mileage_max = load_data()

    with open("model.json", "r") as f:
        model = json.load(f)
    theta0, theta1 = model["theta0"], model["theta1"]
    estimate_price = theta0 + theta1 * mileage_norm
    price_mean = get_price_mean()
    score = calculate_score_prediction(price, estimate_price, price_mean)
    print(f"score prediction = {score}")