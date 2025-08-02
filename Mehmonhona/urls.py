from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deal/<int:room_id>/', views.deal, name='deal'),
    path('add-user/', views.add_user, name='add_user'),
]
