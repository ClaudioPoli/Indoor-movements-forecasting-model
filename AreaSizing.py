import numpy as np
import warnings
warnings.filterwarnings("ignore")

#FUNCTIONS

#2X2
def size2(x,y,df):
    sliceX= x/2
    sliceY=y/2
    
    conditions = [
        (df['X']<= sliceX) & (df['Y']<=sliceY),
        (df['X']>sliceX) & (df['Y']<=sliceY),

        (df['X']<=sliceX) & (df['Y']>sliceY),
        (df['X']>sliceX) & (df['Y']>sliceY)]

    choices = [1,2,3,4]
    df['Area'] = np.select(conditions, choices,default='0')
    df=df.convert_objects(convert_numeric=True)
    #plt.scatter(df.X,df.Y,c=df.newArea,s=2,cmap='gnuplot')
    #plt.show()
    return df

#3X3
def size3(x,y,df):
    sliceX= x/3
    sliceY=y/3

    conditions = [
        (df['X']<=sliceX) & (df['Y']<=sliceY),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']<=sliceY),
        
        (df['X']<=sliceX) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3))
        ]
    choices = [1,2,3,4,5,6,7,8,9]
    df['Area'] = np.select(conditions, choices,default='0')
    df=df.convert_objects(convert_numeric=True)
    #plt.scatter(df.X,df.Y,c=df.Area,s=2,cmap='gnuplot')
    #plt.show()
    return df

#4X4
def size4 (x,y,df):
    sliceX=x/4
    sliceY=y/4

    conditions = [
        (df['X']<=sliceX) & (df['Y']<=sliceY),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']<=sliceY), 
        
        (df['X']<=sliceX) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),

        (df['X']<=sliceX) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4))
    ]

    choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    df['Area'] = np.select(conditions, choices,default='0')
    df=df.convert_objects(convert_numeric=True)
    #plt.scatter(df.X,df.Y,c=df.newArea,s=2,cmap='gnuplot')
    #plt.show()
    return df
#5X5
def size5 (x,y,df):
    sliceX=x/5
    sliceY=y/5

    conditions = [
        (df['X']<=sliceX) & (df['Y']<=sliceY),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']<=sliceY), 
        
        (df['X']<=sliceX) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),

        (df['X']<=sliceX) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),

    ]

    choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    df['Area'] = np.select(conditions, choices,default='0')
    df=df.convert_objects(convert_numeric=True)
    #plt.scatter(df.X,df.Y,c=df.newArea,s=2,cmap='gnuplot')
    #plt.show()
    return df
#6X6
def size6 (x,y,df):
    sliceX=x/6
    sliceY=y/6

    conditions = [
        (df['X']<=sliceX) & (df['Y']<=sliceY),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']<=sliceY),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']<=sliceY), 
        
        (df['X']<=sliceX) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']>sliceY) & (df['Y']<=(sliceY*2)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']>(sliceY*2)) & (df['Y']<=(sliceY*3)),

        (df['X']<=sliceX) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']>(sliceY*3)) & (df['Y']<=(sliceY*4)),
        
        (df['X']<=sliceX) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']>(sliceY*4)) & (df['Y']<=(sliceY*5)),

        (df['X']<=sliceX) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),
        (df['X']>sliceX) & (df['X']<=(sliceX*2)) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),
        (df['X']>(sliceX*2)) & (df['X']<=(sliceX*3)) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),
        (df['X']>(sliceX*3)) & (df['X']<=(sliceX*4)) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),
        (df['X']>(sliceX*4)) & (df['X']<=(sliceX*5)) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),
        (df['X']>(sliceX*5)) & (df['X']<=(sliceX*6)) & (df['Y']>(sliceY*5)) & (df['Y']<=(sliceY*6)),

    ]

    choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    df['Area'] = np.select(conditions, choices,default='0')
    df=df.convert_objects(convert_numeric=True)
    #plt.scatter(df.X,df.Y,c=df.newArea,s=2,cmap='gnuplot')
    #plt.show()
    return df

