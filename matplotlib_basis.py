import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./csv/california_housing_test.csv')
# 適当な切り出し
x_label = 'total_bedrooms'
y_label = 'median_house_value'
x = df[x_label]
y = df[y_label]
# plt.scatter(x, y)
# plt.show()

# 調整
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1, 1, 1) #キャンバス
ax.scatter(x, y, c='green');
ax.set_title('1st scatter')
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
plt.legend()
plt.show()