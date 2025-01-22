from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Questions/', views.Questions, name="Question"),
    path('tags/' , views.tags , name ='tags'),
]