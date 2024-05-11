import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.colors
import matplotlib.animation
import japanize_matplotlib
from sklearn.linear_model import LinearRegression


X = np.array([
    [1, 2, 3],
    [1, 2, 5],
    [1, 3, 4],
    [1, 5, 9]
])
Yt = np.array([
    [1, 5, 6, 8]
])
# 定義を書く時に転置して書いたので
y = Yt.T
Xt = X.T

XtX_inv = np.linalg.inv(np.dot(Xt, X))
Xty = np.dot(Xt, y)
w = np.dot(XtX_inv, Xty)
print(w)
