from django.urls import path
from .views import RegisterView,LoginView,PostApiView

app_name = "newsboardapi"

urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('posts-list/',PostApiView.as_view(),name='posts_list'),
    
]

