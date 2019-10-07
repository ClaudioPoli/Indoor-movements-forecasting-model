from itertools import groupby
import numpy as np
from prefixspan import PrefixSpan
from Main.main import dff
import warnings
warnings.filterwarnings("ignore")


#FUNCTIONS

""" Funzione che consente di visualizzare il menù di scelta, prendendo in input 
la scelta dell'utente"""
def menu():
    print("\n1. Analisi pattern più utenti")
    print("\n2. Analisi pattern singolo utente")
    print("\nPremere 0 per terminare l'analisi")
    scelta=int(input()) 
    return scelta


""" Funzione che consente di importare il dataframe, aggiungendo 
    informazioni utili alle successiva fase di mining """
def importing ():
    df=dff
    return df 

""" Funzione che consente di filtrare l'array @A passato come parametro sulla 
    base dell'array @B, restituendo unicamente le tuple presenti in quest'ultimo"""
def filter(A, B): 
	n = len(A) 
	return any(A == B[i:i + n] for i in range(len(B)-n + 1)) 

""" Funzione che prende in input @num, il quale definisce, in base al parametro @type,
    il numero di utenti minimo che devono aver compiuto un determinato pattern o il 
    numero di giorni in cui deve essere stato ripetuto dallo stesso utente per poter 
    considerare quest'ultimo frequente; @lenght che indica la lunghezza dei pattern che si 
    desidera considerare e @x che rappresenta una lista di liste, le quali 
    sono composte dalla sequenza di tutte le aree visitate.
    La funzione esegue poi l'algoritmo prefixSpan, impostando minsup, lunghezza
    mimina e massima sulla base dei parametri passati in input e mostra a schermo
    i pattern frequenti rilevati"""
def freq (num,lenght,x,type):
    def coverFreq (patt,matches):
        lista=[]
        k=[]
        app=0
        q=0
        for j in x:
            if(filter(patt,x[q])):
                app=app+1
            q=q+1
        
        if(app>=num):
            lista.append(patt)
            k.append(app)
            print(k,"\t",*lista)
            
    #prefixSpan configuration
    ps = PrefixSpan(x)
    ps.maxlen=lenght
    ps.minlen=lenght
    
    if(type=='user'):
        print("\n#Utenti     Pattern")
        ps.frequent(num,callback=coverFreq) 
    
    elif(type=='days'):
        print("\n#Giorni      Pattern")
        ps.frequent(num,callback=coverFreq)


""" Funzione che prende in input @x che è una lista di liste, le quali sono 
    composte, in base al valore del parametro @type, dalla sequenza di tutte 
    le aree visitate dagli utenti presenti o dall'utente scelto durante tutta
    la settimana ed esegue l'algoritmo prefixSpan mostrando a schermo la top 5
    dei pattern più frequenti di lunghezza qualsiasi """
def top(x,type):
    def coverTop (patt,matches):
        lista=[]
        k=[]
        app=0
        q=0
        for j in x:
            if(filter(patt,x[q])):
                app=app+1
            q=q+1
        
        if(app>=1):
            lista.append(patt)
            k.append(app)
            print(k,"\t",*lista)

    #prefixSpan configuration
    ps = PrefixSpan(x)
    ps.minlen=2
    
    print("\n\nPattern più ricorrenti in assoluto:")
    if (type=='user'):
        print("\n#Utenti     Pattern")
        ps.topk(5,callback=coverTop)
    elif (type=='days'):
        print("\n#Giorni      Pattern")
        ps.topk(5,callback=coverTop)
   

""" Funzione che consente di modellare il dataframe @df passato in input e di scegliere i 
    parametri @num e @lenght che saranno passati alle funzioni @freq e @top per eseguire 
    l'algoritmo prefixSpan"""
def init (df):
    #dataframe configuration
    flag=False
    while(flag==False):
        giorno=int(input("Scegliere un giorno da monitorare:"))
        dfgiorno=df.loc[df['day']==giorno]
        ora=int(input("\nScegliere un'ora da monitorare:"))
        dfora=dfgiorno.loc[dfgiorno['hour']==ora]
        users=dfora['Username'].values
        users=np.unique(users)
        print("\nSono presenti ",len(users)," utenti:\n ")
        q=0
        for j in users:
            print(users[q],sep='\n')
            q=q+1

        if(len(users)==0 | len(users)==1):
            print("Riprova")
        elif(len(users)>1):
            flag=True

    
    #pattern configuration
    lenght=int(input("\nScegliere la lunghezza dei pattern da estrarre: "))
    num=int(input("\nQuanti utenti devono aver compiuto il pattern per poterlo considerare rilevante? "))

    #users
    x=[]
    k=0
    for i in users:
        name=users[k]
        userList=dfora.loc[dfora['Username']==name]
        userArea=userList['Area'].values
        userArea= [k[0]for k in groupby (userArea)]
        x.append(userArea)
        k=k+1
    
    freq(num,lenght,x,"user")
    top(x,"user")

""" Funzione che consente di modellare il dataframe @df passato in input e di scegliere i 
    parametri @num e @lenght che saranno passati alle funzioni @freqDay e @topDay per eseguire 
    l'algoritmo prefixSpan"""
def singleInit(df):  
    #dataframe configuration
    sett=False
    while(sett==False):
        settimana=int(input("Scegliere una settimana da monitorare:\n1.1-7Luglio \n2.8-14 Luglio \n3.15-21 Luglio\n4.22-29 Luglio\n"))
        if(settimana == 1): 
            weekDf = df.loc[(df['week']== 27)]
            sett=True
        elif(settimana == 2):
            weekDf = df.loc[(df['week']== 28)]
            sett=True
        elif(settimana == 3):
            weekDf = df.loc[(df['week']== 29)]
            sett=True
        elif(settimana == 4):
            weekDf = df.loc[(df['week']== 30)]
            sett=True
    
    users=weekDf['Username'].values
    users=np.unique(users)
    print("\nNella settimana scelta sono presenti ",len(users)," utenti:\n ")
    q=0
    for j in users:
        print(users[q],sep='\n')
        q=q+1

    utente=str(input("Scegliere un utente: "))
    userDf=weekDf.loc[weekDf['Username']==utente] 

    hour=False
    while(hour==False):
        ora=int(input("\nScegliere un'ora in cui monitorarlo:"))
        dfora=userDf.loc[userDf['hour']==ora]
        days=dfora['day'].values
        days=np.unique(days)
        print("\nL'utente scelto è presente in ",len(days)," giorni")
        q=0
        for j in days:
            print(days[q],sep='\n')
            q=q+1

        if(len(days)==0 | len(days)==1):
            print("Riprova")
        elif(len(days)>1):
            hour=True
    

    #pattern configuration
    lenght=int(input("\nScegliere la lunghezza dei pattern da estrarre: "))
    num=int(input("\nPer quanti giorni devono essere stati ripetuti per poter essere considerati rilevanti? "))

    #days
    x=[]
    k=0
    for i in days:
        day=days[k]
        dayList=dfora.loc[dfora['day']==day]
        dayArea=dayList['Area'].values
        dayArea= [k[0]for k in groupby (dayArea)]
        x.append(dayArea)
        k=k+1
    
    freq(num,lenght,x,"days")
    top(x,"days")     

#MAIN
df=importing()
scelta=-1
while(scelta!=0):
    scelta=menu()
    if(scelta==1):init(df)
    elif(scelta==2):singleInit(df)
    else:print("Scegliere un'opzione")
    
print("Analisi terminata")
