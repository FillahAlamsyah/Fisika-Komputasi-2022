#from library sklearn import metode Decision Tree
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Database
FileDB = 'sinus.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("---------------------")
print (Database)

#x = data, y = target
x = Database[[u'Feature']] #ciri1, #ciri2, dst
y = Database.Target
x = x.values

#Fit model regresi Decision Tree
reg = DecisionTreeRegressor(random_state=0)
reg = reg.fit(x, y)
#Menampilkan data prediksi
xx = np.arange(1, 21, 1)#(data pertama, data terakhir, rentang)
n  = len (xx)
print ("------------------------")
print ("-Prediksi Decision Tree-")
print ("xx(i)  decision tree")
for i in range (n):
    y_dct = reg.predict([[xx[i]]])
    print ('(:.2f)'.format(xx[i]), y_dct)

#Plot data prediksi
y_dct2  = reg.predict(x)
plt.figure()
plt.plot(x, y_dct2, color = 'red')
plt.scatter(x,y, color = 'blue')
plt.title ('Prediksi Data Menggunakan Decision Tree')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['decision tree', 'data'],loc=2)
plt.show()
