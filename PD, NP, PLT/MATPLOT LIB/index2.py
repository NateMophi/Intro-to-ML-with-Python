import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use("dark_background")

# # PLOT KUSTOMIZATION
# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# income= [55, 56, 62, 61, 72, 72, 73, 75]
# income_ticks = list(range(50, 81, 2))
# plt.plot(years, income)
# plt.title("Income of John (in USD)", fontsize=30, fontname="Century Gothic"   )
# plt.xlabel("Year")
# plt.ylabel("Yearly Income in USD")
# plt.yticks(income_ticks, [f"${x}k USD" for x in income_ticks])
# plt.show()


# LEGENDS
# stockA = [100, 102, 90, 101, 101, 100, 102]
# stockB = [90, 95, 102, 104, 105, 103, 109]
# stockC = [110, 115, 100, 105, 100, 98, 95]
# plt.plot(stockA, label = "Ford")
# plt.plot(stockB, label = "Ferrari")
# plt.plot(stockC, label = "Toyota")
# plt.legend(loc="lower right")
# plt.show()

## Custome Pie Chart
# votes = [10, 2, 5, 16, 22]
# people = ["A", "B", "C", "D", "E"]
# plt.pie(votes, labels=None, autopct="%.2f%%", pctdistance=1.3)
# plt.legend(labels=people, loc="lower left")
# plt.show()

## Plots 2 different plots in different windows
# x1, y1= np.random.random(100), np.random.random(100)
# x2, y2 = np.arange(100), np.random.random(100)

# plt.figure(1)
# plt.scatter(x1, y1)

# plt.figure(2)
# plt.plot(x2, y2)

# plt.show()

## SUBPLOTS
x =np.arange(100)
fig, axs = plt.subplots(2,2)
axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("Sine Wave")
axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("Cosine Wave")
axs[1,0].plot(x, np.random.random(100))
axs[1,0].set_title("Random Function")
axs[1,1].plot(x, np.log(x))
axs[1,1].set_title("LOG Function")
fig.suptitle("Four Plots")
plt.tight_layout()
plt.savefig("fourplots.png",dpi=500, transparent=False)