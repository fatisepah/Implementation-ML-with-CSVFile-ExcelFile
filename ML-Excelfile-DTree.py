import pandas as pd
from sklearn import tree

file_path = "C:/Users/ASUS/Desktop/Test/data.xlsx"
df = pd.read_excel(file_path)

x = df[['قد', 'وزن', 'شماره کفش']].values.tolist()  # تبدیل به لیست
y = df['جنسیت'].values.tolist()  

print("x=",x)
print("y=",y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[190, 89, 43], [160, 56, 39]]
answer = clf.predict(new_data)

print(answer[0])
print(answer[1])