from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np


df=pd.read_csv('NTrain.csv')
df.dtypes


df['GarageQual'].value_counts()
df['Exterior2nd'] = df['Exterior2nd'].astype('int')

def pro1():
    q1={"Utilities":{"AllPub":1,"NoSeWa":2}}
    df['Utilities'].fillna(1,inplace=True)
    df.replace(q1,inplace=True)
    q2={"Neighborhood":{"NAmes":1,"CollgCr":2,"OldTown":3,"Edwards":4,"Somerst":5,"Gilbert":6,"NridgHt":7,"Sawyer":8,
                        "NWAmes":9,"SawyerW":10,
                        "BrkSide":11,"Crawfor":12,"Mitchel":13,"NoRidge":14,"Timber":15,
                        "IDOTRR":16,"ClearCr":17,
                        "StoneBr":18,"SWISU":19,"MeadowV":20,"Blmngtn":21,"BrDale":22,"Veenker":23,
                        "NPkVill":24,"Blueste":25}}
    df['Neighborhood'].fillna(1,inplace=True)
    df.replace(q2,inplace=True)
    s1={"Condition1":{"Norm":1,"Feedr":2,"Artery":3,"RRAn":4,"PosN":5,"RRAe":6,"PosA":7,"RRNn":8,"RRNe":9}}
    df['Condition1'].fillna(1,inplace=True)
    df.replace(s1,inplace=True)
    s2={"Condition2":{"Norm":1,"Feedr":2,"Artery":3,"RRAn":4,"PosN":5,"RRAe":6,"PosA":7,"RRNn":8}}
    df['Condition2'].fillna(1,inplace=True)
    df.replace(s2,inplace=True)

def pro2():
    s3={"BldgType":{"1Fam":1,"TwnhsE":2,"Duplex":3,"Twnhs":4,"2fmCon":5}}
    df['BldgType'].fillna(1,inplace=True)
    df.replace(s3,inplace=True)
    s4={"HouseStyle":{"1Story":1,"2Story":2,"1.5Fin":3,"SLvl":4,"SFoyer":5,"1.5Unf":6,"2.5Unf":7,"2.5Fin":8}}
    df['HouseStyle'].fillna(1,inplace=True)
    df.replace(s4,inplace=True)
    s7={"Exterior1st":{"VinylSd":1,"HdBoard":2,"MetalSd":3,"Wd Sdng":4,"Plywood":5,"CemntBd":6,"BrkFace":7,"WdShing":8,"Stucco":9,"AsbShng":10,"Stone":11,"BrkComm":12,"CBlock":13,"ImStucc":14,"AsphShn":15}}
    df['Exterior1st'].fillna(1,inplace=True)
    df.replace(s7,inplace=True)
    s8={"Exterior2nd":{"VinylSd":1,"HdBoard":3,
                       "MetalSd":2,"Wd Sdng":4,
                       "Plywood":5,"CmentBd":6,
                       "BrkFace":9,"Wd Shng":7,
                       "Stucco":8,"AsbShng":10,
                       "Stone":13,"Brk Cmn":12,
                       "CBlock":16,"ImStucc":11,
                       "AsphShn":14,"Other":15}}
    df['Exterior2nd'].fillna(1,inplace=True)
    df.replace(s8,inplace=True)
    q3={"ExterQual":{"TA":1,"Gd":2,"Ex":3,"Fa":4}}
    df['ExterQual'].fillna(1,inplace=True)
    df.replace(q3,inplace=True)
    
def pro3():    
    q4={"ExterCond":{"TA":1,"Gd":2,"Ex":4,"Fa":3,"Po":5}}
    df['ExterCond'].fillna(1,inplace=True)
    df.replace(q4,inplace=True)
    s9={"Foundation":{"PConc":1,"CBlock":2,"BrkTil":3,"Slab":4,"Stone":5,"Wood":6}}
    df['Foundation'].fillna(1,inplace=True)
    df.replace(s9,inplace=True)
    q9={"BsmtQual":{"TA":1,"Gd":2,"Ex":3,"Fa":4}}
    df['BsmtQual'].fillna(1,inplace=True)
    df.replace(q9,inplace=True)
    q10={"BsmtCond":{"TA":1,"Gd":2,"Po":4,"Fa":3}}
    df['BsmtCond'].fillna(1,inplace=True)
    df.replace(q10,inplace=True)

