from django.shortcuts import redirect, render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = ''
cpwd = ''


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

        
    return redirect('/login/')




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def logout(request):
    context = {}
    logout = request.POST.get('logout', None)
    context['logout'] = logout
    return render(request, 'login.html', context)


def mod1(request):
    return render(request, 'mod1.html')


def mod2(request):
    return render(request, 'mod2.html')


def mod3(request):
    return render(request, 'mod3.html')


def mod4(request):
    return render(request, 'mod4.html')

def mod5(request):
    return render(request, 'mod5.html')

def mod6(request):
    return render(request, 'mod6.html')

def mod7(request):
    return render(request, 'mod7.html')

def mod8(request):
    return render(request, 'mod8.html')






   