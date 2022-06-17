import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

pd.set_option('display.max_columns', 30)

hab_data = pd.read_csv('./numerical_dataset/HAB_dataset.csv')
print(hab_data.shape)
print(hab_data.size)
print(hab_data.empty)
print(hab_data.isnull().sum())
print(hab_data.dtypes)
print(hab_data.columns)
print("=========")
print(hab_data.info())
print("=========")
print("=========")
print(hab_data.describe())
print("=========")
hab_data_HAB_label = hab_data[hab_data["CLASS"] == 1]
hab_data_NO_HAB_label = hab_data[hab_data["CLASS"] == 0]
print(hab_data_HAB_label.shape)
print(hab_data_NO_HAB_label.shape)
print("===========HAB DATA============")
print(hab_data_HAB_label.describe())
print("===========NO_HAB DATA============")
print(hab_data_NO_HAB_label.describe())
print("===========DISTRIBUTION PLOTS============")

# max_value = 65
# feature_name = "RD3"
# plt.hist(hab_data[feature_name], bins=50, edgecolor='black')
# plt.title(feature_name + " for the whole dataset")
# plt.xlabel(feature_name + " index")
# plt.ylabel("Counts")
# plt.xlim(0, max_value)
#
# plt.show()
#
# plt.hist(hab_data_HAB_label[feature_name], bins=50, edgecolor='black', color='red')
# plt.title(feature_name + " for the HAB pixels ONLY")
# plt.xlabel(feature_name + " index")
# plt.ylabel("Counts")
# plt.xlim(0, max_value)
#
# plt.show()
#
# plt.hist(hab_data_NO_HAB_label[feature_name], bins=50, edgecolor='black', color='green')
# plt.title(feature_name + " for the NO_HAB pixels ONLY")
# plt.xlabel(feature_name + " index")
# plt.ylabel("Counts")
# plt.xlim(0, max_value)
#
# plt.show()

print("===============")
print("GENERAL QUERIES")
print("===============")

print("NDCI: " + str(len(hab_data[hab_data["NDCI"] > 0.4])))
print("NDVI: " + str(len(hab_data[hab_data["NDVI"] > 0.6])))
print("NDVI_B8A: " + str(len(hab_data[hab_data["NDVI_B8A"] > 0.6])))
print("MPHBI: " + str(len(hab_data[hab_data["MPHBI"] > 20])))
print("RD1: " + str(len(hab_data[hab_data["RD1"] > 21.99])))
print("RD2: " + str(len(hab_data[hab_data["RD2"] > 50])))
print("RD3: " + str(len(hab_data[hab_data["RD3"] > 40])))


print("===========================")
print("GENERATE CSV FOR TENSORFLOW")
print("===========================")

df_shuffled = shuffle(hab_data)
df_shuffled.to_csv('./numerical_dataset/hab_dataset_to_tf.csv', encoding='utf-8', index=False)