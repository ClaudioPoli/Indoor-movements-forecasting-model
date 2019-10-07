import numpy as np
import warnings
warnings.filterwarnings("ignore")

""" Funzioni che permettono di creare delle colorMap di diverse dimensioni"""
def mat2(dims,q,k):
    aa = np.zeros(dims)
    if q==1:
        aa[1, 0] = 1
    if q==2:
        aa[1, 1] = 1
    if q==3:
        aa[0, 1] = 1   
    if q==4:
        aa[0, 0] = 1
    
    if k==1:
        aa[1, 0] = 2
    if k==2:
        aa[1, 1] = 2
    if k==3:
        aa[0, 1] = 2   
    if k==4:
        aa[0, 0] = 2
    
    return aa

def mat3(dims,q,k):
    aa = np.zeros(dims)
    if q==1:
        aa[2, 0] = 1
    if q==2:
        aa[2, 1] = 1
    if q==3:
        aa[2, 2] = 1   
    if q==4:
        aa[1, 2] = 1
    if q==5:
        aa[1, 1] = 1
    if q==6:
        aa[1, 0] = 1
    if q==7:
        aa[0, 0] = 1   
    if q==8:
        aa[0, 1] = 1
    if q==9:
        aa[0, 2] = 1
    
    if k==1:
        aa[2, 0] = 2
    if k==2:
        aa[2, 1] = 2
    if k==3:
        aa[2, 2] = 2   
    if k==4:
        aa[1, 2] = 2
    if k==5:
        aa[1, 1] = 2
    if k==6:
        aa[1, 0] = 2
    if k==7:
        aa[0, 0] = 2   
    if k==8:
        aa[0, 1] = 2
    if k==9:
        aa[0, 2] = 2
    
    return aa

def mat4(dims,q,k):
    aa = np.zeros(dims)
    if q==1:
        aa[3, 0] = 1
    if q==2:
        aa[3, 1] = 1
    if q==3:
        aa[3, 2] = 1   
    if q==4:
        aa[3, 3] = 1
    if q==5:
        aa[2, 3] = 1
    if q==6:
        aa[2, 2] = 1
    if q==7:
        aa[2, 1] = 1   
    if q==8:
        aa[2, 0] = 1
    if q==9:
        aa[1, 0] = 1
    if q==10:
        aa[1, 1] = 1
    if q==11:
        aa[1, 2] = 1   
    if q==12:
        aa[1, 3] = 1
    if q==13:
        aa[0, 3] = 1
    if q==14:
        aa[0, 2] = 1
    if q==15:
        aa[0, 1] = 1   
    if q==16:
        aa[0, 0] = 1
        
    if k==1:
        aa[3, 0] = 2
    if k==2:
        aa[3, 1] = 2
    if k==3:
        aa[3, 2] = 2   
    if k==4:
        aa[3, 3] = 2
    if k==5:
        aa[2, 3] = 2
    if k==6:
        aa[2, 2] = 2
    if k==7:
        aa[2, 1] = 2   
    if k==8:
        aa[2, 0] = 2
    if k==9:
        aa[1, 0] = 2
    if k==10:
        aa[1, 1] = 2
    if k==11:
        aa[1, 2] = 2   
    if k==12:
        aa[1, 3] = 2
    if k==13:
        aa[0, 3] = 2
    if k==14:
        aa[0, 2] = 2
    if k==15:
        aa[0, 1] = 2   
    if k==16:
        aa[0, 0] = 2
    return aa

def mat5(dims,q,k):
    aa = np.zeros(dims)
    if q==1:
        aa[4, 0] = 1
    if q==2:
        aa[4, 1] = 1
    if q==3:
        aa[4, 2] = 1   
    if q==4:
        aa[4, 3] = 1
    if q==5:
        aa[4, 4] = 1
    if q==6:
        aa[3, 4] = 1
    if q==7:
        aa[3, 3] = 1   
    if q==8:
        aa[3, 2] = 1
    if q==9:
        aa[3, 1] = 1
    if q==10:
        aa[3,0] = 1
    if q==11:
        aa[2, 0] = 1
    if q==12:
        aa[2, 1] = 1
    if q==13:
        aa[2, 2] = 1   
    if q==14:
        aa[2, 3] = 1
    if q==15:
        aa[2, 4] = 1
    if q==16:
        aa[1, 4] = 1
    if q==17:
        aa[1, 3] = 1   
    if q==18:
        aa[1, 2] = 1
    if q==19:
        aa[1, 1] = 1
    if q==20:
        aa[1,0] = 1
    if q==21:
        aa[0, 0] = 1
    if q==22:
        aa[0, 1] = 1
    if q==23:
        aa[0, 2] = 1   
    if q==24:
        aa[0, 3] = 1
    if q==25:
        aa[0, 4] = 1


    if k==1:
        aa[4, 0] = 2
    if k==2:
        aa[4, 1] = 2
    if k==3:
        aa[4, 2] = 2   
    if k==4:
        aa[4, 3] = 2
    if k==5:
        aa[4, 4] = 2
    if k==6:
        aa[3, 4] = 2
    if k==7:
        aa[3, 3] = 2   
    if k==8:
        aa[3, 2] = 2
    if k==9:
        aa[3, 1] =2
    if k==10:
        aa[3,0] = 2
    if k==11:
        aa[2, 0] = 2
    if k==12:
        aa[2, 1] = 2
    if k==13:
        aa[2, 2] = 2   
    if k==14:
        aa[2, 3] = 2
    if k==15:
        aa[2, 4] = 2
    if k==16:
        aa[1, 4] = 2
    if k==17:
        aa[1, 3] = 2   
    if k==18:
        aa[1, 2] = 2
    if k==19:
        aa[1, 1] =2
    if k==20:
        aa[1,0] = 2
    if k==21:
        aa[0, 0] = 2
    if k==22:
        aa[0, 1] = 2
    if k==23:
        aa[0, 2] = 2   
    if k==24:
        aa[0, 3] = 2
    if k==25:
        aa[0, 4] = 2
    
    return aa

