mport numpy

import pandas

from keras.models import Sequential

from keras.layers import Dense

from keras.wrappers.scikit_learn import KerasClassifier

from keras.utils import np_utils

#from sklearn.cross_validation import train_test_split

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

# fix random seed for reproducibility

seed = 12

numpy.random.seed(seed)



# encode class values as integers

encoder = LabelEncoder()

encoder.fit(Y)

encoded_Y = encoder.transform(Y)

# convert integers to dummy variables (i.e. one hot encoded)

dummy_y = np_utils.to_categorical(encoded_Y)

# define baseline model

def baseline_model():

    # create model

    model = Sequential()

    model.add(Dense(100, input_dim=1700, init='normal', activation='relu'))

    model.add(Dense(5, init='normal', activation='sigmoid'))

    # Compile model

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model



estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=30, batch_size=5, verbose=0)







numpy.argmax(Y_test, axis=None, out=None)

X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.33, random_state=seed)



from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)



estimator.fit(X_train, Y_train)



predictionsTrain = estimator.predict(X_train)

y_classes_Train = [np.argmax(y, axis=None, out=None) for y in Y_train]

print(confusion_matrix(y_classes_Train,predictionsTrain))



predictions = estimator.predict(X_test)

y_classes = [np.argmax(y, axis=None, out=None) for y in Y_test]

print(confusion_matrix(y_classes,predictions))


