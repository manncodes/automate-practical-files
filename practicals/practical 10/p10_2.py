import random
import pandas as pd


# generate list with random numbers
def generate_list(n):
    return [random.randint(1, 100) for _ in range(n)]


random_list = generate_list(20)

# create pandas series from python list
country_series = pd.Series(random_list)

# mean, mean, mode, standard deviation, range, variance of series
print(f"{country_series.mean() = }")
print(f"{country_series.std() = }")
print(f"{country_series.mode() = }")
print(f"{country_series.min() = }")
print(f"{country_series.max() = }")
print(f"{country_series.var() = }")
