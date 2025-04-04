
# Estimate price before training


# EstimatePrice formuleas 
## EstimatePrice(mileage) = theta0 + (theta1 * mileage)
#  Where theta0 is the biaise and theta1 is the weight  (poids ou ponderation en francais)
# before training theta0 and theta1 are set to 0.


import sys
import json
from shared import *

if __name__== "__main__" :
    
    mileage_input = float(input("Enter the mileage: "))
    theta0, theta1 = 0, 0
    mileage_data, price, mileage_norm, mileage_min, mileage_max = load_data()
    try:
        with open("model.json", "r") as f :
            model = json.load(f)
        theta0, theta1 = model['theta0'], model['theta1']
        mileage_input = (mileage_input - mileage_min) / (mileage_max - mileage_min)
        estimate_price = theta0 + theta1 * mileage_input
        print(f"Estimate price: {estimate_price:.2f}")
    except FileNotFoundError:
        estimate_price = theta0 + theta1 * mileage_input
        print(f"Estimate price: {estimate_price}")