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
    path('ships/<int:ship_id>/add_photo/', views.add_photo, name='add_photo'),
    path('ships/<int:ship_id>/assoc_crew/<int:crew_id>', views.assoc_crew, name='assoc_crew'),
    path('ships/<int:ship_id>/unassoc_crew/<int:crew_id>', views.unassoc_crew, name='unassoc_crew'),
    path('crew/', views.CrewList.as_view(), name='crew_index'),
    path('crew/<int:pk>/', views.CrewDetail.as_view(), name='crew_detail'),
    path('crew/create/', views.CrewCreate.as_view(), name='crew_create'),
    path('crew/<int:pk>/update/', views.CrewUpdate.as_view(), name='crew_update'),
    path('crew/<int:pk>/delete/', views.CrewDelete.as_view(), name='crew_delete'),
]