from sklearn.linear_model import LogisticRegression



lr = LogisticRegression(max_iter =30, solver ='liblinear',multi_class ='auto').fit(X_train,y_train)

yhat = lr.predict(X_train)



from sklearn.metrics import accuracy_score



accuracy_score(y_train, yhat)



yhat_test = lr.predict(X_test)

accuracy_score(y_test, yhat_test)







predictions = lr.predict(X_train)

print(confusion_matrix(y_train,predictions))





predictionsTest = lr.predict(X_test)

print(confusion_matrix(y_test,predictionsTest))


