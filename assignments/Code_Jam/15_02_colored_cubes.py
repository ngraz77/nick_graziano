import matplotlib.pyplot as plt
cubes = [1, 8, 27, 64, 125]
 
fig, ax = plt.subplots()
ax.plot(cubes)
plt.show()

ax.scatter(x_values, y_values, color='red', s=10)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
 # Set chart title and label axes.--snip