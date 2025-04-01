
# Estimate price before training


# EstimatePrice formuleas 
## EstimatePrice(mileage) = theta0 + (theta1 * mileage)
#  Where theta0 is the biaise and theta1 is the weight  (poids ou ponderation en francais)
# before training theta0 and theta1 are set to 0.


import sys

if __name__== "__main__" :
    mileage = input("Enter the mileage: ")
    theta0 = 0 # set to 0 before training
    theta1 = 0 # set to 0 before training
    estimatePrice = theta0 + (theta1 * int(mileage))
    print(f"estimate price = {estimatePrice}")