import pandas as pd
from sklearn.model_selection import train_test_split


df=pd.read_csv('data/amazon_train_samples_img.csv')
train, test = train_test_split(df, test_size=0.3)
val,test = train_test_split(test,test_size=0.5)
train.to_csv('data/amazon_train_samples_img_train.csv',index=False)
val.to_csv('data/amazon_train_samples_img_val.csv',index=False)
test.to_csv('data/amazon_train_samples_img_test.csv',index=False)