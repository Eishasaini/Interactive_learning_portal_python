"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import signup
from signup.views import home
from login.views import loginaction
from signup.views import logout
from login.views import *
from signup.views import *
'''from signup.views import mod2
from signup.views import mod3
from signup.views import mod4
from signup.views import mod5
from login.views import button
#from login.views import quiz'''


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', loginaction),
    path('register/', signup),
    path('home/', home),
    path('aboutus/', about),
    path('mod1/', mod1),
    path('mod2/', mod2),
    path('mod3/', mod3),
    path('mod4/', mod4),
    path('mod5/', mod5),
    path('mod6/', mod6),
    path('mod7/', mod7),
    path('mod8/', mod8),
    path('login/', log),
    path('mod1-quiz/', quizmod1),
    path('mod2-quiz/', quizmod1),
    path('mod3-quiz/', quizmod1),
    path('mod4-quiz/', quizmod1),
    #path('login/', log),
]
