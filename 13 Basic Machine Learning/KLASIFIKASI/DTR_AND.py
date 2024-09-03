from sklearn import tree

#Database : Gerbang Logika AND
#x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0, 1]

#Training and Classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Decision Tree)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0, 0]]))
print ("0 1 = ", clf.predict([[0, 1]]))
print ("1 0 = ", clf.predict([[1, 0]]))
print ("1 1 = ", clf.predict([[1, 1]]))
