import csv
from sklearn import tree

x=[[190,100,48],[180,90,44],[164,56,39]
   ,[180,84,42],[160,54,38],[178,76,40]
   ,[175,81,42],[159,50,37],[185,90,43]
   ,[178,87,44],[159,60,38],[188,96,45]]
y=['مرد', 'مرد', 'زن'
   , 'مرد', 'زن', 'مرد'
   , 'زن', 'زن', 'مرد'
   , 'مرد', 'زن', 'مرد']


clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

new_data=[[190,89,43],[160,56,39]]
answer=clf.predict(new_data)
print(answer[0])
print(answer[1])