def pro4():
    q11={"BsmtFinType1":{"Unf":1,"GLQ":2,"ALQ":3,"BLQ":4,"Rec":5,"LwQ":6}}
    df['BsmtFinType1'].fillna(1,inplace=True)
    df.replace(q11,inplace=True)
    s10={"BsmtFinType2":{"Unf":1,"Rec":2,"LwQ":3,"BLQ":4,"ALQ":5,
                         "GLQ":6}}
    df['BsmtFinType2'].fillna(1,inplace=True)
    df.replace(s10,inplace=True)
    q5={"Heating":{"GasA":1,"GasW":2,"Grav":3,"Wall":4,"OthW":5,"Floor":6}}
    df['Heating'].fillna(1,inplace=True)
    df.replace(q5,inplace=True)
    q6={"HeatingQC":{"TA":2,"Gd":3,"Ex":1,"Fa":4,"Po":5}}
    df['HeatingQC'].fillna(1,inplace=True)
    df.replace(q6,inplace=True)
    
def pro5():
    s11={"CentralAir":{"Y":1,"N":2}}
    df['CentralAir'].fillna(1,inplace=True)
    df.replace(s11,inplace=True)
    q7={"Electrical":{"SBrkr":1,"FuseA":2,"FuseF":3,"FuseP":4,"Mix":5}}
    df['Electrical'].fillna(1,inplace=True)
    df.replace(q7,inplace=True)
    q8={"KitchenQual":{"TA":1,"Gd":2,"Ex":3,"Fa":4}}
    df['KitchenQual'].fillna(1,inplace=True)
    df.replace(q8,inplace=True)
    s12={"Functional":{"Typ":1,"Min2":2,"Min1":3,
                       "Mod":4,"Maj1":5,
                       "Maj2":6,"Sev":7}}
    df['Functional'].fillna(1,inplace=True)
    df.replace(s12,inplace=True)
    s13={"FireplaceQu":{"Gd":1,"TA":2,"Fa":3,"Ex":4,"Po":5}}
    df['FireplaceQu'].fillna(1,inplace=True)
    df.replace(s13,inplace=True)

def pro6():
    s14={"GarageType":{"Attchd":1,"Detchd":2,"BuiltIn":3,"Basment":4,"CarPort":5,"2Types":6}}
    df['GarageType'].fillna(1,inplace=True)
    df.replace(s14,inplace=True)
    s16={"GarageQual":{"TA":1,"Fa":2,"Gd":3,"Ex":4,"Po":5}}
    df['GarageQual'].fillna(1,inplace=True)
    df.replace(s16,inplace=True)
    s17={"GarageCond":{"TA":1,"Fa":2,"Gd":3,"Ex":5,"Po":4}}
    df['GarageCond'].fillna(1,inplace=True)
    df.replace(s17,inplace=True)
    s18={"PavedDrive":{"Y":1,"N":2,"P":3}}
    df['PavedDrive'].fillna(1,inplace=True)
    df.replace(s18,inplace=True)
    
    
pro1()
pro2()
pro3() 
pro4()
pro5()
pro6()

df=df-df.max()/df.max()-df.min()

features_mean=list(df.columns[0:34])

outcome_var='SalePrice' 
predictor_var = features_mean

traindf,testdf=train_test_split(df,test_size = 0.3)

scaler = MinMaxScaler(feature_range=(0,1))

x = scaler.fit_transform(traindf[predictor_var])
y = scaler.fit_transform(testdf[predictor_var])
np.set_printoptions(precision=3)
Rgr = MLPRegressor(hidden_layer_sizes=(7), learning_rate='constant')
Rgr.fit(x,traindf[outcome_var])
predictions=Rgr.predict(y)
print(predictions)

actual=testdf[outcome_var].tolist()
#val=accuracy_score(actual,predictions)
#print("Accuracy is : %f " % (val))



def PREDICTION(val):
    Sal=Rgr.predict(val)
    return Sal




re=[[60,1,1,2,1,1,1,1,3,2,2,1,2,0,1,2,1,0,1,2,1,2,1,0,1,2,1,2,1,2,1,2,750,250]]
pre=PREDICTION(list(re))
print("Sales Price=$%d" %(np.round(pre)))
