"""
URL configuration for dp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage,name='home'),
    path('login/', views.loginpage, name='login'),
    path('', views.signuppage, name='signup'), 
    path('logout/', views.logout_view, name='logout'), # Corrected name
]

    # path('about-Us/',views.aboutUs),
    # path('course/',views.course),
    # path('course/<int:courseid>',views.courseDetails),
    # path('userform/',views.userform),
    # path('aboutus/', views.about_us_view, name='aboutus') , # Use the correct path and view
    # path('contact/', views.contact_us_view, name='contact'),
    # path('calculator/', views.calculator)
     
     