def mat6(dims,q,k):
    aa = np.zeros(dims)
    if q==1:
        aa[5, 0] = 1
    if q==2:
        aa[5, 1] = 1
    if q==3:
        aa[5, 2] = 1   
    if q==4:
        aa[5, 3] = 1
    if q==5:
        aa[5, 4] = 1
    if q==6:
        aa[5, 5] = 1
    if q==7:
        aa[4, 5] = 1   
    if q==8:
        aa[4, 4] = 1
    if q==9:
        aa[4, 3] = 1
    if q==10:
        aa[4,2] = 1
    if q==11:
        aa[4, 1] = 1
    if q==12:
        aa[4, 0] = 1
    if q==13:
        aa[3, 0] = 1   
    if q==14:
        aa[3, 1] = 1
    if q==15:
        aa[3, 2] = 1
    if q==16:
        aa[3, 3] = 1
    if q==17:
        aa[3, 4] = 1   
    if q==18:
        aa[3, 5] = 1
    if q==19:
        aa[2, 5] = 1
    if q==20:
        aa[2,4] = 1
    if q==21:
        aa[2, 3] = 1
    if q==22:
        aa[2, 2] = 1
    if q==23:
        aa[2, 1] = 1   
    if q==24:
        aa[2, 0] = 1
    if q==25:
        aa[1, 0] = 1
    if q==26:
        aa[1, 1] = 1
    if q==27:
        aa[1, 2] = 1
    if q==28:
        aa[1, 3] = 1
    if q==29:
        aa[1, 4] = 1
    if q==30:
        aa[1, 5] = 1
    if q==31:
        aa[0, 5] = 1
    if q==32:
        aa[0, 4] = 1
    if q==33:
        aa[0, 3] = 1
    if q==34:
        aa[0, 2] = 1
    if q==35:
        aa[0, 1] = 1
    if q==36:
        aa[0, 0] = 1


    if k==1:
        aa[5, 0] = 1
    if k==2:
        aa[5, 1] = 1
    if k==3:
        aa[5, 2] = 1   
    if k==4:
        aa[5, 3] = 1
    if k==5:
        aa[5, 4] = 1
    if k==6:
        aa[5, 5] = 1
    if k==7:
        aa[4, 5] = 1   
    if k==8:
        aa[4, 4] = 1
    if k==9:
        aa[4, 3] = 1
    if k==10:
        aa[4,2] = 1
    if k==11:
        aa[4, 1] = 1
    if k==12:
        aa[4, 0] = 1
    if k==13:
        aa[3, 0] = 1   
    if k==14:
        aa[3, 1] = 1
    if k==15:
        aa[3, 2] = 1
    if k==16:
        aa[3, 3] = 1
    if k==17:
        aa[3, 4] = 1   
    if k==18:
        aa[3, 5] = 1
    if k==19:
        aa[2, 5] = 1
    if k==20:
        aa[2,4] = 1
    if k==21:
        aa[2, 3] = 1
    if k==22:
        aa[2, 2] = 1
    if k==23:
        aa[2, 1] = 1   
    if k==24:
        aa[2, 0] = 1
    if k==25:
        aa[1, 0] = 1
    if k==26:
        aa[1, 1] = 1
    if k==27:
        aa[1, 2] = 1
    if k==28:
        aa[1, 3] = 1
    if k==29:
        aa[1, 4] = 1
    if k==30:
        aa[1, 5] = 1
    if k==31:
        aa[0, 5] = 1
    if k==32:
        aa[0, 4] = 1
    if k==33:
        aa[0, 3] = 1
    if k==34:
        aa[0, 2] = 1
    if k==35:
        aa[0, 1] = 1
    if k==36:
        aa[0, 0] = 1

    
    return aa
