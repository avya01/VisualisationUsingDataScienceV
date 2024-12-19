import matplotlib.pyplot as plt

x = [34, 55, 12, 99, 100, 88, 32, 71, 93, 198, 122]
y = [11, 99, 90, 60, 49, 20, 43, 50, 21, 59, 54]

x1 = [87, 44, 19, 49, 88, 39, 84, 109, 33, 55, 69]
y1 = [56, 90, 31, 90, 33, 75, 98, 23, 45, 69, 102]

plt.scatter(x, y, color="green", marker="o", ec="blue", s=150)
plt.scatter(x1, y1, color="blue", marker="^", ec="green", s=150)

plt.show()