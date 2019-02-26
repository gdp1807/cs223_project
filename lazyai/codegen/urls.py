from django.urls import path

from . import views

app_name = 'codegen'
urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate, name='generate'),
    path('output/', views.output, name='output')
]
