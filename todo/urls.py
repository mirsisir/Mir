
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<task_id>',views.delete,name='delete'),
    path('marking/<task_id>', views.marking, name='marking'),
    path('update/<task_id>', views.update , name='update'),
    path('today',views.today,name='today'),
 

]