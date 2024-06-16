#Importing necesary library
import pandas as pd
import numpy as np
import sklearn.model_selection as ms

#Importing data set
df = pd.read_csv("./Dataset/PJME_hourly.csv")
print(df.head())

#Cleaning data
#print(df.loc[df["PJME_MW"].isna() == True]) #Checking if there is a missing value in dataset

#Pre-processing data
df["Datetime"] = pd.to_datetime(df["Datetime"])
#df = df.set_index("Datetime") 
#df.index = pd.to_datetime(df.index)
print(type(df["Datetime"]))

#Train-test split
#X_train, X_test, y_train, y_test = ms.train_test_split()
print(df.describe())    #count 145366 data, 
                        #train index from 0-116292, 
                        # test index from 116293-145366

train = df.iloc[df.index < 116293] #80% of data
test = df.iloc[df.index > 116292] #20% of data
print(test)
print(train)