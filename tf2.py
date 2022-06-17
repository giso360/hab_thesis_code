import keras.utils.conv_utils
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.engine.sequential import relax_input_shape
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from time import time
from keras import backend as K
from memory_profiler import profile


def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))



# y_pred = model.predict(x_test, batch_size=64, verbose=1)
# loss, accuracy, f1_score, precision, recall = model.evaluate(x_test, y_test, verbose=0)
# print(f1_score)

# model.save('my_model.h5')


# def do():
#     df = pd.read_csv('./numerical_dataset/unseen.csv')
#     X = df.drop([
#         "CLASS"
#     ], axis=1)
#     Y = df['CLASS']
#     model = tf.keras.models.load_model('my_model.h5')  # same file path
#     y_prob = model.predict(X, verbose=1)
#     print(y_prob)
#     # y_classes = keras.utils.np_utils
#     # print(y_classes)
#     # # print(y_prob)`
#     # for res in y_prob:
#     #     print(res[0])
#     #     print(tf.nn.sigmoid(res[0]))
#
#
# do()
fp = open('mem_profile.txt', 'w+')
@profile(stream=fp)
def do_prediction():
    columns = ["B01",
               "B02",
               "B03",
               "B04",
               "B05",
               "B06",
               "B07",
               "B08",
               "B08A",
               "B09",
               "B11",
               "B12",
               "NDCI",
               "NDVI",
               "NDVI_B8A",
               "MPHBI",
               "RD1",
               "RD2",
               "RD3",
               "CLASS"
               ]

    df = pd.read_csv('./numerical_dataset/hab_dataset_to_tf.csv')
    print(df.head())
    X = df.drop(['CLASS'], axis=1)

    Y = df['CLASS']

    print(X.head())
    print(Y.head())

    # normalize/scale features
    # min_max_scaler = preprocessing.MinMaxScaler()
    # X = pd.DataFrame(min_max_scaler.fit_transform(X))

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

    l2 = tf.keras.regularizers.L2(
        l2=0.01
    )

    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(19),
        tf.keras.layers.Dense(20, activation=tf.nn.sigmoid),
        tf.keras.layers.Dense(20, activation=tf.nn.relu),
        tf.keras.layers.Dense(20, activation=tf.nn.sigmoid),
        tf.keras.layers.Dense(20, activation=tf.nn.relu),
        tf.keras.layers.Dense(20, activation=tf.nn.sigmoid),
        tf.keras.layers.Dense(20, activation=tf.nn.relu),
        tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])
    model.compile(optimizer="adam",
                  loss='binary_crossentropy',
                  metrics=["accuracy", tf.keras.metrics.AUC(from_logits=True)])

    # model.compile(optimizer="adam",
    #               loss='binary_crossentropy',
    #               metrics=['acc',f1_m,precision_m, recall_m])

    model.fit(x_train, y_train, epochs=200, batch_size=50)

    res = model.evaluate(x_test, y_test, return_dict=True)

    print("[test loss, test acc, AUC]=", res)



do_prediction()