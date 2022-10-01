import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in a csv file:
df = pd.read_csv("old_cars.csv")

df["mpg_bracket"] = pd.cut(df["MPG"], bins=[9,12,15,18,21,24,27,30,33,36,39,42,45,48], right=False)

grouped = df.groupby(["mpg_bracket", "Origin"])["Car"].count()
labels = grouped.reset_index()["mpg_bracket"].drop_duplicates().values

# adapted from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
origins = ["US", "Europe", "Japan"]
origin = "US"

counts = [[], [], []]
for bracket in labels:
    for i, origin in enumerate(origins):
        # get the count for the origin
        if (bracket, origin) in grouped.index:
            #print(bracket, origin, grouped.loc[(bracket, origin)])
            counts[i].append(grouped.loc[(bracket, origin)])
        else:
            #print(bracket, origin, 0)
            counts[i].append(0)

us_counts, eu_counts, japan_counts = counts

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 4/5*width, us_counts, 4/5*width, label='US')
rects2 = ax.bar(x, eu_counts, 4/5*width, label='Europe')
rects3 = ax.bar(x + 4/5*width, japan_counts, 4/5*width, label='Japan')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_xlabel('MPG Bracket')
ax.set_title('Count of Cars by MPG and Origin')
ax.set_xticks(x-1/2)
ax.set_xticklabels([str(i) for i in range(9,46,3)], rotation=90)
ax.legend()


fig.tight_layout()

plt.savefig("p1_grouped.png")
plt.show()