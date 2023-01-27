from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
iris_dataset=load_iris()

print("\n IRIS TARGET NAMES: \n", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n[{0}]:[{1}]".format(i,iris_dataset.target_names[i]))

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"],random_state=0)

kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(X_train, y_train)
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(X_train, y_train)

for i in range (len(X_test)):
    X=X_test[i]
    X_new=np.array([X])
    prediction = kn.predict(X_new)
    print("\n Actual : {0}{1}, Predicted:{2}{3}".format(y_test[i],iris_dataset["target_names"][y_test[i]],prediction,iris_dataset ["target_names"][prediction]))

acc=kn.score(X_test,y_test)
print(acc)
