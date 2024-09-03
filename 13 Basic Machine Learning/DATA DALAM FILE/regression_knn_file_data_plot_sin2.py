#from sklearn import neural network
#from library sklearn import K-Nearest Neighbors
from sklearn.neighbors import KNeighborsRegressor
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
#Fit model regresi Nearest Neighbors
reg = KNeighborsRegressor(n_neighbors=1)
reg.fit(x, y)
#Menampilkan data prediksi
xx = np.arange(1, 21, 1)#(data pertama, data terakhir, rentang)
n  = len (xx)
print ("xx(i)  K-NN")
for i in range (n):
    y_neighbor = reg.predict([[xx[i]]])
    print ('(:.2f)'.format(xx[i]), y_neighbor)

#Plot data prediksi
y_neighbor2  = reg.predict(x)
plt.figure()
plt.plot(x, y_neighbor2, color = 'red')
plt.scatter(x,y, color = 'blue')
plt.title ('Prediksi Data Menggunakan K-Nearest Neighbors')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['nearest neighbors', 'data'],loc=2)
plt.show()
