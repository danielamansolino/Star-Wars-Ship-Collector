from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ships/', views.ships_index, name='index'),
    path('ships/<int:ship_id>/', views.ships_detail, name='detail'),
    path('ships/create/', views.ShipCreate.as_view(), name='ships_create'),
    path('ships/<int:pk>/update/', views.ShipUpdate.as_view(), name='ships_update'),
    path('ships/<int:pk>/delete/', views.ShipDelete.as_view(), name='ships_delete'),
    path('ships/<int:ship_id>/add_task/', views.add_task, name='add_task'),
]