from os import close
from django.http import request
from django.shortcuts import redirect, render
import mysql.connector as sql
import requests
from subprocess import run, PIPE
import sys
from .models import *

fn = ''
ln = ''
em = ''
pwd = ''
cpwd = ''
email = ''
passwd = ''



# Create your views here.
def signup(request):
    global fn,ln,em,pwd,cpwd
    
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="Aditisql", database="website")
        cursor = m.cursor()
        d = request.POST
        
        for key, value in d.items():
            if key == "first_name":
                fn = value
            
            if key == "last_name":
                ln = value
                
            if key == "email":
                em = value
                
            if key == "pwd":
                pwd = value
                
        c = "insert into user Values('{}', '{}', '{}', '{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()

        
    return render(request, 'login.html')


def loginaction(request):
    global email,passwd
    while request.method=="POST":
        n=sql.connect(host="localhost",user="root",passwd="Aditisql",database='website')
        cursor=n.cursor()
        dr=request.POST
        for key,value in dr.items():
            if key=="Email":
                email=value
            if key=="password":
                passwd=value
        
        cr="select * from user where Email ='{}' and password='{}'".format(email,passwd)
        cursor.execute(cr)
        t=tuple(cursor.fetchall())
        if t==():
            cursor.close()
            return render(request,'error.html')
        else:
            cursor.close()
                 
            return render(request,"home.html")

    return render(request,'login.html')


def login(request):
    context = {}
    login = request.POST.get('login', None)
    context['login'] = login
    return render(request, 'login.html', context)

def log(request):
    global fn,ln,em,pwd,cpwd
    
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="Aditisql", database="website")
        cursor = m.cursor()
        d = request.POST
        
        for key, value in d.items():
            if key == "first_name":
                fn = value
            
            if key == "last_name":
                ln = value
                
            if key == "email":
                em = value
                
            if key == "pwd":
                pwd = value
                
        c = "insert into user Values('{}', '{}', '{}', '{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        cursor.close()
        m.commit()

    return redirect("/")

def button(request):
    return render((request), 'login.html')

def quiz(request):
    return render((request), 'quiz.html')
    
def quizmod1(request):
    return render((request), 'quizmod1.html')




