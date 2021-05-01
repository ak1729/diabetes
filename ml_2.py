import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(1234)

def generate_data(num_sample):
    x = np.array(range(num_sample))
    random_noise = np.random.uniform(-10, 10, size=num_sample)
    y = 3.5*x + random_noise

    return x, y

x, y = generate_data(50)
data = np.vstack([x, y]).T

df = pd.DataFrame(data, columns=['x', 'y'])

plt.title('generated_data')
plt.xlabel('x')
plt.ylabel('y')

plt.scatter(x, y)
plt.show()


