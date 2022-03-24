from django.urls import path
from .views import RegisterView

app_name = "newsboardapi"

urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    
]

