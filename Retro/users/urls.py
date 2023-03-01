from django.urls import path

from users import views

app_name = 'urls'

urlpatterns = [
    path('login/', views.page_login, name='login'),
    path('registration/', views.page_registration, name='registration'),
    path('logout/', views.page_logout, name='logout'),
    path('profile/', views.page_profile, name='profile')
]
