import matplotlib.pyplot as plt
import numpy as np
import csv

# read csv file
with open('Boston.csv', 'r') as f:
    reader = csv.reader(f)
    myList = list(reader)
    rm = []
    medv = []

    i = 0
    for row in myList:
        if i == 0:
            i = 1
            continue   # skip the first row , its value is just a header
        rm.append(float(row[6]))
        medv.append(float(row[14]))

# Least square regression
XMean = np.mean(rm)
YMean = np.mean(medv)

A = 0.0
B = 0.0
for i in range(len(medv)):
    A += (rm[i] - XMean) * (medv[i] - YMean)
    B += (rm[i] - XMean)**2

slope = A / B
bias = YMean - slope * XMean
print("Linear model slope = ", slope)
print("Linear model intercept(bias) = ", bias)

# plotting
plt.title("medv Vs rm")
plt.xlabel("rm")
plt.ylabel("medv")
plt.scatter(rm, medv)

axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = bias + slope * x_vals
plt.plot(x_vals, y_vals, linewidth=3.0)
plt.show();

