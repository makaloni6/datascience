import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.colors
import matplotlib.animation
import japanize_matplotlib

# 多項式回帰について実装、計算の確認

X = np.array([ 0.  ,  0.16,  0.22,  0.34,  0.44,  0.5 ,  0.67,  0.73,  0.9 ,  1.  ])
Y = np.array([-0.06,  0.94,  0.97,  0.85,  0.25,  0.09, -0.9 , -0.93, -0.53,  0.08])

# 3つめの引数は多項式の次数
W3 = Polynomial.fit(X, Y, 3)
print(type(W3))
w = W3.convert().coef
print(w)

# MSEの計算
print(np.mean((Y - W3(X)) ** 2)) #0.006168386150620887

# 次数を上げて過学習を確認
W9 = Polynomial.fit(X, Y, 9)
w = W9.convert().coef
print(w)
print(np.mean((Y - W9(X)) ** 2))


for d in range(1, 10):
    W = Polynomial.fit(X, Y, d)
    W = W.convert().coef
    print('d = {}: |W|_2^2 = {}'.format(d, np.dot(W, W)))




# 描画
# x = np.linspace(0, 1, 1000)
# fig, ax = plt.subplots(dpi=100)
# ax.scatter(X, Y, marker='o', color='b')
# ax.plot(x, W3(x), 'r')
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$')

# x = np.linspace(0, 1, 1000)
# fig, ax = plt.subplots(dpi=100)
# ax.scatter(X, Y, marker='o', color='y')
# ax.plot(x, W9(x), 'r')
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$')
# ax.grid()

# ax.grid()
# plt.legend(x)
# plt.show()


