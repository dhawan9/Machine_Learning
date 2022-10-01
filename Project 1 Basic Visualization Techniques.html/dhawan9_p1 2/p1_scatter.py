import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in a csv file: pd.read_csv(), get the file path of the csv file 
# and paste into the function call
df = pd.read_csv("old_cars.csv")

plt.scatter(df["Horsepower"], df["MPG"], c=df["Model"]+1900, cmap="viridis")
plt.colorbar()
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title('Horsepower vs MPG')

plt.savefig("p1_scatter.png")
plt.show()