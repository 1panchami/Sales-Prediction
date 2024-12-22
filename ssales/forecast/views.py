from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.http import HttpResponse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler,OrdinalEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestRegressor






def login(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['psw']
        user=auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"login.html")
        
    return render(request,"login.html")



def home(request):
     return render(request,"home.html")


def registration(request):
    return  render(request,'registration.html')

def saveuser(request):
    username=request.POST['uname']
    password = request.POST['psw']
    

    newusers=User(username=username,password=password)
    newusers.save()
    return render(request, 'hhh.html')

def verifyuser(request):
    username = request.POST.get('uname')
    password = request.POST.get('psw')

    user= User.objects.filter(username=username)

    for u in user:
        if u.password==password:
            return render(request,'home.html')
        else:
            return render(request, 'hh.html')
def hh(request):
    return render(request,"login.html")
def hhh(request):
    return render(request,"login.html")
        
def hhome(request):
    return render(request,"index.html")
def result(request):
    TV=request.POST['tv']
    Radio=request.POST['radio']
    Newspaper=request.POST['news']
    values=[TV,Radio,Newspaper]
    values=np.reshape(values,(1,-1))
    data= pd.read_csv('Advertising_INR.csv')
    print(data)
    data=data.iloc[:,1:]
    data.isna().sum()
    data=data[data['Newspaper_INR']<=90]
    x=data.drop(columns=['Sales_INR'])
    y=data['Sales_INR']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    column_trans=make_column_transformer((OneHotEncoder(sparse=False),[]),remainder='passthrough')
    scaler=StandardScaler()
    oe=OrdinalEncoder()
    r=RandomForestRegressor(n_estimators=10,random_state=0)
    pipe=make_pipeline(column_trans,scaler,r) 
    pipe.fit(x_train,y_train)
    y_pred_r=pipe.predict(x_test)
    score=r2_score(y_test,y_pred_r)
    result=pipe.predict(values)
    result=result[0]
    result=round(result)
    print("Accuracy",score)
    print("Result",result)
    return render(request,'result.html',{'result':result})


