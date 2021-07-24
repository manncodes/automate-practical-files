import numpy as np

# create 2 2D numpy arrays with random numbers
a = np.random.randint(0, 100, (10, 5))
b = np.random.randint(0, 100, (10, 5))

print(f"{a=}")
print(f"{b=}")

# concatenate 2 numpy arrays
c = np.concatenate((a, b))
print(f"{c=}")

# reshape array such that number of rows and columns are swapped
d = c.reshape(c.shape[-1], c.shape[0])
print(f"{d=}")
# or just transpose
d_t = c.T
print(f"{d_t=}")
