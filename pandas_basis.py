import pandas as pd

# csvの読み込み
df = pd.read_csv('./csv/california_housing_test.csv')
print(df)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>

# データフレームの操作基礎
# 先頭と末尾の表示 引数で表示数を設定できる 初期値は5
print(df.head()) 
print(df.tail())

# スライス表記
print(df[:10]) #0~9　:は右側は含まない。左は含む
print(df[1:10])

# ヘッダーで指定
print(df['longitude'])

# ilocとlocの例　ヘッダーがない場合にはインデックスで指定できるilocが便利
# df.loc['a', 'B'] #a行B列の値
# df.loc[:, 'B'] #B列の値

# df.iloc[1, 2] #1行2列目の値

