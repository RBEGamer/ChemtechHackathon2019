from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report,confusion_matrix





from sklearn.model_selection import train_test_split



X_train, X_test, y_train, y_test = train_test_split(X, y)



from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier



####init

mlp = MLPClassifier(hidden_layer_sizes=(1000,300,),max_iter=70)



####train

mlp.fit(X_train,y_train)



predictions = mlp.predict(X_train)

print(confusion_matrix(y_train,predictions))





predictionsTest = mlp.predict(X_test)

print(confusion_matrix(y_test,predictionsTest))
