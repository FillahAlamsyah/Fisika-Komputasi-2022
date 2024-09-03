from sklearn import svm
import pandas as pd

# Database: Gerbang logika AND
# Membaca data dari file
FileDB = 'logikaand.csv'
# selain dalam format csv, file dapat berbentuk text, misal: logikaand.txt
Database = pd.read_csv(FileDB, sep=",", header=0)
print(Database)

#x = Data, y = Target
x = Database[[u'Feature1', u'Feature2']]
y = Database.Target
x = x.values
#Training and Classify
clf = svm.SVC()
clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Support Vector Machine (SVM)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
