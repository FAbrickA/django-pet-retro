from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.page_home, name='home'),
    path('about/', views.page_about, name='about'),
    path('services/', views.page_services, name='services'),
    path('portfolio/', views.page_portfolio, name='portfolio'),
    path('right-sidebar/', views.page_right_sidebar, name='right-sidebar'),
    path('contact/', views.page_contact, name='contact'),
]
