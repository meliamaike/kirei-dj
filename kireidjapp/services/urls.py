from django.urls import path
from . import views

app_name = "services"
urlpatterns = [
    #/services/
    path("", views.index, name = "index"),
    path("all/", views.all_services, name = "all_services"),
    
]