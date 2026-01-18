import matplotlib.pyplot as plt
import numpy as np

# # BAR CHART
# lang = ["C++", "C#", "Python", "Java", "Go"]
# votes = [20, 50, 140, 1, 45]
# plt.bar(lang, votes, color="purple", width=0.5, edgecolor="black", lw=6)
# plt.show()

# x_data = np.random.random(50)*100 #50 random vals b/w 0 and 1 multipyling them by 100
# y_data = np.random.random(50)*100 
# print(y_data)

# # SCATTERPLOT
# plt.scatter(x_data, y_data, c = "#004", marker="+")
# plt.show()

# # LINEPLOT
# years = [2006 + x for x in range(16)]
# weights= [80,83,84,85,86,82,81,79,83,80,82,82,83,81,80,79]
# plt.plot(years, weights, color="orange", lw=2, linestyle = "--")
# plt.show()

# # HISTOGRAM
# ages = np.random.normal(20, 1.5, 100)
# # plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
# plt.hist(ages, bins =20, cumulative=True)
# plt.show()

# # PIE CHART
# lang2= ["Python", "C++", "Java", "C#", "Go"]
# v = [50, 24, 14,6, 17 ]
# explodes = [0,0,0,0.3,0]
# plt.pie(v, labels= lang2, explode = explodes, autopct="%.2f%%", pctdistance=1.3, startangle=45)
# plt.show()

# # BOX PLOT
# heights = np.random.normal(172, 8, 300)
# plt.boxplot(heights)
# plt.show()
first = np.linspace(0,10,25)
second= np.linspace(10,200,25)
third = np.linspace(200,210,25)
fourth = np.linspace(210,230,25)
data = np.concatenate((first, second, third, fourth))
plt.boxplot(data)
plt.show()
