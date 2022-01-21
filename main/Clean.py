import numpy as np
import pandas as pd
####### import os
from .store import getsymptoms, getDiseases, getReplaceDict
from sklearn.svm import SVC
# import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
l1= getsymptoms()

disease= getDiseases()

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA and Path
####### path = os.getcwd() + r'\\main\\'

# tr=pd.read_csv(path + "Testing.csv")
tr = pd.read_csv(r'https://raw.githubusercontent.com/Mr-Amit/Disease-Prediction-Using-MLwithDjango/master/main/Testing.csv')

tr.replace(getReplaceDict(),inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA

# df=pd.read_csv(path + "Training.csv")
df = pd.read_csv(r"https://raw.githubusercontent.com/Mr-Amit/Disease-Prediction-Using-MLwithDjango/master/main/Training.csv")

#df =df.iloc[:,[36,51,52,53,54,55,88,104,105,111,112,71,72,73,77,113,114,120,108,118,101,99,58,80]]
df.replace(getReplaceDict(),inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

# def message():
#     if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
#         messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
#     else :
#         NaiveBayes()

def NaiveBayes(symptoms):
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    
    # y_pred = gnb.predict(X_test)
    # # print(accuracy_score(y_test, y_pred))
    # print("Naive bayes : ",end='')
    # print(accuracy_score(y_test, y_pred, normalize=False))

    # psymptoms = [symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4]]
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]


    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break
    
    if (h == 'no'):
        return "Not sufficient data"
    if (h=='yes'):
        return disease[a]
    else:
        return "No Disease"
        
def randomforest(symptoms):
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier(n_estimators=100,random_state=50,n_jobs=-1,oob_score=True)
    clf4 = clf4.fit(X,np.ravel(y))
    # calculating accuracy 
    # from sklearn.metrics import accuracy_score

    # y_pred=clf4.predict(X_test)

    # print(accuracy_score(y_test, y_pred))
    # print(" Random Forest :",end='')
    # print(accuracy_score(y_test, y_pred,normalize=False))
    
    # psymptoms = [symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4]]
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        return disease[a]
    else:
        return "No Disease"

def DecisionTree(symptoms):
    from sklearn import tree
    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)
    # from sklearn.metrics import accuracy_score
    # y_pred=clf3.predict(X_test)
#     print(accuracy_score(y_test, y_pred))

#    print(accuracy_score(y_test, y_pred,normalize=False))
#     psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        return disease[a]
    else:
        return ("No Disease")
# print(Symptom1) #       sdsdsdsds


df1 = pd.read_csv(r"https://raw.githubusercontent.com/Mr-Amit/Disease-Prediction-Using-MLwithDjango/master/main/Prototype.csv")
def functionSVM(symptoms):

    # df1 = pd.read_csv(path + 'Prototype.csv')
    
    X = df1.drop(columns="prognosis")
    y = df1['prognosis'] 
    #print(X.head()) 
    #print(y.head()) 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101) 
    #model = SVC(gamma='scale', kernel='linear') 
    model = SVC( kernel='rbf' , gamma =0.5, C = 0.1) 
    #gradient boosting  
    #moecisidel=donTreeClassifier(kernel='linear) 
    #adaboost = AdaBoostClassifier(base_estimator=model,algorithm='SAMME',n_estimators=400,learning_rate=1)  
    #boostmodel=adaboost.fit(X_train,y_train)  
    #y_pred=boostmodel.predict(X_test)  
    #print(y_pred)
    #-----------------------------------------------
    
    temp = model.fit(X_train, y_train) 
    predictions = model.predict(X_test) 
    l = [0]*132

    l = np.array(l)
    f = pd.Series(l, index = df1.columns[:-1])
    for sympt in symptoms:
        f[sympt] = 1
    # print(f, 'ffffffffffffffff')
    predictions = model.predict([f]) 
    # print(predictions, type(predictions))

    # from sklearn.metrics import accuracy_score
    # y_pred=temp.predict(X_test)
    # print(accuracy_score(y_test, y_pred))
    # print(" SVM :",end='')
    # print(accuracy_score(y_test, y_pred,normalize=False))

    return predictions[0]

# from django.core.cache import cache # This is the memcache cache.

# def flush():
#     # This works as advertised on the memcached cache:
#     cache.clear()

def runApp(symptoms = ['sweating','dehydration','blood_in_sputum','family_history','high_fever']):
    dis = []
    dis.append(NaiveBayes(symptoms))
    dis.append(randomforest(symptoms))
    dis.append(functionSVM(symptoms))
    # flush()
    return dis