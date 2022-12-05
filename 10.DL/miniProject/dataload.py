df=pd.read_csv('data_preprocessed.csv',index_col=0)
data = df.iloc[:,:-1]
target = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data,target
                                                 test_size=0.2,
                                                 random_state=1234,
                                                 shuffle=True,
                                                 stratify=target)

y_trainOHE = pd.get_dummies(y_train)
y_testOHE = pd.get_dummies(y_test)
