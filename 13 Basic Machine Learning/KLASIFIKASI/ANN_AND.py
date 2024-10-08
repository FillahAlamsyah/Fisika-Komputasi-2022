from sklearn.neural_network import MLPClassifier

#Database : Gerbang Logika AND
#x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0, 1]

#Training and Classify
clf = MLPClassifier(solver='lbfgs', alpha=1e-2,
                    hidden_layer_sizes=(10, 5),
                    random_state=1, max_iter=1000,
                    warm_start=True)
clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0, 0]]))
print ("0 1 = ", clf.predict([[0, 1]]))
print ("1 0 = ", clf.predict([[1, 0]]))
print ("1 1 = ", clf.predict([[1, 1]]))
