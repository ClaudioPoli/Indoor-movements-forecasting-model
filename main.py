import pandas as pd
import warnings
from Main.AreaSizing import size2,size3,size4,size5,size6
warnings.filterwarnings("ignore")

#C:/Users/polic/Desktop/Tesi/LuglioCSV.csv

#Data Mining
csv=str(input("Inserire il percorso del csv: "))
df = pd.read_csv(csv)
df['Timestamp']=pd.to_datetime(df['Timestamp'],infer_datetime_format=True)

#Data cleaning
df=df.dropna()

#Feature Engineering
df['hour'] = df['Timestamp'].dt.hour
df['day'] = df['Timestamp'].dt.day
df['week'] = df['Timestamp'].dt.week
df['weekday'] = df['Timestamp'].dt.weekday
df['minute'] = df['Timestamp'].dt.minute

maxX= df['X'].max()
maxY=df['Y'].max()


#MAIN
flag=False
while(flag==False):
    scelta=int(input("In quante aree dividere la mappa?"))
    if(scelta==4):
        dff=size2(maxX,maxY,df)
        flag=True
    elif(scelta==9):
        dff=size3(maxX,maxY,df)
        flag=True
    elif(scelta==16):
        dff=size4(maxX,maxY,df)
        flag=True
    elif(scelta==25):
        dff=size5(maxX,maxY,df)
        flag=True
    elif(scelta==36):
        dff=size6(maxX,maxY,df)
        flag=True

