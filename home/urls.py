from django.urls import path
from.import views

urlpatterns = [
  
    path('district/', views.districts, name='district'),
    path('view_district/', views.view_district, name='view_district'),

    path('taluk/', views.taluk, name='taluk'), 
    path('view_taluk/', views.view_taluk, name="view_taluk"),


    path('vaccine/', views.vaccine, name='vaccine'), 
    path('view_vaccine/', views.view_vaccine, name="view_vaccine"),
    path('delete_vaccine/<int:vid>/', views.delete_vaccine, name="delete_vaccine"),

    path('user/', views.user, name='user'), 
    path('user_records/', views.user_records, name="user_records"),
    path('view_user/', views.view_user, name="view_user"),

    path('user_slot_booking/', views.user_slot_booking, name='user_slot_booking'),
    path('view_slot/', views.view_slot, name="view_slot"), 

    path('vaccine_center/', views.vaccine_center, name="vaccine_center"),

    path('add_vaccinated/', views.vaccination, name="add_vaccinated"),
    path('view_vaccinated/', views.view_vaccinated, name="view_vaccinated"),
    path('due_vaccinated/', views.due_vaccinated, name="due_vaccinated"),


    
  
 
]
