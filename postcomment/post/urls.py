from django.urls import path
from . import  views
urlpatterns=[
    path('',views.home,name='home'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('post', views.post_view, name='post_view'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete')

]