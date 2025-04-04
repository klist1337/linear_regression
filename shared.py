
import pandas as pd

def load_data() :
    data = pd.read_csv("data.csv")
    mileage_data = data['km'].values
    price = data['price'].values
    # mileage_mean = mileage_data.mean()
    # mileage_std = mileage_data.std()
    # mileage_standardiser = (mileage_data - mileage_mean) / mileage_std
    # return mileage_data, price, mileage_standardiser, mileage_mean, mileage_std
    mileage_min = mileage_data.min()
    mileage_max = mileage_data.max()
    mileage_normaliser = (mileage_data - mileage_min) / (mileage_max - mileage_min)
    return mileage_data, price, mileage_normaliser, mileage_min, mileage_max
