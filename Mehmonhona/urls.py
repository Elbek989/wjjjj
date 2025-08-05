from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deal/<int:room_id>/', views.bron_qilish, name='deal'),
    path('add-user/', views.add_user, name='add_user'),
    path('users/', views.show_users, name='show_users'),
]
