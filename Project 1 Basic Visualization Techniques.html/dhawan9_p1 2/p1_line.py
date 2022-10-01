
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in a csv file: pd.read_csv(), get the file path of the csv file 
# and paste into the function call
df = pd.read_csv("old_cars.csv")


# 1) select only cars from one origin
USdf = df[df["Origin"] == "US"]
EUdf = df[df["Origin"] == "Europe"]
JAdf = df[df["Origin"] == "Japan"]


# 2) get the average mpg for each year
# 3) save that data in a variable
grouped_df = USdf.groupby("Model")["MPG"]
mean_USdf = grouped_df.mean()
grouped_df = EUdf.groupby("Model") ["MPG"]
mean_EUdf = grouped_df.mean()
grouped_df = JAdf.groupby("Model") ["MPG"]
mean_JAdf = grouped_df.mean()

plt.plot(range(1970,1983), mean_USdf, label='US')
plt.plot(range(1970,1983), mean_EUdf,label='Europe')
plt.plot(range(1970,1983), mean_JAdf,label='Japan')  
plt.legend()
plt.xlabel('Year')
plt.ylabel('Average MPG')
plt.title('MPG by Year by Origin')

plt.savefig("p1_line.png")
plt.show()