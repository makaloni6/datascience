#pip install numpyでインストール
import numpy as np

# vector
x = np.array([[1, 2, 3]])
print(x)

# 平均値 
# meanで計算してくれる　引き算も可能
print(x.mean())
print(type(x.mean()))

print(x - x.mean()) # [[-1.  0.  1.]]で平均の2.0が引かれてる。

# 偏差
xc = x - x.mean() 

# 単回帰分析の定義式から実装 y = f(x)
# a = 偏差積和 / 偏差平方和
y = np.array([[2.5, 4, 8.6]])
yc = y - y.mean() 
print(yc) # [[-2.53333333 -1.03333333  3.56666667]]
a = (yc * xc).sum() / (xc * xc).sum()
print(a) #3.05

