import numpy as np
import matplotlib.pyplot as plt

steps = int(input('输入：'))
rndwlk = np.random.randint(-1, 2, size=(2, steps))
rndwlk = np.where(rndwlk == 0, 1, -1)
position = rndwlk.cumsum(axis=1)
dists = np.sqrt(position[0] ** 2 + position[1] ** 2)
np.set_printoptions(precision=4)
print(rndwlk)
print(position)
print(dists)
print(dists.max().round(4))
print(dists.min().round(4))
print(dists.mean().round(4))
print((dists > dists.mean()).sum())
x = position[0]
y = position[1]
plt.plot(x, y, c='g', marker='*')
plt.grid()
plt.scatter(0, 0, c='r', marker='o')
plt.text(.1, -.1, 'origin')
plt.scatter(x[-1], y[-1], c='r', marker='o')
plt.text(x[-1] + .1, y[-1] - .1, 'stop')
plt.savefig('F:\\jie\程序输出结果\随机游走图像.jpg', bbox_inches='tight')
plt.show()
# 一共26行代码
