from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('questions/', views.questions, name="questions"),
    path('tags/' , views.tags , name ='tags'),
    path('adminhome/' , views.admin , name ='adminhome'),
]