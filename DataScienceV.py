import matplotlib.pyplot as plt

x = [34, 55, 12, 99, 100, 88, 32, 71, 93, 198, 122]
y = [11, 99, 90, 60, 49, 20, 43, 50, 21, 59, 54]

plt.scatter(x, y, color="green", marker="o", ec="blue", s=150)

plt.show()