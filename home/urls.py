from . import views
from django.urls import path


urlpatterns = [
    path('',views.signup,name='signup'),
    path('home/',views.index,name='home'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
    # path('forget-password/',views.forget_password,name='forget-password'),
    # path('change-password/<str:username>/<str:token>/',views.change_password,name='change-password'),

]