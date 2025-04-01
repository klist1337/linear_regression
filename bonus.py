
from train import load_data
import matplotlib.pyplot as plt

def plot_data(mileage, price):
    plt.scatter(mileage, price)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.title("price distribution based on mileage")
    plt.show()

if __name__ == "__main__" :
    mileage, price = load_data()
    plot_data(mileage, price)


