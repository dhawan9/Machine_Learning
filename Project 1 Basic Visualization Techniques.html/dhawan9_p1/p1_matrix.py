import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in a csv file: pd.read_csv(), get the file path of the csv file 
# and paste into the function call
df = pd.read_csv("old_cars.csv")

columns = ["MPG", "Weight", "Horsepower", "Displacement"]

# set up a scatter plot matrix
fig, ax = plt.subplots(nrows=4, ncols=4,figsize=(10,10))

# ax contains a matrix of plots
# loop over the columns (nested loop to create every pair)
for row, r_col in enumerate(columns):
    for col, c_col in enumerate(columns):
        # create a scatter plot of r_col vs c_col and plot it on axis ax[row, col]
        # use country of origin for color
        ax[row,col].scatter(df[c_col], df[r_col], c=df["Origin"].replace({"US":"purple", "Europe":"green", "Japan":"blue"}))
        ax[row, 0].set_ylabel(r_col)
        ax[-1,col].set_xlabel(c_col)

plt.tight_layout()

plt.savefig("p1_matrix.png")
plt.show()