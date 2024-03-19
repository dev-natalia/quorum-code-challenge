from django.urls import path
from app_quorum import views

urlpatterns = [
    path('', views.home, name='home'),
    path('legislators/', views.legislators, name='legislators'),
    path('bills/', views.bills, name='bills')
]
